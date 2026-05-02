import sqlite3
import os
print("DB PATH:", os.path.abspath("lab.db"))

def init_db():
    conn = sqlite3.connect("lab.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT,
        message TEXT,
        date TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_booking(phone, message, date, time):
    conn = sqlite3.connect("lab.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT,
        message TEXT,
        date TEXT,
        time TEXT
    )
    """)

    c.execute(
        "INSERT INTO bookings (phone, message, date, time) VALUES (?, ?, ?, ?)",
        (phone, message, date, time)
    )

    conn.commit()
    conn.close()


def get_all_bookings():
    conn = sqlite3.connect("lab.db")
    c = conn.cursor()

    c.execute("SELECT phone, message, date, time FROM bookings")
    rows = c.fetchall()

    conn.close()
    return rows