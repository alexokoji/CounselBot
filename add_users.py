import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

username = 'user1'
email = 'user1@example.com'
name = 'User One'
password = 'password123'
hashed_password = password

cursor.execute('''
INSERT INTO users (username, email, name, password)
VALUES (?, ?, ?, ?)
''', (username, email, name, hashed_password))

conn.commit()
conn.close()