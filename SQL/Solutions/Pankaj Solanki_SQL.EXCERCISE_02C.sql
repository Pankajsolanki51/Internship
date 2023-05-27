--2c join queries



--1. Find actors who acted in film "Lost Bird"
SELECT actor.actor_id,f.film_id,first_name,last_name
FROM actor 
JOIN film_actor fa ON fa.actor_id = actor.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE f.title = 'LOST BIRD';


--for cross checking
SELECT * FROM public.film_actor
where film_id=533
ORDER BY actor_id ASC, film_id 



--2. Find movies of "Sci-Fi" genre
select title from film f
join film_category fc on fc.film_id = f.film_id
where fc.category_id=14 --category id for sci fi movie is given as 14


--3. Find movies of actress first_name: "PENELOPE"	last_name:"GUINESS"
SELECT title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor ON fa.actor_id = actor.actor_id
WHERE actor.first_name = 'PENELOPE' AND actor.last_name = 'GUINESS';



--4. list Genres, movies (in each Genre), actors in each movie
SELECT c.name AS category_name, f.title AS film_title, a.First_name AS actor_name
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
GROUP BY c.name, f.title, a.first_name
ORDER BY f.title;




--5. List films that are rented from inventory
SELECT f.film_id, f.title, f.release_year, f.description
FROM inventory i
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.title;



--6. List genres corresponding movies rented by customer.
SELECT c.name AS genre, f.title AS film_title, cu.first_name || ' ' || cu.last_name AS name
FROM inventory i
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
JOIN customer cu ON r.customer_id = cu.customer_id
ORDER BY c.name, f.title;


--7. List 5 rows of customer which have renated "Horror" generes.
SELECT DISTINCT ON (c.customer_id) c.customer_id, c.first_name || ' ' || c.last_name AS customer_name
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c2 ON fc.category_id = c2.category_id
WHERE c2.name = 'Horror'
ORDER BY c.customer_id, r.rental_date
LIMIT 5;



--8. List 5 staff members who have given maximum movies on rent (best performers)
SELECT s.staff_id, CONCAT(s.first_name, ' ', s.last_name) AS staff_name, COUNT(r.rental_id) AS rental_count
FROM staff s
JOIN rental r ON s.staff_id = r.staff_id
GROUP BY s.staff_id
ORDER BY rental_count DESC
LIMIT 5;



--9. List top movies types Genre (by count) rented by customers.
SELECT c.name AS genre_name, COUNT(r.rental_id) AS rental_count
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY rental_count DESC
LIMIT 16;



--10. List top movies (by count) by Genre (by count) in the inventory.
SELECT c.name AS genre_name, f.title AS movie_title, COUNT(i.inventory_id) AS inventory_count
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
JOIN inventory i ON f.film_id = i.film_id
GROUP BY c.name, f.title
ORDER BY COUNT(i.inventory_id) DESC, c.name, f.title
LIMIT 10;



--11. List of actors who have not acted in any flim.
SELECT *
FROM actor
WHERE actor.actor_id NOT IN (
    SELECT DISTINCT actor_id
    FROM film_actor
); --- result is empty hence there is no actors who have not acted in any flim



--12. List of films that are not in inventory
SELECT film.film_id, film.title
FROM film
LEFT JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.inventory_id IS NULL;



--13. List of actors who are not in inventory
SELECT actor.actor_id, actor.first_name, actor.last_name
FROM actor
WHERE actor.actor_id NOT IN (
  SELECT DISTINCT film_actor.actor_id
  FROM inventory
  JOIN rental ON inventory.inventory_id = rental.inventory_id
  JOIN film ON inventory.film_id = film.film_id
  JOIN film_actor ON film.film_id = film_actor.film_id
);   --result is empty 


--14. List of actors whose movies are not stores.
SELECT a.actor_id, a.first_name, a.last_name
FROM actor a
LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id
WHERE fa.film_id IS NULL;
--empty result



--15. List of staff who have not rented movies.
SELECT s.staff_id, s.first_name, s.last_name
FROM staff s
WHERE s.staff_id NOT IN (
  SELECT r.staff_id
  FROM rental r
)
--empty result

--16. categories which do not have movies.
SELECT c.category_id, c.name
FROM category c
LEFT JOIN film_category fc ON c.category_id = fc.category_id
WHERE fc.film_id IS NULL;


--17. Actors who acted in all movie categories
SELECT a.actor_id, a.first_name, a.last_name
FROM actor a
WHERE NOT EXISTS (
    SELECT c.category_id
    FROM category c
    WHERE NOT EXISTS (
        SELECT fc.film_id
        FROM film_category fc
        JOIN film_actor fa ON fc.film_id = fa.film_id
        WHERE fc.category_id = c.category_id
        AND fa.actor_id = a.actor_id
    )
);




--18. Actors who did NOT act in all movie categories
SELECT a.actor_id, a.first_name, a.last_name
FROM actor a
WHERE a.actor_id NOT IN (
    SELECT fa.actor_id
    FROM film_actor fa
    JOIN film_category fc ON fa.film_id = fc.film_id
    GROUP BY fa.actor_id
    HAVING COUNT(DISTINCT fc.category_id) = (SELECT COUNT(*) FROM category)
)
ORDER BY a.last_name, a.first_name;





--19. List of stores with address, city, countries.
SELECT store.store_id, address.address, city.city, country.country
FROM store
JOIN address ON store.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id;


--20. List of stores that do not have inventory.
SELECT *
FROM store
WHERE store_id NOT IN (
    SELECT DISTINCT store_id
    FROM inventory
);
--empty result



--21. List of customers who do not have movie rentals.
SELECT *
FROM customer c
LEFT JOIN rental r ON c.customer_id = r.customer_id
WHERE r.rental_id IS NULL;



--22. List of Customers in India with address.
SELECT c.first_name || ' ' || c.last_name AS customer_name, a.address, a.city_id, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
where country = 'India'
ORDER BY co.country, a.city_id, a.address;


--23. List of Customers with address all over the world.
SELECT c.first_name || ' ' || c.last_name AS customer_name, a.address, a.city_id, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
ORDER BY co.country, a.city_id, a.address;


--24. List of movies made in Japanese or Mandarin.
SELECT title, language.name AS language
FROM film
JOIN language ON film.language_id = language.language_id
WHERE language.name IN ('Japanese', 'Mandarin');




--25. List of languages with no movies.
SELECT name
FROM language
WHERE language_id NOT IN (
  SELECT DISTINCT language_id
  FROM film
  WHERE language_id IS NOT NULL
)