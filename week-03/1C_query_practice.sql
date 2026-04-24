USE Northwind;

-- 1 
SELECT ProductID, ProductName,UnitPrice
From Products
ORDER BY UnitPrice ASC;

-- 2
Select ProductID, ProductName, UnitsInStock, UnitPrice
From Products
Where UnitsInStock <=100
ORDER BY UnitPrice DESC;

-- 3
SELECT UnitsInStock
From Products 
Where UnitsInStock >=100
ORDER BY UnitPrice DESC, ProductName ASC;

-- 4
SELECT CustomerID,Count(*)AS
CustomerCOUNT
from orders 
Group by CustomerID
Order by CustomerCount DESC;

-- 5 
SELECT CustomerID,Count(*)As 
CustomerCount
From Orders 
Where ShippedDate IS NOT NULL 
GROUP BY CustomerID 
Order BY CustomerCount DESC;

-- 6
Select ProductName,UnitsOnOrder
FRom Products 
Where UnitsInStock < 25
AND UnitsOnOrder > 0 
Order BY ProductName ASC;

-- 7
Select Title,COUNT(*)AS EmployeeCount
From Employees
Group By Title
Order By Title ASC;

-- 8 
Select Title,COUNT(*)AS
employeesCount
FROM Employees
WHERE Salary BETWEEN 2000 AND 2500
GROUP BY Title
Order BY Title ASC;





