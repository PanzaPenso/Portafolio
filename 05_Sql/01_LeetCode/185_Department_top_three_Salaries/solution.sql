-- Write your PostgreSQL query statement below

WITH baselines AS (
SELECT d.name as department,
    e.name as employee,
    e.salary as salary,
    DENSE_RANK() OVER (partition by d.name order by e.salary desc) as rank
FROM employee e
INNER JOIN department d on e.departmentID = d.id
)
SELECT department,
    employee,
    salary
FROM baselines
where rank <= 3

