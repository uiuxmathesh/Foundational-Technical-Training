USE [training]
SELECT *
FROM [EmployeeData]

-- Task 4
-- Write a query to calculate the tenure of each employee in complete years as of today.
SELECT DATEDIFF(YEAR, [startdate],GETDATE()) AS Tenure_Years
FROM [EmployeeData]


-- Task 5 - Calculate Annual Salary Increase
-- Assume a yearly salary increase of 3% for each employee. 
-- Write a query to calculate their new salary rounded to the nearest whole number.
SELECT [EmployeeID],[FirstName],[LastName],[Salary],([Salary]*1.03) AS Annual_Increase
FROM [EmployeeData]


USE [Joins]

CREATE TABLE Employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Salary DECIMAL(10,2),
    DepartmentID INT
);
 
CREATE TABLE Departments (
    DepartmentID INT,
    DepartmentName VARCHAR(50),
    MinSalary DECIMAL(10,2)
);
 
INSERT INTO Employees VALUES (1, 'John Doe', 50000, 101), (2, 'Jane Smith', 40000, 102);
INSERT INTO Departments VALUES (101, 'HR', 45000), (102, 'Marketing', 35000);
 
Select * from Employees
 
Select * from Departments
 
 -- OG Inner Join
Select Name, Salary, DepartmentName,  MinSalary
From Employees
Inner Join Departments 
on Salary > MinSalary



-- Top 3 Purc_Amt
-- Clue: Read Docs
USE [training];

SELECT *
FROM orders 
Order by purch_amt desc
    OFFSET 0 ROWS  
    FETCH NEXT 3 ROWS ONLY;

-- Date Formatting
-- It can be done using FORMAT() function.
-- Select the dates from orders tabls using FORMAT() to display in "25 Apr 2019" Format

SELECT *, FORMAT(ord_date, 'dd MMM yyyy')
FROM orders 
Order by purch_amt desc
    OFFSET 0 ROWS  
    FETCH NEXT 3 ROWS ONLY;

-- Declare a variable to fetch the records dynamically
-- Syntax for Declaring SQL variable. DECLARE @variable_name <Data type> = Value


DECLARE @n INT = 1;
SELECT *
FROM orders 
Order by purch_amt desc
    OFFSET 0 ROWS  
    FETCH NEXT @n ROWS ONLY;


-- Set theory
-- Union
-- Intersect
-- Except

Create Database setoperations;
use setoperations
 
 
CREATE TABLE Employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Department VARCHAR(50)
);
 
INSERT INTO Employees (EmployeeID, Name, Department) VALUES
(1, 'Alice', 'Engineering'),
(2, 'Bob', 'Marketing'),
(3, 'Charlie', 'Engineering'),
(4, 'Dana', 'HR');
 
 
CREATE TABLE Applicants (
    ApplicantID INT,
    Name VARCHAR(50),
    AppliedFor VARCHAR(50)
);
 
INSERT INTO Applicants (ApplicantID, Name, AppliedFor) VALUES
(5, 'George', 'Engineering'),
(6, 'Helen', 'Marketing'),
(7, 'Ian', 'Marketing'),
(3, 'Charlie', 'Sales');
 
Select * from Employees;
Select * from Applicants;

CREATE DATABASE set_theory
USE set_theory;

CREATE TABLE Products (
    ProductID INT,
    ProductName VARCHAR(50),
    Category VARCHAR(50),
    InStock CHAR(3)
);


INSERT INTO Products (ProductID, ProductName, Category, InStock) VALUES
(1, 'Laptop', 'Electronics', 'Yes'),
(2, 'Smartphone', 'Electronics', 'No'),
(3, 'Coffee Maker', 'Appliances', 'Yes'),
(4, 'Blender', 'Appliances', 'Yes'),
(5, 'T-shirt', 'Apparel', 'No');

CREATE TABLE Orders (
    OrderID INT,
    ProductID INT,
    CustomerName VARCHAR(50),
    Quantity INT
);
 
INSERT INTO Orders (OrderID, ProductID, CustomerName, Quantity) VALUES
(100, 1, 'Alice', 1),
(101, 3, 'Bob', 2),
(102, 2, 'Charlie', 1),
(103, 4, 'Dana', 1),
(104, 3, 'Alice', 1);

--Task 1
--List all the distinct products that are either in stock or have Been ordered

--Step 1: Selecting all ProductID from Orders
SELECT [ProductID] FROM [Orders]


--Step 2: Selecting all ProductId from Porducts where Instock = "Yes"
SELECT [ProductID] FROM [Products] WHERE [InStock] = 'Yes'

--Step 3: Unioning the Both result sets to get all the ProductIds that are either in Stock or have been ordered
SELECT [ProductID] FROM [Orders]
UNION
SELECT [ProductID] FROM [Products] WHERE [InStock] = 'Yes'


SELECT *
FROM [Products]
WHERE [ProductID] IN (
					SELECT [ProductID] FROM [Orders]
					UNION
					SELECT [ProductID] FROM [Products] WHERE [InStock] = 'Yes'
)

--Task 2
-- Identify the products that are both in stock and Orders table

--Step 1: Selecting all ProductID from Orders
SELECT [ProductID] FROM [Orders]


--Step 2: Selecting all ProductId from Porducts where Instock = "Yes"
SELECT [ProductID] FROM [Products] WHERE [InStock] = 'Yes'

--Step 3: Intersecting the Both result sets to get all the ProductIds that are both inStock and have been ordered
SELECT [ProductID] FROM [Orders]
INTERSECT
SELECT [ProductID] FROM [Products] WHERE [InStock] = 'Yes'

--Step 4: Selecting all the product details from product table where product ID is equivalent to the above query's productID
SELECT *
FROM [Products]
WHERE [ProductID] IN (
			SELECT [ProductID] FROM [Orders]
			INTERSECT
			SELECT [ProductID] FROM [Products] WHERE [InStock] = 'Yes'
)

-- Find the stock that are in stock but never been ordered.
--Step 1: Selecting all ProductID from Orders
SELECT [ProductID] FROM [Orders]


--Step 2: Selecting all ProductId from Porducts where Instock = "Yes"
SELECT [ProductID] FROM [Products] WHERE [InStock] = 'Yes'

--Step 3: Differencing the Both result sets to get all the ProductIds that are both inStock and have been ordered
SELECT [ProductID] FROM [Orders]
EXCEPT
SELECT [ProductID] FROM [Products] WHERE [InStock] = 'Yes'

--Step 4: Selecting all the product details from product table where product ID is equivalent to the above query's productID
SELECT *
FROM [Products]
WHERE [ProductID] IN (
			SELECT [ProductID] FROM [Orders]
			EXCEPT
			SELECT [ProductID] FROM [Products] WHERE [InStock] = 'Yes'
)