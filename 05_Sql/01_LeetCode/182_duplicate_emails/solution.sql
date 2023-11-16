# Write your MySQL query statement below

SELECT Email
FROM
(
SELECT 
        email as Email,
        count(email)
FROM Person
Group by email
having count(email) > 1
) as result
