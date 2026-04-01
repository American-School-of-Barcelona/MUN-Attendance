

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "mun.db"
CHAIR_PASSWORD = "MUNPassword2026"
ADMIN_PASSWORD = "MUNAdmin2026"
SECRET_KEY = "9f3a8c2d7b4e1f6a9c0d2b3e4f5a6c7d"

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def rows_to_dicts(rows: list[sqlite3.Row]) -> list[dict[str, Any]]:
    return [dict(row) for row in rows]


def is_authenticated() -> bool:
    return session.get("role") in {"chair", "admin"}


def is_admin() -> bool:
    return session.get("role") == "admin"


def require_admin() -> tuple[dict[str, str], int] | None:
    if not is_admin():
        return {"error": "Admin access required."}, 403
    return None


def require_auth() -> tuple[dict[str, str], int] | None:
    if not is_authenticated():
        return {"error": "Authentication required."}, 401
    return None


@app.route("/")
def index() -> str:
    return render_template(
        "index.html",
        authenticated=is_authenticated(),
        is_admin=is_admin(),
    )


@app.route("/login", methods=["GET", "POST"])
def login() -> str:
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == CHAIR_PASSWORD:
            session["role"] = "chair"
            return redirect(url_for("index"))
        return render_template(
            "login.html",
            error="Invalid chair password.",
            authenticated=is_authenticated(),
            is_admin=is_admin(),
        )
    return render_template(
        "login.html",
        error=None,
        authenticated=is_authenticated(),
        is_admin=is_admin(),
    )


@app.route("/admin-login", methods=["GET", "POST"])
def admin_login() -> str:
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == ADMIN_PASSWORD:
            session["role"] = "admin"
            return redirect(url_for("admin_page"))
        return render_template(
            "admin_login.html",
            error="Invalid admin password.",
            authenticated=is_authenticated(),
            is_admin=is_admin(),
        )
    return render_template(
        "admin_login.html",
        error=None,
        authenticated=is_authenticated(),
        is_admin=is_admin(),
    )


@app.route("/logout")
def logout() -> Any:
    session.clear()
    return redirect(url_for("index"))


@app.route("/attendance")
def attendance_page() -> str:
    return render_template(
        "attendance.html",
        authenticated=is_authenticated(),
        is_admin=is_admin(),
    )


@app.route("/participation")
def participation_page() -> str:
    return render_template(
        "participation.html",
        authenticated=is_authenticated(),
        is_admin=is_admin(),
    )


@app.route("/admin")
def admin_page() -> str:
    if not is_admin():
        return redirect(url_for("admin_login"))
    return render_template(
        "admin.html",
        authenticated=is_authenticated(),
        is_admin=is_admin(),
    )


@app.route("/api/committees")
def api_committees() -> Any:
    conn = get_db_connection()
    rows = conn.execute(
        """
        SELECT committee_code, committee_name, total_sessions
        FROM committees
        ORDER BY committee_name ASC;
        """
    ).fetchall()
    conn.close()
    return jsonify(rows_to_dicts(rows))


@app.route("/api/conference-schedule")
def api_conference_schedule() -> Any:
    conn = get_db_connection()
    rows = conn.execute(
        """
        SELECT committee_code, committee_name, total_sessions
        FROM committees
        ORDER BY committee_name ASC;
        """
    ).fetchall()
    conn.close()
    return jsonify(rows_to_dicts(rows))


# Admin filter options API
@app.route("/api/admin-filters")
def api_admin_filters() -> Any:
    admin_error = require_admin()
    if admin_error:
        return jsonify(admin_error[0]), admin_error[1]

    conn = get_db_connection()

    schools = conn.execute(
        """
        SELECT school_name
        FROM schools
        ORDER BY school_name ASC;
        """
    ).fetchall()

    committees = conn.execute(
        """
        SELECT committee_code, committee_name
        FROM committees
        ORDER BY committee_name ASC;
        """
    ).fetchall()

    countries = conn.execute(
        """
        SELECT country_name
        FROM countries
        ORDER BY country_name ASC;
        """
    ).fetchall()

    roles = conn.execute(
        """
        SELECT DISTINCT role
        FROM people
        ORDER BY role ASC;
        """
    ).fetchall()

    conn.close()
    return jsonify(
        {
            "schools": rows_to_dicts(schools),
            "committees": rows_to_dicts(committees),
            "countries": rows_to_dicts(countries),
            "roles": rows_to_dicts(roles),
        }
    )


@app.route("/api/attendance-data")
def api_attendance_data() -> Any:
    committee_code = request.args.get("committee_code", "").strip()
    session_number_raw = request.args.get("session_number", "").strip()

    if not committee_code or not session_number_raw:
        return jsonify({"error": "committee_code and session_number are required."}), 400

    try:
        session_number = int(session_number_raw)
    except ValueError:
        return jsonify({"error": "session_number must be an integer."}), 400

    conn = get_db_connection()
    rows = conn.execute(
        """
        SELECT
          p.person_id,
          cm.committee_id,
          p.person_code,
          p.first_name,
          p.last_name,
          co.country_name,
          s.school_name,
          COALESCE(a.status, 'absent') AS status
        FROM delegate_assignments da
        JOIN people p ON da.person_id = p.person_id
        JOIN countries co ON da.country_id = co.country_id
        JOIN schools s ON p.school_id = s.school_id
        JOIN committees cm ON da.committee_id = cm.committee_id
        LEFT JOIN attendance a
          ON a.person_id = p.person_id
         AND a.committee_id = cm.committee_id
         AND a.session_number = ?
        WHERE cm.committee_code = ?
        ORDER BY co.country_name ASC;
        """,
        (session_number, committee_code),
    ).fetchall()
    conn.close()
    return jsonify(rows_to_dicts(rows))


@app.route("/api/save-attendance", methods=["POST"])
def api_save_attendance() -> Any:
    auth_error = require_auth()
    if auth_error:
        return jsonify(auth_error[0]), auth_error[1]

    data = request.get_json(silent=True) or {}
    committee_code = str(data.get("committee_code", "")).strip()
    session_number = data.get("session_number")
    entries = data.get("entries", [])

    if not committee_code or session_number is None:
        return jsonify({"error": "committee_code and session_number are required."}), 400

    try:
        session_number = int(session_number)
    except ValueError:
        return jsonify({"error": "session_number must be an integer."}), 400

    allowed_statuses = {"absent", "present", "present_voting"}

    conn = get_db_connection()
    committee = conn.execute(
        "SELECT committee_id FROM committees WHERE committee_code = ?;",
        (committee_code,),
    ).fetchone()

    if committee is None:
        conn.close()
        return jsonify({"error": "Invalid committee_code."}), 400

    committee_id = committee["committee_id"]

    try:
        for entry in entries:
            person_id = int(entry.get("person_id"))
            status = str(entry.get("status", "")).strip()
            if status not in allowed_statuses:
                raise ValueError(f"Invalid attendance status: {status}")

            conn.execute(
                """
                INSERT INTO attendance (person_id, committee_id, session_number, status)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(person_id, committee_id, session_number)
                DO UPDATE SET status = excluded.status;
                """,
                (person_id, committee_id, session_number, status),
            )
        conn.commit()
    except (TypeError, ValueError) as exc:
        conn.rollback()
        conn.close()
        return jsonify({"error": str(exc)}), 400

    conn.close()
    return jsonify({"success": True})


@app.route("/api/participation-data")
def api_participation_data() -> Any:
    committee_code = request.args.get("committee_code", "").strip()
    if not committee_code:
        return jsonify({"error": "committee_code is required."}), 400

    conn = get_db_connection()

    delegations = conn.execute(
        """
        SELECT
          p.person_id,
          co.country_name AS delegation
        FROM delegate_assignments da
        JOIN people p ON da.person_id = p.person_id
        JOIN countries co ON da.country_id = co.country_id
        JOIN committees cm ON da.committee_id = cm.committee_id
        WHERE cm.committee_code = ?
        ORDER BY co.country_name ASC;
        """,
        (committee_code,),
    ).fetchall()

    participation_types = conn.execute(
        """
        SELECT type_id, type_code, type_name, points
        FROM participation_types
        ORDER BY points ASC, type_name ASC;
        """
    ).fetchall()

    recent_participation = conn.execute(
        """
        SELECT
          pa.participation_id,
          co.country_name AS delegation,
          pt.type_name,
          pt.points,
          pa.created_at
        FROM participation pa
        JOIN people p ON pa.person_id = p.person_id
        JOIN delegate_assignments da
          ON da.person_id = p.person_id
         AND da.committee_id = pa.committee_id
        JOIN countries co ON da.country_id = co.country_id
        JOIN participation_types pt ON pa.type_id = pt.type_id
        JOIN committees cm ON pa.committee_id = cm.committee_id
        WHERE cm.committee_code = ?
        ORDER BY pa.created_at DESC, pa.participation_id DESC
        LIMIT 10;
        """,
        (committee_code,),
    ).fetchall()

    call_priority = conn.execute(
        """
        SELECT
          p.person_id,
          co.country_name AS delegation,
          COALESCE(SUM(pt.points), 0) AS points
        FROM delegate_assignments da
        JOIN people p ON da.person_id = p.person_id
        JOIN countries co ON da.country_id = co.country_id
        JOIN committees cm ON da.committee_id = cm.committee_id
        LEFT JOIN participation pa
          ON pa.person_id = p.person_id
         AND pa.committee_id = cm.committee_id
        LEFT JOIN participation_types pt ON pa.type_id = pt.type_id
        WHERE cm.committee_code = ?
        GROUP BY p.person_id, co.country_name
        ORDER BY points ASC, co.country_name ASC;
        """,
        (committee_code,),
    ).fetchall()

    conn.close()
    return jsonify(
        {
            "delegations": rows_to_dicts(delegations),
            "participation_types": rows_to_dicts(participation_types),
            "recent_participation": rows_to_dicts(recent_participation),
            "call_priority": rows_to_dicts(call_priority),
        }
    )


@app.route("/api/add-participation", methods=["POST"])
def api_add_participation() -> Any:
    auth_error = require_auth()
    if auth_error:
        return jsonify(auth_error[0]), auth_error[1]

    data = request.get_json(silent=True) or {}
    committee_code = str(data.get("committee_code", "")).strip()
    person_id = data.get("person_id")
    type_id = data.get("type_id")

    if not committee_code or person_id is None or type_id is None:
        return jsonify({"error": "committee_code, person_id, and type_id are required."}), 400

    try:
        person_id = int(person_id)
        type_id = int(type_id)
    except ValueError:
        return jsonify({"error": "person_id and type_id must be integers."}), 400

    conn = get_db_connection()
    committee = conn.execute(
        "SELECT committee_id FROM committees WHERE committee_code = ?;",
        (committee_code,),
    ).fetchone()

    if committee is None:
        conn.close()
        return jsonify({"error": "Invalid committee_code."}), 400

    conn.execute(
        """
        INSERT INTO participation (person_id, committee_id, type_id)
        VALUES (?, ?, ?);
        """,
        (person_id, committee["committee_id"], type_id),
    )
    conn.commit()
    conn.close()

    return jsonify({"success": True})


@app.route("/api/delete-participation", methods=["POST"])
def api_delete_participation() -> Any:
    auth_error = require_auth()
    if auth_error:
        return jsonify(auth_error[0]), auth_error[1]

    data = request.get_json(silent=True) or {}
    participation_id = data.get("participation_id")

    if participation_id is None:
        return jsonify({"error": "participation_id is required."}), 400

    try:
        participation_id = int(participation_id)
    except ValueError:
        return jsonify({"error": "participation_id must be an integer."}), 400

    conn = get_db_connection()
    conn.execute(
        "DELETE FROM participation WHERE participation_id = ?;",
        (participation_id,),
    )
    conn.commit()
    conn.close()

    return jsonify({"success": True})



# Admin search API
@app.route("/api/admin-search")
def api_admin_search() -> Any:
    admin_error = require_admin()
    if admin_error:
        return jsonify(admin_error[0]), admin_error[1]

    school_name = request.args.get("school_name", "").strip()
    committee_code = request.args.get("committee_code", "").strip()
    country_name = request.args.get("country_name", "").strip()
    role = request.args.get("role", "").strip()

    query = """
        SELECT DISTINCT
          p.first_name,
          p.last_name,
          p.email,
          s.school_name,
          p.role,
          cm.committee_name,
          co.country_name
        FROM people p
        LEFT JOIN schools s ON p.school_id = s.school_id
        LEFT JOIN delegate_assignments da ON p.person_id = da.person_id
        LEFT JOIN committees cm ON da.committee_id = cm.committee_id
        LEFT JOIN countries co ON da.country_id = co.country_id
        WHERE 1=1
    """

    params: list[Any] = []

    if school_name:
        query += " AND s.school_name = ?"
        params.append(school_name)

    if committee_code:
        query += " AND cm.committee_code = ?"
        params.append(committee_code)

    if country_name:
        query += " AND co.country_name = ?"
        params.append(country_name)

    if role:
        query += " AND p.role = ?"
        params.append(role)

    query += " ORDER BY s.school_name ASC, p.last_name ASC, p.first_name ASC;"

    conn = get_db_connection()
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return jsonify(rows_to_dicts(rows))


if __name__ == "__main__":
    app.run(debug=True)