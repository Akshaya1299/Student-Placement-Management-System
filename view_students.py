import sqlite3

conn = sqlite3.connect("placement.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print("\nStudent Details")
    print("ID:", student[0])
    print("Name:", student[1])
    print("USN:", student[2])
    print("Branch:", student[3])
    print("CGPA:", student[4])

conn.close()