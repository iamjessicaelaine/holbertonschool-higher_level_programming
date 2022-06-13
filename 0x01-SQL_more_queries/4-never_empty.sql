-- script creates table id_not_null on MySQL server
-- table with fields id & name, and id gets default value of 1
CREATE TABLE IF NOT EXISTS id_not_null
( id INT DEFAULT '1',
  name VARCHAR(256)
);
