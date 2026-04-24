USE Northwind;

-- 1 
SELECT ProductID, ProductName, UnitPrice 
FROM products;

-- 2 
SELECT ProductID, ProductName, UnitPrice 
FROM products
WHERE UnitPrice <= 7.50;

-- 3 
SELECT ProductID, ProductName, UnitPrice, UnitsInStock, UnitsOnOrder 
FROM products
WHERE UnitsInStock = 0
AND UnitsOnOrder >= 1;

-- 4 
SELECT p.ProductID, p.ProductName, c.CategoryName
FROM Products p
JOIN Categories c
    ON p.CategoryID = c.CategoryID
    WHERE c.CategoryName = 'Seafood';
    
-- 5a 
SELECT * 
From Suppliers 
Where CompanyName = 'Tokyo Traders';

-- 5b. Products from Tokyo Traders
SELECT ProductID, ProductName, SupplierID
FROM Products
WHERE SupplierID = 4;

-- 6a. How many employees work at Northwind
SELECT COUNT(*) AS TotalEmployees
FROM Employees;

-- 6b. Employees with "manager" in job title
SELECT EmployeeID,FirstName,LastName,Title
FROM Employees
WHERE Title LIKE '%Manager%';



