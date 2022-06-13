-- script lists all the cities of CA that are in db hbtn_0d_usa
-- because west coast is the best coast
USE hbtn_0d_usa;
SELECT id, name FROM cities WHERE state_id
IN (
   SELECT id
   FROM states
   WHERE name = 'California'
)
ORDER BY cities.id ASC;
