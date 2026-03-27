INSERT INTO schools (school_code, school_name)
SELECT DISTINCT school_code, school_name
FROM staging_schools;

INSERT INTO committees (committee_code, committee_name, total_sessions)
SELECT DISTINCT committee_code, committee_name, total_sessions
FROM staging_committees;

INSERT INTO countries (country_code, country_name)
SELECT country_code, MIN(country_name)
FROM staging_countries
GROUP BY country_code;

INSERT INTO participation_types (type_code, type_name, points)
SELECT DISTINCT type_code, type_name, points
FROM staging_participation_types;

INSERT INTO people (person_code, first_name, last_name, email, role, school_id)
SELECT
  p.person_code,
  p.first_name,
  p.last_name,
  p.email,
  p.role,
  s.school_id
FROM staging_people p
JOIN schools s ON s.school_code = p.school_code;

INSERT INTO delegate_assignments (person_id, committee_id, country_id)
SELECT
  p.person_id,
  c.committee_id,
  co.country_id
FROM staging_delegate_assignments da
JOIN people p ON p.person_code = da.person_code
JOIN committees c ON c.committee_code = da.committee_code
JOIN countries co ON co.country_code = da.country_code;