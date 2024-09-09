import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Verify if the table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
table_exists = cursor.fetchone()

if table_exists:
    print("Table 'users' exists.")
else:
    print("Table 'users' does not exist.")

# Print the structure of the users table
cursor.execute("PRAGMA table_info(users);")
columns = cursor.fetchall()

print("Users table structure:")
for column in columns:
    print(column)

conn.close()