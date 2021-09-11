DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS sickness;
DROP TABLE IF EXISTS symptom;
DROP TABLE IF EXISTS trailer;
DROP TABLE IF EXISTS medical_center;
DROP TABLE IF EXISTS record;
DROP TABLE IF EXISTS record_detail;

CREATE TABLE user (
  username TEXT PRIMARY KEY,
  password TEXT NOT NULL,
  name TEXT,
  email TEXT
);

CREATE TABLE sickness (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  reason TEXT,
  description TEXT
);

CREATE TABLE symptom (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  description KEY,
  id_sickness TEXT,
  FOREIGN KEY(id_sickness) REFERENCES sickness(id)
);

CREATE TABLE trailer (
  id TEXT PRIMARY KEY,
  url TEXT NOT NULL,
  id_sickness TEXT,
  FOREIGN KEY(id_sickness) REFERENCES sickness(id)
);

CREATE TABLE medical_center (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  address TEXT NOT NULL,
  phone TEXT NOT NULL
);

CREATE TABLE record (
  id TEXT PRIMARY KEY,
  username TEXT,
  image_url TEXT NOT NULL,
  createdAt TEXT NOT NULL,
  FOREIGN KEY(username) REFERENCES user(username)
);

CREATE TABLE record_detail (
  id TEXT PRIMARY KEY,
  id_record TEXT,
  id_sickness TEXT,
  result REAL NOT NULL,
  FOREIGN KEY(id_record) REFERENCES record(id),
  FOREIGN Key(id_sickness) REFERENCES sickness(id)
);