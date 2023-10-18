-- lists all genres from hbtn_0d_tvshows.
-- Format: <TV Show genre> - <Number of shows linked to this genre>.

SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id)
AS 'number_of_shows'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
