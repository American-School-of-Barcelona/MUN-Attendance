-- =========================
-- SCHOOLS
-- =========================
CREATE TABLE schools (
  school_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE
);

-- =========================
-- PEOPLE
-- =========================
CREATE TABLE people (
  person_id INTEGER PRIMARY KEY AUTOINCREMENT,
  school_id INTEGER,

  first_name TEXT NOT NULL,
  last_name  TEXT NOT NULL,
  email TEXT UNIQUE,

  role TEXT NOT NULL CHECK (role IN ('delegate','director','executive')),

  FOREIGN KEY (school_id) REFERENCES schools(school_id)
);

-- =========================
-- COMMITTEES
-- =========================
CREATE TABLE committees (
  committee_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  total_sessions INTEGER NOT NULL DEFAULT 0
);

-- =========================
-- COMMITTEE ROSTER
-- =========================
CREATE TABLE committee_delegates (
  committee_id INTEGER NOT NULL,
  delegate_id  INTEGER NOT NULL,

  PRIMARY KEY (committee_id, delegate_id),

  FOREIGN KEY (committee_id) REFERENCES committees(committee_id),
  FOREIGN KEY (delegate_id) REFERENCES people(person_id)
);

-- =========================
-- ATTENDANCE
-- =========================
CREATE TABLE attendance (
  attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
  committee_id INTEGER NOT NULL,
  delegate_id  INTEGER NOT NULL,
  session_number INTEGER NOT NULL,
  is_present BOOLEAN NOT NULL DEFAULT 0,

  UNIQUE (committee_id, delegate_id, session_number),

  FOREIGN KEY (committee_id) REFERENCES committees(committee_id),
  FOREIGN KEY (delegate_id) REFERENCES people(person_id)
);

-- =========================
-- PARTICIPATION TYPES
-- =========================
CREATE TABLE participation_types (
  type_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  points INTEGER NOT NULL CHECK (points >= 0)
);

-- =========================
-- PARTICIPATION
-- =========================
CREATE TABLE participation (
  participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
  committee_id INTEGER NOT NULL,
  delegate_id  INTEGER NOT NULL,
  type_id INTEGER NOT NULL,
  session_number INTEGER,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY (committee_id) REFERENCES committees(committee_id),
  FOREIGN KEY (delegate_id) REFERENCES people(person_id),
  FOREIGN KEY (type_id) REFERENCES participation_types(type_id)
);
