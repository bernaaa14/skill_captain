CREATE TABLE Employees (
  ID INT,
  Name VARCHAR(255),
  Department VARCHAR(255)
);

INSERT INTO Employees
VALUES
    (1, "Myla Melendez", "Information Technology"),
    (2, "Nikolas McKee", "Information Technology"),
    (3, "Kori Travis", "Information Technology"),
    (4, "Willie McPherson", "Marketing"),
    (5, "Emmaline Walter", "Marketing"),
    (6, "Lochlan Hendricks", "Human Resources"),
    (7, "Dani Mullen", "Human Resources"),
    (8, "Shepard Phelps", "Finance"),
    (9, "Laney Flynn", "Finance"),
    (10, "Kannon Ochoa", "Sales");

SELECT COUNT(ID) AS TotalOfEmployees, Department
FROM Employees
GROUP BY Department
HAVING COUNT(ID) > 2
ORDER BY COUNT(ID) DESC;