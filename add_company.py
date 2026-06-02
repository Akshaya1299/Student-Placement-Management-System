import sqlite3

conn = sqlite3.connect("placement.db")

cursor = conn.cursor()

company_name = input("Enter Company Name: ")
role = input("Enter Role: ")
min_cgpa = float(input("Enter Minimum CGPA: "))

cursor.execute(
    "INSERT INTO companies(company_name, role, min_cgpa) VALUES (?, ?, ?)",
    (company_name, role, min_cgpa)
)

conn.commit()

print("Company Added Successfully")

conn.close()