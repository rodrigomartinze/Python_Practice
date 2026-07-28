import sqlite3
conn = sqlite3.connect("math_exam.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM results")
print(cursor.fetchall())
conn.close()