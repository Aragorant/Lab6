import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
    )

    cursor = connection.cursor()
    cursor.execute("DROP DATABASE IF EXISTS university")
    cursor.close()

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE university")
    cursor.close()

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='university'
    )

    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE Students (
            `Student_id` INT AUTO_INCREMENT PRIMARY KEY,
            `Student_surname` VARCHAR(255),
            `Student_name` VARCHAR(255),
            `Student_lastname` VARCHAR(255),
            `Student_address` VARCHAR(255),
            `Student_phone` VARCHAR(15),
            `Course` INT CHECK (Course >= 1 AND Course <= 4),
            `Faculty` ENUM('аграрного менеджменту', 'економіки', 'інформаційних технологій'),
            `Student_group` VARCHAR(10),
            `isHead` BOOLEAN
        )
    """)

    cursor.execute("""
        CREATE TABLE Subjects (
            `Subject_id` INT AUTO_INCREMENT PRIMARY KEY,
            `Title` VARCHAR(255),
            `Hours_per_semester` INT,
            `Number_of_semesters` INT
        )
    """)

    cursor.execute("""
        CREATE TABLE Passing_exams (
            `Passing_id` INT AUTO_INCREMENT PRIMARY KEY,
            `Date_of_passing` DATE,
            `Student_id` INT,
            `Subject_id` INT,
            `Score` INT CHECK (Score >= 2 AND Score <= 5),
            FOREIGN KEY (`Student_id`) REFERENCES Students (`Student_id`),
            FOREIGN KEY (`Subject_id`) REFERENCES Subjects (`Subject_id`)
        )
    """)

    students_data = [
        (1, 'Сидоренко', 'Іван', 'Петрович', 'вул. Героїв України, 123', '1234567890', 1, 'аграрного менеджменту', 'Група1', 1),
        (2, 'Петренко', 'Марія', 'Олександрівна', 'вул. Шевченка, 45', '1234567891', 2, 'економіки', 'Група2', 0),
        (3, 'Іванов', 'Олег', 'Васильович', 'вул. Пушкіна, 67', '1234567892', 3, 'інформаційних технологій', 'Група3', 0),
        (4, 'Павленко', 'Наталія', 'Ігорівна', 'вул. Гагаріна, 34', '1234567893', 1, 'аграрного менеджменту', 'Група1', 0),
        (5, 'Григоров', 'Володимир', 'Андрійович', 'вул. Лесі Українки, 56', '1234567894', 2, 'економіки', 'Група2', 0),
        (6, 'Сергієнко', 'Тетяна', 'Михайлівна', 'вул. Лермонтова, 78', '1234567895', 3, 'інформаційних технологій', 'Група3', 0),
        (7, 'Мельник', 'Андрій', 'Віталійович', 'вул. Шкільна, 12', '1234567896', 1, 'аграрного менеджменту', 'Група1', 0),
        (8, 'Коваленко', 'Ольга', 'Володимирівна', 'вул. Петра Порошенка, 23', '1234567897', 2, 'економіки', 'Група2', 0),
        (9, 'Біленька', 'Юлія', 'Вікторівна', 'вул. Січових Стрільців, 8', '1234567898', 3, 'інформаційних технологій', 'Група3', 0),
        (10, 'Козаченко', 'Дмитро', 'Сергійович', 'вул. Шевченка, 34', '1234567899', 1, 'аграрного менеджменту', 'Група1', 0),
        (11, 'Захаренко', 'Оксана', 'Андріївна', 'вул. Першотравнева, 56', '1234567800', 2, 'економіки', 'Група2', 0)
    ]

    insert_students_query = """
        INSERT INTO Students (Student_id, Student_surname, Student_name, Student_lastname, Student_address, Student_phone, Course, Faculty, Student_group, isHead)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(insert_students_query, students_data)

    subjects_data = [
        (1, 'Математика', 60, 2),
        (2, 'Історія', 45, 3),
        (3, 'Фізика', 30, 2)
    ]

    insert_subjects_query = """
        INSERT INTO Subjects (Subject_id, Title, Hours_per_semester, Number_of_semesters)
        VALUES (%s, %s, %s, %s)
    """

    cursor.executemany(insert_subjects_query, subjects_data)

    insert_passing_exams_query = """
    INSERT INTO Passing_exams 
        (Date_of_passing, Student_id, Subject_id, Score) 
    VALUES (%s, %s, %s, %s)
    """

    passing_exams_data = [
        ('2023-01-15', 1, 1, 5),
        ('2023-02-20', 2, 2, 4),
        ('2023-03-25', 3, 3, 3),
        ('2023-04-10', 4, 1, 5),
        ('2023-05-18', 5, 2, 4),
        ('2023-06-30', 6, 3, 3),
        ('2023-01-15', 7, 1, 5),
        ('2023-02-20', 8, 2, 4),
        ('2023-03-25', 9, 3, 3),
        ('2023-04-10', 10, 1, 5),
        ('2023-05-18', 1, 2, 4),
        ('2023-06-30', 2, 3, 3),
        ('2023-01-15', 3, 1, 5),
        ('2023-02-20', 4, 2, 4),
        ('2023-03-25', 5, 3, 3),
        ('2023-04-10', 6, 1, 5),
        ('2023-05-18', 7, 2, 4),
        ('2023-06-30', 8, 3, 3),
        ('2023-01-15', 9, 1, 5),
        ('2023-02-20', 10, 2, 4)
    ]

    cursor.executemany(insert_passing_exams_query, passing_exams_data)

    connection.commit()
    print("База даних, та таблиці в ній успішно створені. Таблиці успішно наповнені даними")

except mysql.connector.Error as err:
    print("Помилка MySQL: {}".format(err))

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
