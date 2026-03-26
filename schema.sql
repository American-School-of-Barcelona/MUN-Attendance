DROP TABLE IF EXISTS participation;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS delegate_assignments;
DROP TABLE IF EXISTS participation_types;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS committees;
DROP TABLE IF EXISTS schools;

CREATE TABLE schools (
  school_id INTEGER PRIMARY KEY AUTOINCREMENT,
  school_code TEXT NOT NULL UNIQUE,
  school_name TEXT NOT NULL UNIQUE
);

CREATE TABLE committees (
  committee_id INTEGER PRIMARY KEY AUTOINCREMENT,
  committee_code TEXT NOT NULL UNIQUE,
  committee_name TEXT NOT NULL UNIQUE,
  total_sessions INTEGER NOT NULL DEFAULT 0 CHECK (total_sessions >= 0)
);

CREATE TABLE countries (
  country_id INTEGER PRIMARY KEY AUTOINCREMENT,
  country_code TEXT NOT NULL UNIQUE,
  country_name TEXT NOT NULL UNIQUE
);

CREATE TABLE people (
  person_id INTEGER PRIMARY KEY AUTOINCREMENT,
  person_code TEXT NOT NULL UNIQUE,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT UNIQUE,
  role TEXT NOT NULL CHECK (role IN ('delegate','director','executive')),
  school_id INTEGER NOT NULL,
  FOREIGN KEY (school_id) REFERENCES schools(school_id)
);

CREATE TABLE participation_types (
  type_id INTEGER PRIMARY KEY AUTOINCREMENT,
  type_code TEXT NOT NULL UNIQUE,
  type_name TEXT NOT NULL UNIQUE,
  points INTEGER NOT NULL CHECK (points >= 0)
);

CREATE TABLE delegate_assignments (
  assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
  person_id INTEGER NOT NULL,
  committee_id INTEGER NOT NULL,
  country_id INTEGER NOT NULL,
  UNIQUE (person_id, committee_id),
  UNIQUE (committee_id, country_id),
  FOREIGN KEY (person_id) REFERENCES people(person_id),
  FOREIGN KEY (committee_id) REFERENCES committees(committee_id),
  FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

CREATE TABLE attendance (
  attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
  person_id INTEGER NOT NULL,
  committee_id INTEGER NOT NULL,
  session_number INTEGER NOT NULL CHECK (session_number >= 1),
  is_present INTEGER NOT NULL CHECK (is_present IN (0, 1)),
  UNIQUE (person_id, committee_id, session_number),
  FOREIGN KEY (person_id) REFERENCES people(person_id),
  FOREIGN KEY (committee_id) REFERENCES committees(committee_id)
);

CREATE TABLE participation (
  participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
  person_id INTEGER NOT NULL,
  committee_id INTEGER NOT NULL,
  type_id INTEGER NOT NULL,
  session_number INTEGER CHECK (session_number >= 1),
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (person_id) REFERENCES people(person_id),
  FOREIGN KEY (committee_id) REFERENCES committees(committee_id),
  FOREIGN KEY (type_id) REFERENCES participation_types(type_id)
);
