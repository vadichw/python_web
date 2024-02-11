SELECT student_id, AVG(grade) AS avg_grade
FROM Grades
WHERE subject_id = 3
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 1;