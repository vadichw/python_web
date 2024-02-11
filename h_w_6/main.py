import sqlite3
from faker import Faker
import random


fake = Faker()

conn = sqlite3.connect('h_w_base')
cursor = conn.cursor()


groups = [(i, fake.word()) for i in range(1, 4)]
cursor.executemany("INSERT INTO Groups (group_id, group_name) VALUES (?, ?)", groups)


teachers = [(i, fake.name()) for i in range(1, 6)]
cursor.executemany("INSERT INTO Teachers (teacher_id, name) VALUES (?, ?)", teachers)


subjects = [(i, fake.word(), random.randint(1, 5)) for i in range(1, 9)]
cursor.executemany("INSERT INTO Subjects (subject_id, subject_name, teacher_id) VALUES (?, ?, ?)", subjects)


students = [(i, fake.name(), random.randint(1, 3)) for i in range(1, 51)]
cursor.executemany("INSERT INTO Students (student_id, name, group_id) VALUES (?, ?, ?)", students)

grades = []
for student_id in range(1, 51):
    for subject_id in range(1, 9):
        grades.extend([(None, student_id, subject_id, random.randint(60, 100), fake.date_between(start_date='-1y', end_date='today'))])

cursor.executemany("INSERT INTO Grades (grade_id, student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?, ?)", grades)

conn.commit()
conn.close()
