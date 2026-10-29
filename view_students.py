from database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

conn.close()