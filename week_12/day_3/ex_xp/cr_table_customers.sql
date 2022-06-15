-- Database: public

-- DROP DATABASE IF EXISTS public;
CREATE TABLE customers(
 customer_id SERIAL PRIMARY KEY,
 firstname VARCHAR (50) NOT NULL,
 lastname VARCHAR (50) NOT NULL
)
