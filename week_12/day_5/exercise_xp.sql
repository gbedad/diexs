-- Database: dvdrental

-- DROP DATABASE IF EXISTS dvdrental;

-- Exercise 1 DVD Rental
-- question 1
--SELECT film.rating,
--count(film.film_id)
--FROM film
--GROUP BY film.rating
--ORDER BY film.rating

-- question 2
--SELECT film_id, title, length, rental_rate
--FROM film
--WHERE (rating = 'G' OR rating = 'PG-13') AND length < 120 AND rental_rate < 3.00
--ORDER BY title

-- question 3
--UPDATE customer
--SET
--first_name = 'Gerald',
--last_name = 'Berrebi'
--WHERE customer_id = '1'
--RETURNING
--first_name,
--last_name,
--address_id

-- question 4
UPDATE address
SET
address = '68 avenue Ledru Rollin',
district = 'Paris',
city_id ='544'
WHERE address_id='5'
RETURNING
*









