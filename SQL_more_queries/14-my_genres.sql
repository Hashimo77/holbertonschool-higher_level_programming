-- 14-my_genres.sql
-- List all genres of the show Dexter

SELECT g.name
FROM genres g
JOIN tv_show_genres tg ON g.id = tg.genre_id
JOIN tv_shows t ON t.id = tg.tv_show_id
WHERE t.title = 'Dexter'
ORDER BY g.name ASC;
