SELECT em.name as Employee
FROM Employee em
INNER JOIN Employee mg on em.managerId = mg.id
WHERE em.salary > mg.salary