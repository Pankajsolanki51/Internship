--2a
--1. Get list of tables 
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public'
AND table_type='BASE TABLE';

--2. Get list of columns and data types
SELECT column_name, data_type
FROM information_schema.columns

--3. Get list of Schema, tables, columns.
SELECT 
    table_schema, 
    table_name, 
    column_name
FROM 
    information_schema.columns
ORDER BY 
    table_schema, 
    table_name, 
    ordinal_position;

--4. Get list of constraints (Primary Key, Foreign Key, Check Constraints).
SELECT 
    tc.constraint_name, 
    tc.constraint_type, 
    tc.table_name, 
    kcu.column_name, 
    cc.check_clause
FROM 
    information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu 
        ON tc.constraint_name = kcu.constraint_name 
        AND tc.table_schema = kcu.table_schema
    LEFT JOIN information_schema.check_constraints cc 
        ON tc.constraint_name = cc.constraint_name 
        AND tc.table_schema = cc.constraint_schema
WHERE 
    tc.constraint_type IN ('PRIMARY KEY', 'FOREIGN KEY', 'CHECK')
ORDER BY 
    tc.constraint_type, 
    tc.table_name, 
    kcu.ordinal_position;
	
--5. What is difference between Primary Key, Foreign Key and Unique Contraints.	
	A primary key is a column or group of columns in a table that uniquely identifies each row in the table. Primary keys are always unique and cannot contain null values.A table can have only one primary key
    
	A foreign key is a column or group of columns in a table that refers to the primary key of another table. It is used to establish a relationship between two tables and enforce referential integrity between them
	
	A unique constraint is a rule that ensures that the values in a column or group of columns in a table are unique
	
--6. Get list of indexes for each tables.
SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;

--7. Understand table structures along with relationships, for each table look at data and see if they are in 1 Normal form,
--2nd Normal Form or 3rd Normal form. Format should be
--<Table> <Name> <Normal Form Reason>
actor - First normal form (1NF), Second normal form (2NF), and Third normal form (3NF).
1NF: Each column contains atomic values.
2NF: There is a primary key (actor_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


store - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (store_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


payment - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (payment_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


film - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (film_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


payment_p2007_02 - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (payment_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


payment_p2007_03 - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (payment_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


payment_p2007_04 - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (payment_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


payment_p2007_05 - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (payment_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


payment_p2007_06 - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (payment_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


payment_p2007_01 - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (payment_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.

address - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (address_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


category - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (category_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


city - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (city_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


country - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (country_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


customer - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (customer_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


film_actor - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a composite primary key (actor_id, film_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


film_category - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a composite primary key (film_id, category_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


inventory - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (inventory_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


language - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (language_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


rental - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (rental_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


staff - 1NF, 2NF, and 3NF.
1NF: Each column contains atomic values.
2NF: There is a primary key (staff_id) and all non-key columns depend on the primary key.
3NF: There are no transitive dependencies.


--8. Create Database diagram for tables in shakila using https://dbdiagram.io/home/ and send the screenshots.
--Attached in mail sended (Screenshots)


--9.Calculate size of each table and total database size.
SELECT
  pg_class.relname AS table,
  pg_size_pretty(pg_total_relation_size(pg_class.oid)) AS size
FROM pg_class
LEFT JOIN pg_namespace ON pg_namespace.oid = pg_class.relnamespace
WHERE pg_namespace.nspname = 'public'
AND pg_class.relkind = 'r'
ORDER BY pg_total_relation_size(pg_class.oid) DESC;
SELECT pg_size_pretty(pg_database_size(current_database())) AS size;

--10.Get list of users and related permissions.
SELECT
    r.rolname AS user_name,
    string_agg(t.table_name || '.' || c.column_name, ', ') AS permissions
FROM
    pg_roles r
LEFT JOIN
    information_schema.role_table_grants rtg ON r.rolname = rtg.grantee
LEFT JOIN
    information_schema.columns c ON rtg.table_name = c.table_name
        AND rtg.table_schema = c.table_schema
LEFT JOIN
    information_schema.tables t ON c.table_name = t.table_name
        AND c.table_schema = t.table_schema
WHERE
    r.rolcanlogin = 'true' -- only get roles that can login
GROUP BY
    r.rolname;
	

