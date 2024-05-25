# Write your MySQL query statement below
SELECT Employees2.employee_id,
        Employees2.name,
        COUNT(Employees1.employee_id) AS reports_count,
        ROUND(AVG(Employees1.age)) AS average_age
        
FROM Employees AS Employees1

INNER JOIN Employees AS Employees2
    ON Employees1.reports_to = Employees2.employee_id
    
GROUP BY Employees1.reports_to
ORDER BY Employees2.employee_id ASC
