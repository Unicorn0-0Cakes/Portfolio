import sqlite3
from datetime import datetime

# Connect to the SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('datasets/chatbot_archive.sqlite')
cursor = conn.cursor()

-- Create the 'chatbots' table
CREATE TABLE chatbots (
    chatbot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    visibility TEXT CHECK (visibility IN ('public', 'private')),
    status TEXT CHECK (status IN ('active', 'retired', 'archived')),
    created_date TEXT,
    last_updated TEXT
);

-- Create the 'instructions' table
CREATE TABLE instructions (
    instruction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chatbot_id INTEGER,
    instruction_text TEXT NOT NULL,
    version TEXT,
    date_added TEXT,
    FOREIGN KEY (chatbot_id) REFERENCES chatbots (chatbot_id)
);

-- Create the 'updates' table
CREATE TABLE updates (
    update_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chatbot_id INTEGER,
    update_date TEXT NOT NULL,
    update_notes TEXT,
    FOREIGN KEY (chatbot_id) REFERENCES chatbots (chatbot_id)
);

-- Create the 'interaction_stats' table
CREATE TABLE interaction_stats (
    stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chatbot_id INTEGER,
    total_chats INTEGER DEFAULT 0,
    last_active_date TEXT,
    FOREIGN KEY (chatbot_id) REFERENCES chatbots (chatbot_id)
);

-- Create the 'tags' table
CREATE TABLE tags (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chatbot_id INTEGER,
    tag TEXT NOT NULL,
    FOREIGN KEY (chatbot_id) REFERENCES chatbots (chatbot_id)
);

# Commit changes and close the connection
conn.commit()
conn.close()
print("Database and tables created successfully!")
