import sqlite3

conn = sqlite3.connect("placement.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    role TEXT,
    min_cgpa REAL
)
""")

conn.commit()

print("Company Table Created")

conn.close()