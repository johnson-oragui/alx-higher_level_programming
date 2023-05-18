-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_show_genres.genre AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM hbtn_0d_tvshows.tv_show_genres
GROUP BY tv_show_genres.genre
HAVING number_of_shows > 0  -- Exclude genres without any linked shows
ORDER BY number_of_shows DESC;

