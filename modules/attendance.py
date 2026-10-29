import pandas as pd
from datetime import datetime
from database.db import get_connection


def mark_attendance(student_id, confidence):

    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    # Check if attendance is already marked today
    cursor.execute(
        """
        SELECT * FROM attendance
        WHERE student_id = ?
        AND date = ?
        """,
        (student_id, today)
    )

    existing = cursor.fetchone()

    if existing:
        conn.close()
        return False

    cursor.execute(
        """
        INSERT INTO attendance
        (
            student_id,
            date,
            time,
            confidence,
            status
        )

        VALUES (?, ?, ?, ?, ?)
        """,
        (
            student_id,
            today,
            current_time,
            float(confidence),
            "Present"
        )
    )

    conn.commit()
    conn.close()

    return True


def get_attendance():

    conn = get_connection()

    query = """
        SELECT
            student_id,
            date,
            time,
            confidence,
            status
        FROM attendance
        ORDER BY date DESC, time DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    df.columns = [
        "Student ID",
        "Date",
        "Time",
        "Confidence",
        "Status"
    ]

    return df


def search_attendance(student_id):

    conn = get_connection()

    query = """
        SELECT
            student_id,
            date,
            time,
            confidence,
            status
        FROM attendance
        WHERE student_id LIKE ?
        ORDER BY date DESC, time DESC
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(f"%{student_id}%",)
    )

    conn.close()

    df.columns = [
        "Student ID",
        "Date",
        "Time",
        "Confidence",
        "Status"
    ]

    return df


def get_attendance_by_date(date):

    conn = get_connection()

    query = """
        SELECT
            student_id,
            date,
            time,
            confidence,
            status
        FROM attendance
        WHERE date=?
        ORDER BY time
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(date,)
    )

    conn.close()

    df.columns = [
        "Student ID",
        "Date",
        "Time",
        "Confidence",
        "Status"
    ]

    return df


def get_all_attendance():

    conn = get_connection()

    query = """
        SELECT
            student_id,
            date,
            time,
            confidence,
            status
        FROM attendance
        ORDER BY date DESC,time DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    df.columns = [
        "Student ID",
        "Date",
        "Time",
        "Confidence",
        "Status"
    ]

    return df

def attendance_summary():

    conn = get_connection()

    query = """
    SELECT
        date,
        COUNT(*) as Present
    FROM attendance
    GROUP BY date
    ORDER BY date DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

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

    count = cursor.fetchone()[0]

    conn.close()

    return count

from database.db import get_connection


def student_attendance_stats(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            AVG(confidence),
            MAX(date)
        FROM attendance
        WHERE student_id=?
    """, (student_id,))

    total, avg_confidence, last_date = cursor.fetchone()

    conn.close()

    return {
        "total": total or 0,
        "confidence": round((avg_confidence or 0) * 100, 2),
        "last": last_date if last_date else "Never"
    }

def attendance_percentage_student(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT date)
        FROM attendance
    """)

    total_days = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM attendance
        WHERE student_id=?
    """, (student_id,))

    present = cursor.fetchone()[0]

    conn.close()

    if total_days == 0:
        return 0

    return round((present / total_days) * 100, 1)

def student_history(student_id):

    conn = get_connection()

    query = """
    SELECT
        date,
        confidence
    FROM attendance
    WHERE student_id=?
    ORDER BY date
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(student_id,)
    )

    conn.close()

    return df