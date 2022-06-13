-- lists all cities contained in the database
-- joining the two tables in DB to give us a specific result
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.id = states.id
ORDER BY cities.id ASC;
