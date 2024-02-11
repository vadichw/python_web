SELECT DISTINCT Subjects.subject_name
FROM Subjects
JOIN Grades ON Subjects.subject_id = Grades.subject_id
JOIN Teachers ON Subjects.teacher_id = Teachers.teacher_id
WHERE Grades.student_id = 1
  AND Teachers.teacher_id = 1
 