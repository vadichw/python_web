from faker import Faker
from random import randint, choice
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade

from connect_db import session

fake = Faker()

# Створення груп
groups = []
for i in range(1, 4):
    group = Group(name=f'Group {i}')
    groups.append(group)

session.add_all(groups)
session.commit()


# Створення студентів
students = []
for _ in range(50):
    group = choice(groups)
    student = Student(name=fake.name(), group=group)
    students.append(student)

session.add_all(students)
session.commit()


# Створення викладачів
teachers = []
for _ in range(5):
    teacher = Teacher(name=fake.name())
    teachers.append(teacher)

session.add_all(teachers)
session.commit()

# Створення предметів
subjects = []
for i in range(5):
    subject = Subject(name=f'Subject {i+1}', teacher=choice(teachers))
    subjects.append(subject)

session.add_all(subjects)
session.commit()

# Створення оцінок для кожного студента по кожному предмету
for student in students:
    for subject in subjects:
        score = randint(1, 100)
        date = fake.date_time_between(start_date="-1y", end_date="now")
        grade = Grade(student=student, subject=subject, grade=score, date=date)
        session.add(grade)

session.commit()
