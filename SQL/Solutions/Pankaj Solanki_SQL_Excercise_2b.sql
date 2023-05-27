--2b
--Join simple queries 
--Actor table
--1. Get first_name , last_name for actors
SELECT first_name, last_name
FROM Actor;

--2. Get first_name, last_name only 5 rows.
SELECT first_name, last_name
FROM Actor
LIMIT 5;

--3. Get first_name, last_name of 5 actors who have been modified last
SELECT first_name, last_name
FROM Actor
ORDER BY last_update DESC
LIMIT 5;

--4. Get top 5 repeating last_names of actors.
SELECT last_name, COUNT(*) as count
FROM Actor
GROUP BY last_name
ORDER BY count DESC
LIMIT 5;

--5. Get top 6 repeating first_name of actors.
SELECT first_name, COUNT(*) as count
FROM Actor
GROUP BY first_name
ORDER BY count DESC
LIMIT 6;
--Film table
--6. Get count of films in table
SELECT DISTINCT COUNT(*) FROM film;

--7. What is average movie length (use length column)
SELECT AVG(length) as avg_length
FROM film;



--8. Count of movies for each rating (use rating column)
SELECT rating, COUNT(*) as count
FROM film
GROUP BY rating;


--9. Get list of horror movies
SELECT *
FROM category
WHERE LOWER(name) LIKE '%horror%';


--10. Movies that contain CAT in title.
SELECT title
FROM film
WHERE LOWER(title) LIKE '%cat%';

--Category
--11. How many movie categories are there?
SELECT COUNT(DISTINCT name) AS num_categories
FROM category;

--12. Are category names repeating ?
SELECT DISTINCT name
FROM category
Select name from category
--both has same count of rows hence there is no repaeating

--Country & City
--13. how many countries and cities ?
SELECT COUNT(DISTINCT country) AS num_countries
FROM country;
SELECT COUNT(DISTINCT city) AS num_cities
FROM city;

--14. For each country get the list of cities.
SELECT c.country, string_agg(ct.city, ', ' ORDER BY ct.city ASC) AS cities
FROM country c
JOIN city ct ON c.country_id = ct.country_id
GROUP BY c.country;

--Customer
--15. Get list of active customers;
SELECT cu.customer_id, cu.first_name, cu.last_name, COUNT(re.rental_id) AS num_rentals
FROM customer cu
JOIN rental re ON cu.customer_id = re.customer_id
GROUP BY cu.customer_id
HAVING COUNT(re.rental_id) > 0;


--16. Do any customer share same emailID
SELECT email, COUNT(*) AS num_customers
FROM customer
GROUP BY email
HAVING COUNT(*) > 1;
--No results given hence no customers with same email are present.

--17. List of customers with same lastname
SELECT last_name, COUNT(*) AS num_customers
FROM customer
GROUP BY last_name
HAVING COUNT(*) > 1;
--No results found 

--film_category
--18. Total movies that are categoried
SELECT COUNT(DISTINCT film_id) AS num_movies_categorized
FROM film_category;


--19. Total rows in inventory
SELECT COUNT(*) AS num_rows
FROM inventory;