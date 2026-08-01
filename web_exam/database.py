import sqlite3

# CREATE DATABASE
conn = sqlite3.connect("math_exam.db")
cursor = conn.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    password TEXT,
                    grade TEXT                  
                    )""")

cursor.execute("""
                CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    name TEXT,
                    grade TEXT,
                    difficulty TEXT,
                    score REAL,
                    date TEXT,
                    time_seconds REAL                 
                )
                """)



conn.commit()
conn.close()