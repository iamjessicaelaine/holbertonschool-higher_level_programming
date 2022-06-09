-- script lists number of records with the same score in table
-- let's find out how many peers a winner has
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
