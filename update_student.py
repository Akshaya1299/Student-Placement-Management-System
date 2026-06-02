import sqlite3

conn = sqlite3.connect("placement.db")

cursor = conn.cursor()

usn = input("Enter USN of Student to Update: ")
new_cgpa = float(input("Enter New CGPA: "))

cursor.execute(
    "UPDATE students SET cgpa = ? WHERE usn = ?",
    (new_cgpa, usn)
)

conn.commit()

if cursor.rowcount > 0:
    print("Student Updated Successfully")
else:
    print("Student Not Found")

conn.close()