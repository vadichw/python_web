SELECT DISTINCT Subjects.subject_name
FROM Subjects
JOIN Grades ON Subjects.subject_id = Grades.subject_id
WHERE Grades.student_id = 12
