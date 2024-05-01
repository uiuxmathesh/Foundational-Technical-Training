-- task 7
-- write a query to  find all the orders attributed to newyork salesman

-- method 1
SELECT a.*  
FROM orders as a INNER JOIN salesman AS b
ON a.salesman_id = b.salesman_id
WHERE b.city IN ('Paris')


-- method 2
SELECT *
FROM orders 
WHERE salesman_id IN (
	SELECT salesman_id
	FROM salesman
	WHERE city='Paris'
);



-- Creating customer database
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR(255),
    city VARCHAR(255),
    grade INT NULL,
    salesman_id INT
);

-- Inserting data into customer
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3001, 'Brad Guzan', 'London', NULL, 5005),
(3004, 'Fabian Johns', 'Paris', 300, 5006),
(3007, 'Brad Davis', 'New York', 200, 5001),
(3009, 'Geoff Camero', 'Berlin', 100, 5003),
(3008, 'Julian Green', 'London', 300, 5002),
(3003, 'Jozy Altidor', 'Moscow', 200, 5007);


 
-- task 8 
-- Write a query to find the name and id of all salesmen who had more than one customer

SELECT salesman_id, name
FROM salesman
WHERE salesman_id IN(
	SELECT salesman_id
	FROM customer
	GROUP BY salesman_id
	HAVING COUNT(customer_id) > 1
)



 
SELECT * 
FROM orders 
where purch_amt > All(
			SELECT purch_amt
			FROM orders
			where customer_id = 3005);

SELECT * 
FROM orders
WHERE purch_amt > (
				SELECT MAX(purch_amt)
				FROM orders
				WHERE customer_id = 3005);

-- Task 9
-- Write a query to display only those customers whose grade or greater than every customer in newyork

-- Step 1:
--selecting customers from new york

SELECT *
FROM customer
WHERE city = 'New York'

--Step 2: To getting all the customers whose grade are greater than those of the above query
--Method 1: Using MAX
SELECT *
FROM customer
WHERE grade > (
		SELECT MAX(grade)
		FROM customer
		WHERE city = 'New York'
)

--Method 2: Using ALL
SELECT *
FROM customer
WHERE grade > ALL(
		SELECT grade
		FROM customer
		WHERE city = 'New York'
)

-- Task 10
-- Write a query to find all orders with an amount smaller than any amount for a customer in London

-- Step 1: Selecting customers from London
SELECT * 
FROM customer
WHERE city = 'London'

-- Step 2: Selecting orders with amount smaller than any particular order (HARD CODE)
SELECT *
FROM orders
WHERE purch_amt < 120

-- Step 3: Selecting orders with amount smaller than minimum order of any random customer
SELECT *
FROM orders
WHERE purch_amt < (
	SELECT MIN(purch_amt)
	FROM orders
	WHERE customer_id = 3001
)

--Step 3: Selecting customer_id of the customer whose from London City.
SELECT *
FROM orders
WHERE purch_amt < (
					SELECT MIN(purch_amt)
					FROM orders
					WHERE customer_id IN (
											SELECT customer_id 
											FROM customer
											WHERE city = 'London'
	)
)


CREATE TABLE [Professor] (
  [professor_id] Varchar(255),
  [professor_name] Varchar(255),
  [department] Varchar(255),
  PRIMARY KEY ([professor_id])
);
 
 
CREATE TABLE [Student] (
  [student_id] Varchar(255),
  [student_name] Varchar(255),
  PRIMARY KEY ([student_id])
);
 
CREATE TABLE [Course] (
  [course_id] Varchar(255),
  [course_name] Varchar(255),
  [professor_id] Varchar(255),
  PRIMARY KEY ([course_id]),
  Foreign Key ([professor_id]) References Professor([professor_id])
);
 
 
CREATE TABLE [Enrollment] (
  [enroll_id] Varchar(255) ,
  [course_id] Varchar(255),
  [student_id] Varchar(255) ,
  PRIMARY KEY ([enroll_id]),
  Foreign Key ([course_id]) References Course([course_id]),
  Foreign Key ([student_id]) References Student([student_id])
);
 
 
INSERT INTO Professor (professor_id, professor_name, department)
VALUES ('P001', 'Dr. Brown', 'Mathematics'),
       ('P002', 'Dr. Smith', 'Physics');
 
 
Select * from Professor;
 
INSERT INTO Student (student_id, student_name)
VALUES ('S001', 'Alice'),
       ('S002', 'Bob'),
       ('S003', 'Charlie');
 
Select * from Professor;
 
Select * from Course;
 
INSERT INTO Course (course_id, course_name, professor_id)
VALUES ('C001', 'Math 101', 'P001'),
       ('C002', 'Physics 101', 'P002');
 
 
INSERT INTO Enrollment (enroll_id, course_id, student_id)
VALUES ('E001', 'C001', 'S001'),
       ('E002', 'C002', 'S002'),
       ('E003', 'C002', 'S001'),
       ('E004', 'C001', 'S003');
 
Select * from Enrollment;



CREATE TABLE EmployeeData (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary INT,
    StartDate DATE
);

INSERT INTO EmployeeData (EmployeeID, FirstName, LastName, Salary, StartDate) VALUES
(1, 'John', 'Doe', 70000, '2020-05-01'),
(2, 'Jane', 'Smith', 85000, '2018-08-15'),
(3, 'Emily', 'Jones', 94000, '2019-12-30'),
(4, 'Chris', 'Brown', 62000, '2021-03-22');


--Task 1
-- Sort the employees based om the length of their first namw

SELECT FirstName
FROM EmployeeData
ORDER BY len(FirstName) DESC

--Task 2
--List the Initials of all the employees
SELECT CONCAT( LEFT(FirstName,1), LEFT(LastName,1)) AS Employee_Initials
FROM EmployeeData


-- Task 3
-- Extract and Display the first three letters of each employee's last name and Display it  in uppercase

SELECT UPPER(SUBSTRING(LastName, 1, 3)) AS Short_name
FROM EmployeeData

-- Task 4
-- Find out how many years an employee has been in the company

SELECT DATEDIFF(YEAR,StartDate, GETDATE()) AS no_of_days_since_appointment
FROM EmployeeData






