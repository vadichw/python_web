SELECT AVG(Grades.grade) AS avg_grade
FROM Grades
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
JOIN Teachers ON Subjects.teacher_id = Teachers.teacher_id
WHERE Teachers.teacher_id = 3