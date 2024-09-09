import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT,
    name TEXT,
    password TEXT,
    security_question TEXT,
    security_answer TEXT
)
''')

conn.commit()
conn.close()
