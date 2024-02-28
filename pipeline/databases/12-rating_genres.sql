-- SQL
SELECT tv_genres.name, SUM(ratings.rating)
AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres on tv_genres.id=tv_show_genres.genre_id
LEFT JOIN tv_show_ratings ON tv_show_genres.show_id=tv_show_ratings.show_id
GROUP BY name
ORDER BY rating_sum DESC;