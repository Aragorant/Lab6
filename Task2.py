import mysql.connector
from tabulate import tabulate

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='university',
    )

    cursor = connection.cursor()

    def print_query_results(query, query_description, param):
        cursor.execute(query, param)
        results = cursor.fetchall()

        if results:
            print(f"{query_description}:")
            print(tabulate(results, headers=[i[0] for i in cursor.description]))
            print("\n")


    subject_name = ("Фізика",)
    queries = [
        ("DESCRIBE Students", "Структура таблиці Students"),
        ("SELECT * FROM Students", "Дані з таблиці Students"),
        ("DESCRIBE Subjects", "Структура таблиці Subjects"),
        ("SELECT * FROM Subjects", "Дані з таблиці Subjects"),
        ("DESCRIBE Passing_exams", "Структура таблиці Passing_exams"),
        ("SELECT * FROM Passing_exams", "Дані з таблиці Passing_exams"),
        ("SELECT * FROM Students WHERE isHead = 1 ORDER BY Student_surname", "Студенти-старости"),
        ("SELECT Students.Student_id, Student_surname, Student_name, Student_lastname, AVG(Score) AS Average_Score "
         "FROM Students JOIN Passing_exams ON Students.Student_id = Passing_exams.Student_id "
         "GROUP BY Students.Student_id",
         "Середній бал для кожного студента"),
        ("SELECT Title, SUM(Hours_per_semester * Number_of_semesters) AS Total_Hours FROM Subjects GROUP BY Title",
         "Загальна кількість годин для кожного предмета"),
        ("SELECT Students.Student_id, Student_surname, Student_name, Student_lastname, Score FROM Students "
         "JOIN Passing_exams ON Students.Student_id = Passing_exams.Student_id "
         "JOIN Subjects ON Passing_exams.Subject_id = Subjects.Subject_id WHERE Title = %s",
         f"Успішність студентів по предмету '{subject_name[0]}'"),
        ("SELECT Faculty, COUNT(*) AS Student_Count FROM Students GROUP BY Faculty",
         "Кількість студентів на кожному факультеті"),
        ("SELECT Students.Student_id, Student_surname, Student_name, Student_lastname, Title, Score FROM Students "
         "INNER JOIN Passing_exams ON Students.Student_id = Passing_exams.Student_id "
         "INNER JOIN Subjects ON Passing_exams.Subject_id = Subjects.Subject_id",
         "Оцінки кожного студента по кожному предмету"),
    ]

    for query, description in queries:
        if subject_name[0] in description:
            print_query_results(query, description, subject_name)
        else:
            print_query_results(query, description, "")

except mysql.connector.Error as err:
    print("Помилка MySQL: {}".format(err))

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
