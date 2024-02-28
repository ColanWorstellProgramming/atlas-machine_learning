-- SQL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
INNER JOIN tv_show ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;