-- SQL
SELECT tv_shows.title, SUM(ratings.rating)
AS rating_sum
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id=tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC