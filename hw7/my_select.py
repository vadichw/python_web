from sqlalchemy import func, create_engine, and_, distinct
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade, Base

from connect_db import session


# def select_1(session):
#     top_students = (
#         session.query(Grade.student_id, func.avg(Grade.grade).label('avg_grade'))
#         .group_by(Grade.student_id)
#         .order_by(func.avg(Grade.grade).desc())
#         .limit(5)
#         .all()
#     )
#     return top_students
#
#
# result1 = select_1(session)
# for student_id, avg_grade in result1:
#     print(f"Student ID: {student_id}, Average Grade: {avg_grade}")

# def select_2(session, subject_id):
#     top_student = (
#         session.query(Grade.student_id, func.avg(Grade.grade).label('avg_grade'))
#         .filter(Grade.subject_id == subject_id)
#         .group_by(Grade.student_id)
#         .order_by(func.avg(Grade.grade).desc())
#         .limit(1)
#         .first()
#     )
#     return top_student
#
#
# result2 = select_2(session, subject_id=3)
# if result2:
#     student_id, avg_grade = result2
#     print(f"Top student ID: {student_id}, Average Grade: {avg_grade}")
# else:
#     print("No data found for the specified subject ID.")

# def select_3(session, subject_id):
#     avg_grades_by_group = (
#         session.query(Student.group_id, func.avg(Grade.grade).label('avg_grade'))
#         .join(Grade, Grade.student_id == Student.id)
#         .filter(Grade.subject_id == subject_id)
#         .group_by(Student.group_id)
#         .all()
#     )
#     return avg_grades_by_group
#
#
# result3 = select_3(session, subject_id=3)
# if result3:
#     for group_id, avg_grade in result3:
#         if group_id is None:
#             print(f"Group ID: {group_id}, Average Grade: {avg_grade}")
# else:
#     print("No data found for the specified subject ID.")

# def select_4(session):
#     result4 = session.query(func.avg(Grade.grade).label('avg_grade')).scalar()
#     return result4
#
# print(select_4(session))


# def select_5(session, teacher_name):
#     query_result = session.query(Subject.name). \
#         join(Subject.teacher). \
#         filter(Teacher.name == teacher_name). \
#         all()
#     return [row[0] for row in query_result]
#
#
# teacher_name = 'Carla Jenkins'
# distinct_subjects = select_5(session, teacher_name)
# for subject in distinct_subjects:
#     print(subject)


# def select_6(session, group_id):
#     students_in_group = session.query(Student).filter(Student.group_id == group_id).all()
#     return students_in_group
#
# group_id = 2
# students = select_6(session, group_id)
# for student in students:
#     print(f"Student Name: {student.name}")


# def select_7(session, group_id, subject_id):
#     grades_query = session.query(Grade).\
#         join(Student, Grade.student_id == Student.id).\
#         join(Subject, Grade.subject_id == Subject.id).\
#         filter(Student.group_id == group_id).\
#         filter(Subject.id == subject_id).\
#         all()
#
#     return grades_query
#
# group_id = 1
# subject_id = 1
# grades = select_7(session, group_id, subject_id)
#
# for grade in grades:
#     print(f"Student ID: {grade.student_id}, Grade: {grade.grade}")


# def select_8(session, teacher_id):
#     avg_grade_subquery = session.query(func.avg(Grade.grade)).\
#         join(Subject, Grade.subject_id == Subject.id).\
#         filter(Subject.teacher_id == teacher_id).scalar_subquery()
#
#     average_grade = session.query(func.avg(avg_grade_subquery)).scalar()
#     print(f"Average Grade for Teacher with ID {teacher_id}: {average_grade}")
#     return average_grade
#
# teacher_id = 1
# average_grade = select_8(session, teacher_id)


# def select_9(session, student_id):
#     query = session.query(Subject.name) \
#         .join(Grade, Subject.id == Grade.subject_id) \
#         .filter(Grade.student_id == student_id) \
#         .distinct()
#     return query.all()
#
#
# student_id = 22
# result = select_9(session, student_id)
# for subject_name in result:
#     print(subject_name)


# def select_10(session, student_id, teacher_id):
#     query = session.query(Subject.name) \
#         .join(Grade, Subject.id == Grade.subject_id) \
#         .join(Teacher, Subject.teacher_id == Teacher.id) \
#         .filter(Grade.student_id == student_id) \
#         .filter(Teacher.id == teacher_id)
#     return query.all()
#
#
# student_id = 1
# teacher_id = 1
# result = select_10(session, student_id, teacher_id)
#
# if result:
#     print("Courses attended by student and taught by teacher:")
#     for course in result:
#         print(course[0])
# else:
#     print("No courses found for the given student and teacher.")
