--2d Aggregate Queries 

--1. Count of movies acted by actor with actor list in descending order (by count of movies acted).

SELECT a.actor_id, a.first_name || ' ' || a.last_name AS actor_name, COUNT(fa.film_id) AS movie_count
FROM actor a
LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id
GROUP BY a.actor_id
ORDER BY movie_count DESC;

--2. Which actor has highest "Average movie rating"
SELECT a.first_name || ' ' || a.last_name AS actor_name, AVG(f.rental_rate) AS avg_rental_rate
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
GROUP BY a.actor_id
ORDER BY avg_rental_rate DESC
LIMIT 1;


--3. Count of movies per language
SELECT language.name AS language_name, COUNT(film.language_id) AS movie_count
FROM language
LEFT JOIN film ON language.language_id = film.language_id
GROUP BY language.name
ORDER BY movie_count DESC;

--4. Movie collection by stores 
SELECT s.store_id, a.city_id, f.title
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN inventory i ON s.store_id = i.store_id
JOIN film f ON i.film_id = f.film_id
ORDER BY s.store_id, f.title;


--4.1 How many movies of same film are stored in each store
SELECT s.store_id, i.film_id, COUNT(*) AS num_movies
FROM store AS s
JOIN inventory AS i ON s.store_id = i.store_id
GROUP BY s.store_id, i.film_id;


--4.2 How many unique movies in each store.
SELECT 
  s.store_id, 
  COUNT(DISTINCT i.film_id) AS unique_movies_count
FROM 
  store AS s 
  JOIN inventory AS i ON s.store_id = i.store_id
GROUP BY 
  s.store_id;
  
--5. Average length of movies.
 SELECT AVG(length) AS average_length FROM film;
  
  
--6. Which language movies are longest 
SELECT f.language_id, l.name AS language, AVG(f.length) AS avg_length
FROM film AS f
JOIN language AS l ON f.language_id = l.language_id
GROUP BY f.language_id, l.name
ORDER BY avg_length DESC;



--7. Which language movies have highest rating
SELECT l.name AS language_name, f.rating
FROM film f
JOIN language l ON f.language_id = l.language_id
WHERE f.rating = (SELECT MAX(rating) FROM film)
order by f.rating
limit 1;



--8. Count of movies by category
SELECT c.name AS category, COUNT(*) AS movie_count
FROM film_category AS fc
JOIN category AS c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY movie_count DESC;

--9. Top 3 actors who worked in horror movies
SELECT a.actor_id, a.first_name || ' ' || a.last_name AS actor_name, COUNT(*) AS movie_count
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Horror'
GROUP BY a.actor_id
ORDER BY COUNT(*) DESC
LIMIT 3;

--10. Top 3 actors who acted in action or romantic movies.
SELECT a.first_name || ' ' || a.last_name AS actor_name, COUNT(*) AS movie_count
FROM actor AS a
INNER JOIN film_actor AS fa ON a.actor_id = fa.actor_id
INNER JOIN film AS f ON fa.film_id = f.film_id
INNER JOIN film_category AS fc ON f.film_id = fc.film_id
INNER JOIN category AS c ON fc.category_id = c.category_id
WHERE c.name IN ('Action', 'Romance')
GROUP BY a.actor_id
ORDER BY movie_count DESC
LIMIT 3;

--11. Count of movies rented by Country
SELECT co.country, COUNT(*) AS total_movies_rented
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
GROUP BY co.country
ORDER BY total_movies_rented DESC;


--12. Top 3 film renting customers in each city of every country.
WITH cte AS (
  SELECT
    co.country,
    ci.city,
    cu.customer_id,
    cu.first_name || ' ' || cu.last_name AS customer_name,
    COUNT(re.rental_id) AS rentals_count,
    ROW_NUMBER() OVER (PARTITION BY co.country, ci.city ORDER BY COUNT(re.rental_id) DESC) AS row_num
  FROM
    country co
    JOIN city ci ON co.country_id = ci.country_id
    JOIN address ad ON ci.city_id = ad.city_id
    JOIN customer cu ON ad.address_id = cu.address_id
    JOIN rental re ON cu.customer_id = re.customer_id
  GROUP BY
    co.country,
    ci.city,
    cu.customer_id,
    customer_name
)
SELECT
  country,
  city,
  customer_name,
  rentals_count
FROM
  cte
WHERE
  row_num <= 3
ORDER BY
  country,
  city,
  rentals_count DESC;
  


--13. Number of employees in each store
SELECT s.store_id, COUNT(*) AS num_employees
FROM staff st
JOIN store s ON st.store_id = s.store_id
GROUP BY s.store_id;



--14. Min, Max, average, 90 percentile of rental amount paid by customers in each country.
	--Paraphrashing, which country provides more early opportunity.
SELECT 
  co.country, 
  MIN(p.amount) AS min_rental_amount, 
  MAX(p.amount) AS max_rental_amount, 
  AVG(p.amount) AS avg_rental_amount, 
  percentile_cont(0.9) WITHIN GROUP (ORDER BY p.amount) AS percentile_90
FROM 
  payment p 
  JOIN customer c ON p.customer_id = c.customer_id 
  JOIN address a ON c.address_id = a.address_id 
  JOIN city ci ON a.city_id = ci.city_id 
  JOIN country co ON ci.country_id = co.country_id 
GROUP BY 
  co.country;


--15. Which employee has rented move movies and what is earning amount per flim.
SELECT CONCAT(s.first_name, ' ', s.last_name) AS staff_name, COUNT(r.rental_id) AS num_rentals, SUM(p.amount) AS total_earning, AVG(p.amount) AS avg_earning_per_film
FROM staff s
JOIN rental r ON s.staff_id = r.staff_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY s.staff_id
ORDER BY total_earning DESC;