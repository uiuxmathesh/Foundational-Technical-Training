# Foundational Technical Training 24/04/2024

# SQL and Cloud ☁️💾

## Agenda 📝

- Intro to DB
- DML
- DDL
- Joints
- Normalization

## Introduction

### Database lives in Cloud

We all know local machines cannot host a large database as it has limitation of handling high network traffic.  So, the databases back then are hosted with servers. As the modern era of technology grows, the businesses choose to host their databases in cloud infrastructures like Azure, AWS, Google Cloud. The hosting of database in cloud literally means renting out the servers for pay-as-per-use. 

### Why it beneficial to rent?

As said before renting out computing resources means paying for only what we are using.  It minimizes the huge upfront needed to be put before the cloud. Additionally there’s no need for buying software licenses, maintenance and everything is done by the service provider itself. Apart from all these Scalability is a important factor in Cloud computing.

Scaling:

- Vertical
- Horizontal

### Which OS runs on Cloud?

Mostly, Alpine Linux

Event - Based database supports rollback of operation infinite  times

### Types of Databases

- Relational Databases
- Non-Relational Databases

## Relational Databases

- PL SQL
- Postgres SQL
- MySQL
- MS SQL
- Amazon RDS

## Non-Relational Databases

- Mongo DB
- Couch DB
- Redis
- Cassandra
- Dynamo DB
- Neo4j

# Coding in SQL

## SQL Lesson 1: Filtering Columns:

We will be using a database with data about some of Pixar's classic movies for most of our exercises. This first exercise will only involve the **Movies** table, and the default query below currently shows all the properties of each movie. To continue onto the next lesson, alter the query to find the exact information we need for each task.

Task 1: Find the **`title`** of each film

```sql
SELECT Title FROM Movies;
```

Task 2: Find the **`director`** of each film

```sql
SELECT Director FROM Movies;
```

Task 3: Find the **`title`** and **`director`** of each film

```sql
SELECT Title, Director FROM movies;
```

Task 4: Find the **`title`** and **`year`** of each film

```sql
SELECT Title, Year FROM Movies;
```

Task 5: Find **`all`** the information about each film

```sql
SELECT * FROM Movies;
```

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled.png)

## **SQL Lesson 2: Queries with constraints (Pt. 1)**

Task 1: Find the movie with a row **`id`** of 6

```sql
SELECT * FROM movies WHERE id=6;
```

Task 2: Find the movies released in the **`year`**s between 2000 and 2010

```sql
SELECT * FROM movies WHERE Year BETWEEN 2000 AND 2010;
```

Task 3: Find the movies **not** released in the **`year`**s between 2000 and 2010

```sql
SELECT * FROM movies WHERE Year NOT BETWEEN 2000 AND 2010;
```

Task 4: Find the first 5 Pixar movies and their release **`year`**

```sql
SELECT * FROM movies WHERE Id In(1,2,3,4,5);
```

## **SQL Lesson 3: Queries with constraints (Pt. 2)**

| Operator | Condition | Example |
| --- | --- | --- |
| = | Case sensitive exact string comparison (notice the single equals) | col_name = "abc" |
| != or <> | Case sensitive exact string inequality comparison | col_name != "abcd" |
| LIKE | Case insensitive exact string comparison | col_name LIKE "ABC" |
| NOT LIKE | Case insensitive exact string inequality comparison | col_name NOT LIKE "ABCD" |
| % | Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE) | col_name LIKE "%AT%"(matches "AT", "ATTIC", "CAT" or even "BATS") |
| _ | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE) | col_name LIKE "AN_"(matches "AND", but not "AN") |
| IN (…) | String exists in a list | col_name IN ("A", "B", "C") |
| NOT IN (…) | String does not exist in a list | col_name NOT IN ("D", "E", "F") |

Exercise 3 — Tasks

1. Find all the Toy Story movies ✓
2. Find all the movies directed by John Lasseter
3. Find all the movies (and director) not directed by John Lasseter
4. Find all the WALL-* movies

Task 1: 

```sql
SELECT * FROM movies WHERE Title LIKE "TOY STORY%"
```

Task 2:

```sql
SELECT * FROM movies WHERE Director = "John Lasseter"
SELECT Title, Director FROM movies WHERE Director IN ("John Lasseter")
```

Task 3:

```sql
SELECT Title, Director FROM movies WHERE Director != "John Lasseter"
SELECT Title, Director FROM movies WHERE Director NOT IN ("John Lasseter")
```

Task 4:

```sql
SELECT * FROM movies WHERE Title LIKE "WALL-_"
SELECT * FROM movies WHERE Title LIKE "WALL%"
```

### ADDITIONAL INFO

Commenting in SQL

```sql
-- SELECT * FROM movies
```

### **SQL Lesson 4: Filtering and sorting Query results**

**Syntax For Selecting Distinct Entries**

SQL provides a convenient way to discard rows that have a duplicate column value by using the **`DISTINCT`** keyword.

```sql
SELECT DISTINCT column, another_column, …
FROM mytable
WHERE condition(s);
```

**Syntax For Ordering (Ascending/ Descending) Selected Entries**

SQL provides a way to sort your results by a given column in ascending or descending order using the **`ORDER BY`** clause.

```sql
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC;
```

**Syntax For Limiting Selected Entries**

The **`LIMIT`** will reduce the number of rows to return, and the optional **`OFFSET`** will specify where to begin counting the number rows from.

```sql
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

Exercise

Task 1: List all directors of Pixar movies (alphabetically), without duplicates 

```sql
SELECT DISTINCT Director 
FROM movies 
ORDER BY Director ASC;
```

Task 2: List the last four Pixar movies released (ordered from most recent to least)

```sql
SELECT * FROM movies 
ORDER BY Year DESC 
LIMIT 4;
```

Task 3: List the **first** five Pixar movies sorted alphabetically

```sql
SELECT * FROM movies 
ORDER BY Title ASC 
LIMIT 5;
```

Task 4: List the **next** five Pixar movies sorted alphabetically

```sql
SELECT * FROM movies 
ORDER BY Title ASC 
LIMIT 5 OFFSET 5;
```

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%201.png)

### **SQL Review: Simple SELECT Queries**

lattitude is horizontal

longitude is vertical

longitude towards east will increase

latitude towards north  will increase

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%202.png)

Task 1: List all the Canadian cities and their populations

```sql
SELECT City 
FROM north_american_cities
WHERE Country = "Canada"
ORDER BY Population
```

Task 2: Order all the cities in the United States by their latitude from north to south

```sql
SELECT City 
FROM north_american_cities 
WHERE Country="United States" 
ORDER BY Latitude DESC;
-- Latitude Will increase towards north.
```

Task 3: List all the cities west of Chicago, ordered from west to east

```sql
SELECT city FROM north_american_cities
WHERE Longitude < (
    SELECT Longitude 
    FROM north_american_cities 
    WHERE city = "Chicago") 
ORDER BY Longitude
;
```

Task 4: List the two largest cities in Mexico (by population)

```sql
SELECT City 
FROM north_american_cities 
WHERE country="Mexico" 
ORDER BY Population DESC 
LIMIT 2;
```

Task 5: List the third and fourth largest cities (by population) in the United States and their population

```sql
SELECT City, Population 
FROM north_american_cities 
WHERE country="United States" 
ORDER BY Population DESC
LIMIT 2 OFFSET 2;
```

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%203.png)

### Types of Anomalies in SQL

1. **Updation Anomaly**
    
    Consider a person is charged with maintaining consistent and accurate record, is asked to update a employee’s title due to promotion. If the employee’s record is stored redundantly in the  table and the person misses any of it, then there will be multiple titles assocciated with a single employee. 
    
2. **Insertion Anomaly**
    
    For example, if a system is designed to require that a customer be on file before a sale can be made to that customer, but you cannot add a customer until they have bought something, then you have an insert anomaly. It is the classic "catch-22" situation.
    
3. Deletion Anomaly
    
    For example, if a single database record contains information about a particular product along with information about a salesperson for the company and the salesperson quits, then information about the product is deleted along with salesperson information. 
    

### Types of Keys

1. Canditate Key
2. Primary Key
3. Super Key
4. Foreign Key
5. Composite Key
6. Alternate Key
7. Unique Key

🔗For a detailed Overview: 

[Types of Keys in DBMS](https://medium.com/@ismsapugodage/types-of-keys-in-dbms-8637aa558381)

## Normalization

Normalization is process of ensuring safety to our data in the database. It aims to eliminate redundant data, minimize data modification errors and simplify  the querying process.

There are 5 levels of Normal Form:

### First Normal Form (1NF)

- Rule 1: Do not use row order to convey information

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%204.png)

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%205.png)

- Rule 2: Mixing Datatype is not allowed

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%206.png)

- Rule 3: Every table should have a primary key

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%207.png)

- Rule 4: Repeating Groups are not permitted

![The data items amulets rings copper coins are getting  repeated in each row](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%208.png)

The data items amulets rings copper coins are getting  repeated in each row

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%209.png)

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2010.png)

## Second Normal Form 2NF:

- Rule 1: It must be in First Normal Form
- Rule 2: Each Non-key attribute must depend on entire primary key

![This table is not  in 2NF as the player_rating column is dependent on the  item_quantity, rather than the composite primary key {player_id, item_type} which violates 2NF](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2011.png)

This table is not  in 2NF as the player_rating column is dependent on the  item_quantity, rather than the composite primary key {player_id, item_type} which violates 2NF

![The table is then splitted into separate tables. Now each non-key attributes on each table  is  dependent  on their corresponding primary key.](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2012.png)

The table is then splitted into separate tables. Now each non-key attributes on each table  is  dependent  on their corresponding primary key.

## Third Normal Form 3NF

- Rule 1: It should be in 2NF and 3NF
- Rule 2: Every  non-key attribute on the table should depend on the key, the whole key, nothing but the key.

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2013.png)

![In this example the a non-key attribute “player_skill_level” is entirely dependent on another non-key attribute “player_rating” which violates 3NF](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2014.png)

In this example the a non-key attribute “player_skill_level” is entirely dependent on another non-key attribute “player_rating” which violates 3NF

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2015.png)

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2016.png)

## **SQL Lesson 6: Multi-table queries with JOINs**

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2017.png)

The **`INNER JOIN`** is a process that matches rows from the first table and the second table which have the same key (as defined by the **`ON`** constraint) to create a result row with the combined columns from both tables. After the tables are joined, the other clauses we learned previously are then applied.

```sql
SELECT column, another_table_column, …
FROM mytable
INNER JOIN another_table 
    ON mytable.id = another_table.id
WHERE condition(s)
ORDER BY column, … ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2018.png)

Exercise 6 — Tasks

Task 1: Find the domestic and international sales for each movie ✓

```sql
SELECT Title, Domestic_sales, International_sales 
FROM movies INNER JOIN Boxoffice 
ON movies.Id = Boxoffice.Movie_id;
```

Task 2: Show the sales numbers for each movie that did better internationally rather than domestically

```sql
SELECT * 
FROM movies INNER JOIN Boxoffice 
ON movies.Id = Boxoffice.Movie_id
WHERE Domestic_sales < International_sales;
```

Task 3: List all the movies by their ratings in descending order

```sql
SELECT * 
FROM movies INNER JOIN Boxoffice 
ON movies.Id = Boxoffice.Movie_id
ORDER BY Rating DESC;
```

If the two tables have asymmetric data, which can easily happen when data is entered in different stages, then we would have to use a **`LEFT JOIN`**, **`RIGHT JOIN`** or **`FULL JOIN`** instead to ensure that the data you need is not left out of the results.

```sql
SELECT column, another_column, …
FROM mytable
INNER/LEFT/RIGHT/FULL JOIN another_table 
    ON mytable.id = another_table.matching_id
WHERE condition(s)
ORDER BY column, … ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2019.png)

Exercise 7 — Tasks

Task 1: Find the list of all buildings that have employees

```sql
SELECT DISTINCT Building 
FROM employees;
```

Task 2: Find the list of all buildings and their capacity

```sql
SELECT * FROM Buildings;
```

Task 3: List all buildings and the distinct employee roles in each building (including empty buildings)

```sql
SELECT DISTINCT Building_Name, Role 
FROM Buildings LEFT JOIN Employees
ON Building_name = Building;
```

## **SQL Lesson 8: A short note on NULLs**

In SQL, it is always advised to eliminate `NULL` Values at all cost as it requires special attention while querying. It is a best practice to use default values according to the data-type of columns for eliminating `NULL` values. Default values can be like 0’s for Numerical values, empty string for strings and so on.

But in scenarios like where an average is to be calculated, it is not possible to use 0 as a default value. So, anyways we got to deal with null values

you can test a column for **`NULL`** values in a **`WHERE`** clause by using either the **`IS NULL`** or **`IS NOT NULL`** constraint.

```sql
SELECT column, another_column, …
FROM mytable
WHERE column IS/IS NOT NULL
AND/OR another_condition
AND/OR …;
```

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2020.png)

Exercise 8 — Tasks

Task 1: Find the name and role of all employees who have not been assigned to a building ✓

```sql
SELECT Role 
FROM Employees
WHERE Building IS NULL;
```

Task 2. Find the names of the buildings that hold no employees

```sql
SELECT Building_name 
FROM Buildings LEFT JOIN Employees
ON Building_name = Building
WHERE Name IS NULL;
```

## **SQL Lesson 9: Queries with expressions**

In addition to querying raw column values we can also perform computation on Queries as well. This makes use of mathematical expression, some string functions and basic arithmetic operations.

For example,

```sql
SELECT particle_speed / 2.0 AS half_particle_speed
FROM physics_data
WHERE ABS(particle_position) * 10.0 > 500;
```

### Aliasing

SQL supports aliasing of the above said expressions as well as column names and table names for better accessibility. The aliasing can be done using `AS` keyword

```sql
SELECT col_expression AS expr_description, …
FROM mytable;
```

In addition to expressions, regular columns and even tables can also have aliases to make them easier to reference in the output and as a part of simplifying more complex queries.

Example query with both column and table name aliases

```sql
SELECT column AS better_column_name, …
FROM a_long_widgets_table_name AS mywidgets INNER JOIN widget_sales
ON mywidgets.id = widget_sales.widget_id;
```

![Untitled](Foundational%20Technical%20Training%2024%2004%202024%204ef4fddd7c5a452689d50d4846da7ff7/Untitled%2021.png)

Exercise 9:

Task 1: List all movies and their combined sales in **millions** of dollars

```sql
SELECT Title,
(Domestic_sales + International_sales)/1000000 AS Combined_sales 
FROM movies LEFT JOIN Boxoffice
ON id = movie_id;
```

Task 2: List all movies and their ratings **in percent**

```sql
SELECT Title, Rating*10 As Rating_Percentage 
FROM movies LEFT JOIN Boxoffice
ON id = movie_id;
```

Task 3: List all movies that were released on even number years

```sql
SELECT * FROM movies
WHERE Year%2 = 0;
```