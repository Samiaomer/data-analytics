/*
a) The actor table includes information about actors suchas actor_id,first_name. 
b) The film table includes information about films such as film_id, litle, descript. 
c) The table that contains both actor_id and film_id is the film_actor table. 
d) The rental table includes rental transactions with datws and IDs; it is hard to read becouse it uses IDs instead of names. 
e) The inventory table includes film_id and store inventory information. 
F) The rental, inventory, and film tables are needed. rental links to inventory likns to film to get movie names. 
*/ 

SELECT * FROM actor;
SELECT * FROM film;
SELECT * FROM film_actor;
SELECT * FROM rental;
