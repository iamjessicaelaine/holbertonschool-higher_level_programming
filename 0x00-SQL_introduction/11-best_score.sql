-- script that lists all records with score higher than 10
-- sorting records in desc order displaying name and score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
