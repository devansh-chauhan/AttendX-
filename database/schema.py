import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# ---------------- STUDENTS ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id TEXT UNIQUE NOT NULL,

    name TEXT NOT NULL,

    department TEXT,

    semester INTEGER,

    section TEXT,

    email TEXT,

    image_path TEXT,

    embedding_path TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# ---------------- ATTENDANCE ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id TEXT NOT NULL,

    date DATE NOT NULL,

    time TIME NOT NULL,

    confidence REAL,

    status TEXT DEFAULT 'Present',

    FOREIGN KEY(student_id)
    REFERENCES students(student_id)
)
""")

connection.commit()
connection.close()

print("Database initialized successfully.")
