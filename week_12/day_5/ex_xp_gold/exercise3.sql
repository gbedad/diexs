-- Database: public

-- Part 1
--CREATE TABLE purchases(
--id SERIAL PRIMARY KEY,
--customer_id int,
--item_id int,
--quantity_purchased smallint
--)

--INSERT INTO purchases (customer_id, item_id, quantity_purchased)
--VALUES
--('3', '3', 10),
--('5', '2', 10),
--('1', '1', 2)

--SELECT * FROM purchases
--INNER JOIN customers
--ON purchases.customer_id = customers.customer_id

--SELECT * FROM purchases
--WHERE customer_id = '5'

--SELECT * FROM purchases
--INNER JOIN customers
--ON purchases.customer_id=customers.customer_id
--INNER JOIN items
--ON purchases.item_id=items.item_id
--WHERE items.description='Large Desk' OR items.description='Small Desk'

--SELECT customers.firstname, customers.lastname, items.description FROM purchases
--INNER JOIN customers
--ON purchases.customer_id=customers.customer_id
--INNER JOIN items
--ON purchases.item_id=items.item_id
--WHERE purchases.quantity_purchased > 0

--INSERT INTO purchases (customer_id, quantity_purchased)
--VALUES
--('3', 6)

SELECT * FROM purchases







