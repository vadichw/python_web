SELECT Students.student_id, Students.name, Grades.grade
FROM Students
JOIN Grades ON Students.student_id = Grades.student_id
WHERE Students.group_id = 3
  AND Grades.subject_id = 1
 
 