import sqlite3

conn = sqlite3.connect("placement.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM companies")

companies = cursor.fetchall()

for company in companies:
    print("\nCompany Details")
    print("ID:", company[0])
    print("Company:", company[1])
    print("Role:", company[2])
    print("Minimum CGPA:", company[3])

conn.close()