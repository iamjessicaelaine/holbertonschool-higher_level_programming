-- script that lists all records of the table except  w/o name
-- say my name, say my name!!
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
