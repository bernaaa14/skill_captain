USE EmployeesDb;

CREATE TABLE Employee (
  EmployeeID INT,
  EmployeeName VARCHAR(255),
  DepartmentID INT
);

CREATE TABLE Department (
  DepartmentID INT,
  DepartmentName VARCHAR(255)
);

--List of all possible combinations of employees and departments 

SELECT Employee.EmployeeName, Department.DepartmentName
FROM Employee
CROSS JOIN Department;

--List all of employees who belong to at least one department
SELECT Employee.EmployeeName
FROM Employee
INNER JOIN Department ON Employee.DepartmentID = Department.DepartmentID;

/*List all of employees and their department details
ncluding those employees who do not belong to any department 
or departments which do not have any employees.*/
SELECT Employee.EmployeeName, Department.DepartmentName
FROM Employee
LEFT JOIN Department ON Employee.DepartmentID = Department.DepartmentID
UNION
SELECT Employee.EmployeeName, Department.DepartmentName
FROM Department
LEFT JOIN Employee ON Department.DepartmentID = Employee.DepartmentID;

--List of all empyees, along with their department details
SELECT Employee.EmployeeName, Department.DepartmentName
FROM Employee
LEFT JOIN Department ON Employee.DepartmentID = Department.DepartmentID;

--List all departments , along with the employee details if they have one employee belonging to the
SELECT Department.DepartmentName, Employee.EmployeeName
FROM Department
RIGHT JOIN Employee ON Department.DepartmentID = Employee.DepartmentID;