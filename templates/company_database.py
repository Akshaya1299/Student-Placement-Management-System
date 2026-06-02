import sqlite3

conn = sqlite3.connect("placement.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS companies")

cursor.execute("""
CREATE TABLE companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    cgpa REAL
)
""")

conn.commit()

print("Companies table recreated successfully!")

conn.close()