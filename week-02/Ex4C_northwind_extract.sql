-- 4a) The table that holds the items Northwind sells is called 'products'.
-- 4b) The table that holds the categories/types of items is called 'categories'.

-- 5a)
SELECT * 
FROM employees;
-- 5b) -- The employee whose name looks like a bird is Nancy Davolio.

-- 6a) 
SELECT * 
FROM products;
-- This query returns 77 records.
-- You can change the result to 10 rows using the "Limit Rows" option in the toolbar.

-- 6b) 
SELECT * 
FROM products
LIMIT 10;
-- BONUS: You can limit rows using the LIMIT keyword (e.g., LIMIT 10).
-- Source: MySQL documentation / online SQL references.

-- 7)
SELECT * 
FROM categories;
-- The category ID for Seafood is 1.

-- 8)
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;