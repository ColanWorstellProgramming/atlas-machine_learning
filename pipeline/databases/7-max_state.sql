-- SQL
SELECT state, AVG(value) AS temp FROM temperatures GROUP BY state ORDER BY state ASC;