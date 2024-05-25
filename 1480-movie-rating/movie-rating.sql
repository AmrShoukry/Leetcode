# Write your MySQL query statement below
(SELECT Users.name AS results FROM MovieRating INNER JOIN Users ON MovieRating.user_id = Users.user_id
GROUP BY MovieRating.user_id ORDER BY COUNT(MovieRating.user_id) DESC, Users.name ASC
LIMIT 1)

UNION ALL

(SELECT Movies.title FROM MovieRating INNER JOIN Movies ON MovieRating.movie_id = Movies.movie_id AND MONTH(MovieRating.created_at) = 2 AND YEAR(MovieRating.created_at) = 2020
GROUP BY MovieRating.movie_id ORDER BY SUM(MovieRating.rating) / COUNT(MovieRating.user_id) DESC, Movies.title ASC
LIMIT 1)
