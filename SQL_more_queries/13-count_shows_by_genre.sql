-- 13-count_shows_by_genre.sql
-- List all genres and the number of shows linked to each

SELECT g.name AS genre,
       COUNT(tg.tv_show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres tg ON g.id = tg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
