-- create db hbtn_0d_usa and table cities if they dont exist on MySQL server
-- cities as fields, id (primary key), state_id (foreign key) & name (!null)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
