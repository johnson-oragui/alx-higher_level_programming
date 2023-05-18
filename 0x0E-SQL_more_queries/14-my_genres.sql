-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Query to select genres of the show Dexter
SELECT tv_genres.name
FROM hbtn_0d_tvshows.tv_genres
JOIN hbtn_0d_tvshows.tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN hbtn_0d_tvshows.tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;

