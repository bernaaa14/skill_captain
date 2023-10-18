CREATE TABLE employees(
employee_id VARCHAR(50),
employee_name VARCHAR(50),
employee_email VARCHAR (50),
department VARCHAR (50),
birth_date DATE,
salary DECIMAL(10, 2),
is_active BOOLEAN);

INSERT INTO employees
VALUES 
   (1011, "Aissam Rezzouqi", "aissam.rezzouqi25@gmail.com", "Marketing", "1998-08-25", 45600.56, TRUE),
   (1012, "Berna Alhambra", "berna.alhambra14@gmail.com", "Information Technology", "2004-04-14", 45800.56, FALSE);

    
