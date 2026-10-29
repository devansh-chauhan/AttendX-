from database.db import get_connection
import pandas as pd
from datetime import datetime


def total_students():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def today_attendance():

    conn = get_connection()

    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attendance
        WHERE date=?
        """,
        (today,)
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def attendance_percentage():

    students = total_students()

    if students == 0:
        return 0

    return round(
        today_attendance() / students * 100,
        1
    )


def average_confidence():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT AVG(confidence)
        FROM attendance
        """
    )

    value = cursor.fetchone()[0]

    conn.close()

    if value is None:
        return 0

    return round(value * 100, 1)


def camera_status():

    return "🟢 Online"


def attendance_by_day():

    conn = get_connection()

    query = """
        SELECT
            date,
            COUNT(*) AS Attendance
        FROM attendance
        GROUP BY date
        ORDER BY date
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def department_statistics():

    conn = get_connection()

    query = """
        SELECT
            department,
            COUNT(*) AS Students
        FROM students
        GROUP BY department
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

def recent_attendance():

    conn = get_connection()

    query = """
        SELECT
            student_id,
            date,
            time,
            confidence
        FROM attendance
        ORDER BY id DESC
        LIMIT 5
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def recent_students():

    conn = get_connection()

    query = """
        SELECT
            student_id,
            name,
            department
        FROM students
        ORDER BY id DESC
        LIMIT 5
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df