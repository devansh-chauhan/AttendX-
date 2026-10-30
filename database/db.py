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

**Important:** This assumes your existing `students` table has the listed columns. Before using this version, check your actual student schema in the existing database initialization code or `modules/student.py`. If it differs, preserve the existing schema instead of replacing it with this example.

Also, `CREATE TABLE IF NOT EXISTS` creates missing tables but does not repair an existing table with an incompatible schema.


Open your main `app.py` file.

At the beginning of the file, add:

```python
from database.db import init_db

init_db()
```

Place these lines after the imports and before any dashboard or page code queries the database.

This ensures the tables are initialized before your application tries to retrieve attendance records.

If your project already has a database initialization function, reuse it rather than creating a second initialization system.


Your attendance module already contains the main operations we need:

- `mark_attendance()`
- `get_attendance()`
- `search_attendance()`
- `get_attendance_by_date()`
- `attendance_summary()`
- `today_attendance()`
- `student_attendance_stats()`

The immediate error occurs because the queried table is missing, not because the SQL query itself is malformed.

We should avoid changing these functions until we verify that the correct database and tables are being used.


Once you've verified the student schema and updated the code:

1. Save the changes to `database/db.py`.
2. Save the changes to `app.py`.
3. Commit the changes to your `main` branch.
4. Open your Streamlit Community Cloud dashboard.
5. Wait for the app to redeploy.
6. Open your deployed application and check the dashboard and attendance pages.

Your deployment is:

[AttendX AI — Live Application](https://lrgdsgbarfgwgdbhk7mh5k.streamlit.app/)


Your current database path is:

```python
DATABASE = "database.db"
```

This is a relative path. Depending on the working directory, SQLite may open a different database file from the one you expect.

The updated version uses an absolute path relative to `database/db.py`, which helps avoid that problem.

However, **this will not automatically restore student records from your computer**. The deployed application runs in a separate environment, and its local database may not contain your existing students or face embeddings.

For a public demo, we should use synthetic student records. Before using AttendX AI for real attendance, we should configure persistent database storage and protect all student and facial data.


Please send me the contents of your existing `modules/student.py`, particularly the `add_student()` function and any SQL that creates the `students` table.

I want to verify your actual student schema before you deploy these changes, so we don't fix the attendance error only to introduce a new student-registration error.import sqlite3

DATABASE = "database.db"

def get_connection():
    return sqlite3.connect(DATABASE)
