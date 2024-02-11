

-- Таблиця студентів
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    group_id INTEGER
);

-- Таблиця груп
CREATE TABLE IF NOT EXISTS Groups (
    group_id INTEGER PRIMARY KEY,
    group_name TEXT
);

-- Таблиця викладачів
CREATE TABLE IF NOT EXISTS Teachers (
    teacher_id INTEGER PRIMARY KEY,
    name TEXT
);

-- Таблиця предметів із зазначенням викладача, який читає предмет
CREATE TABLE IF NOT EXISTS Subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

-- Таблиця, де у кожного студента є оцінки з предметів із зазначенням, коли оцінку отримано
CREATE TABLE IF NOT EXISTS Grades (
    grade_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date_received DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);
