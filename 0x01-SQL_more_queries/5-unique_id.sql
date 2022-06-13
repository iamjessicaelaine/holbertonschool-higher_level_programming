-- script creates table `unique_id` on MySQL server
-- table with name and id fields, id has default value & requires uniqueness
CREATE TABLE IF NOT EXISTS unique_id
( id INT DEFAULT '1' UNIQUE,
  name VARCHAR(256)
);
