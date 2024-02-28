-- SQL
SELECT tv_shows.title, SUM(ratings.rating) AS rating_sum
FROM tv_shows
JOIN ratings ON tv_shows.id = ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
