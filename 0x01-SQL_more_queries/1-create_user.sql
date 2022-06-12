-- script creates a MySQL user with all privileges
-- create user `user_0d_1` with global privileges granted on my MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* to 'user_0d_1'@'localhost';
