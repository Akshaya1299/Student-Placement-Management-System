import sqlite3

conn = sqlite3.connect("placement.db")
cursor = conn.cursor()

usn = input("Enter Student USN: ")
company_id = int(input("Enter Company ID: "))

cursor.execute("SELECT cgpa FROM students WHERE usn = ?", (usn,))
student = cursor.fetchone()

cursor.execute("SELECT company_name, min_cgpa FROM companies WHERE id = ?", (company_id,))
company = cursor.fetchone()

if student and company:
    student_cgpa = student[0]
    company_name = company[0]
    min_cgpa = company[1]

    if student_cgpa >= min_cgpa:
        print("Eligible for", company_name)
    else:
        print("Not Eligible for", company_name)
else:
    print("Student or Company not found")

conn.close()