-- a script that creates a table, `force_name` in MySQL server
-- table with fields id and name which can't be null get created
CREATE TABLE IF NOT EXISTS force_name
( id INT,
  name VARCHAR(256) NOT NULL
);
