-- lists all cities contained in the database
-- joining the two tables in DB to give us a specific result
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON state.id = cities.states_id
ORDER BY cities.id ASC;
