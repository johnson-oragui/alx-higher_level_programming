--Lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Query to select the shows without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL  -- Filter shows without a genre
ORDER BY tv_shows.title ASC;

