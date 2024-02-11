SELECT Students.group_id, AVG(Grades.grade) AS avg_grade
FROM Grades
JOIN Students ON Grades.student_id = Students.student_id
WHERE Grades.subject_id = 3
GROUP BY Students.group_id;