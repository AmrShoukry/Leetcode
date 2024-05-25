# Write your MySQL query statement below
SELECT IFNULL( (SELECT DISTINCT salary FROM Employee ORDER By salary DESC LIMIT 1, 1) , NULL) AS SecondHighestSalary