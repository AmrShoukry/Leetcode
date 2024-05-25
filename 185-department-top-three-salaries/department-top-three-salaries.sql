# Write your MySQL query statement below
SELECT dept_name AS Department, emp_name AS Employee, salary AS Salary  FROM (
SELECT
Employee.name AS emp_name,
Department.name AS dept_name,
Employee.salary,
DENSE_RANK() OVER (PARTITION BY Department.name ORDER BY Employee.salary DESC) AS ranks
FROM Employee INNER JOIN Department ON Employee.departmentId = Department.id
) AS rank_table
WHERE ranks < 4