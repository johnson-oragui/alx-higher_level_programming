-- Lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN hbtn_0d_tvshows.tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;

