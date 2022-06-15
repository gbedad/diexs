-- Database: public

-- DROP DATABASE IF EXISTS public;
CREATE TABLE items(
 item_id SERIAL PRIMARY KEY,
 description VARCHAR (50) NOT NULL,
 price SMALLINT NOT NULL
)
