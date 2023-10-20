INSERT INTO employees
VALUES(1 ,"Badr Edin","badr.edin13@gmail.com","Finance", "1990-08-13", 34500.13,FALSE),
	  (2 ,"Abdel Hasset","abdel.hasset23@gmail.com","Product Mangement", "1993-06-23", 44500.13,TRUE);

UPDATE employees
SET
	salary = 75000
WHERE
	employee_id = 2;

DELETE FROM employees WHERE employee_id=1;