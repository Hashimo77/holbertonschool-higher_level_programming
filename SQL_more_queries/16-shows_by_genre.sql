-- 16-shows_by_genre.sql
-- List all shows and their linked genres, show NULL if no genre

SELECT t.title, g.name
FROM tv_shows t
LEFT JOIN tv_show_genres tg ON t.id = tg.tv_show_id
LEFT JOIN genres g ON tg.genre_id = g.id
ORDER BY t.title ASC, g.name ASC;
