-- Quentions I want to answer in this project

-- 1. Who are the top five stars with the most shows and most episodes, and best average rating?

--top five stars with the most shows 
SELECT people.name, COUNT(stars.person_id) AS star_count
FROM people
JOIN stars ON people.id = stars.person_id
GROUP BY people.name
ORDER BY star_count DESC
LIMIT 5;

--top five stars with the most episodes
SELECT people.name, SUM(shows.episodes) AS total_episodes
FROM people
JOIN stars ON people.id = stars.person_id
JOIN shows ON stars.show_id = shows.id
GROUP BY people.name
ORDER BY total_episodes DESC
LIMIT 5;

-- stars with best average rating
SELECT people.name, ROUND(AVG(ratings.rating), 2) AS avg_rating, COUNT(stars.person_id) AS star_count
FROM people
JOIN stars ON people.id = stars.person_id
JOIN shows ON stars.show_id = shows.id
JOIN ratings ON ratings.show_id = shows.id
GROUP BY people.name
HAVING COUNT(stars.person_id) >= 20
ORDER BY avg_rating DESC
LIMIT 5;


-- 2. What is the relationship between number of episodes and rating?



-- 3. What is the most common genre for each writer, the most common genre combination btween writters
--    and the best rating genre?
