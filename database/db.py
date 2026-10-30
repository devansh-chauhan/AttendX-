import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "database.db"


def get_connection():
    DATABASE.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(DATABASE))
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Create the database tables if they do not already exist."""

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT,
                semester INTEGER,
                section TEXT,
                email TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                student_id TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                confidence REAL,
                status TEXT DEFAULT 'Present',
                FOREIGN KEY (student_id)
                    REFERENCES students(student_id)
            )
        """)

        conn.commit()

