import sqlite3

conn = sqlite3.connect("placement.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    usn TEXT,
    branch TEXT,
    cgpa REAL
)
""")

conn.commit()

print("Students table created successfully!")

conn.close()