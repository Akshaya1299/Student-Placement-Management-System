import sqlite3

conn = sqlite3.connect("placement.db")

cursor = conn.cursor()

name = input("Enter Name: ")
usn = input("Enter USN: ")
branch = input("Enter Branch: ")
cgpa = float(input("Enter CGPA: "))

cursor.execute(
    "INSERT INTO students (name, usn, branch, cgpa) VALUES (?, ?, ?, ?)",
    (name, usn, branch, cgpa)
)

conn.commit()

print("Student Added Successfully")

conn.close()