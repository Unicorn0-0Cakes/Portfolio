import sqlite3
from datetime import datetime

# Connect to the SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('datasets/chatbot_archive.sqlite')
cursor = conn.cursor()

# Create the 'conversations' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT NOT NULL,
    bot_response TEXT NOT NULL,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

# Create the 'users' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully!")
