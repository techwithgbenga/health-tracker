import sqlite3
from datetime import datetime

DB_NAME = 'health_tracker.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            sleep_hours REAL,
            exercise_minutes REAL,
            water_intake REAL,
            mood_rating INTEGER,
            diary TEXT,
            sentiment REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_log(date, sleep_hours, exercise_minutes, water_intake, mood_rating, diary, sentiment):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (date, sleep_hours, exercise_minutes, water_intake, mood_rating, diary, sentiment)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (date, sleep_hours, exercise_minutes, water_intake, mood_rating, diary, sentiment))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logs ORDER BY date DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows
