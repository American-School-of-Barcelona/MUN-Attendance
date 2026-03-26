DROP TABLE IF EXISTS staging_schools;
DROP TABLE IF EXISTS staging_people;
DROP TABLE IF EXISTS staging_committees;
DROP TABLE IF EXISTS staging_countries;
DROP TABLE IF EXISTS staging_delegate_assignments;
DROP TABLE IF EXISTS staging_participation_types;

CREATE TABLE staging_schools (
  school_code TEXT,
  school_name TEXT
);

CREATE TABLE staging_people (
  person_code TEXT,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  role TEXT,
  school_code TEXT,
  school_name TEXT
);

CREATE TABLE staging_committees (
  committee_code TEXT,
  committee_name TEXT,
  total_sessions INTEGER
);

CREATE TABLE staging_countries (
  country_code TEXT,
  country_name TEXT
);

CREATE TABLE staging_delegate_assignments (
  person_code TEXT,
  committee_code TEXT,
  country_code TEXT
);

CREATE TABLE staging_participation_types (
  type_code TEXT,
  type_name TEXT,
  points INTEGER
);