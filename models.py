# models.py
from db import get_connection

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # Clubs table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clubs (
        club_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT
    )
    """)

    # Students table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)

    # Memberships table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS memberships (
        membership_id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES students(student_id) ON DELETE CASCADE,
        club_id INTEGER REFERENCES clubs(club_id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    cur.close()
    conn.close()