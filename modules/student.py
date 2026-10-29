from database.db import get_connection


def add_student(
    student_id,
    name,
    department,
    semester,
    section,
    email,
    image_path,
    embedding_path
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (
            student_id,
            name,
            department,
            semester,
            section,
            email,
            image_path,
            embedding_path
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        student_id,
        name,
        department,
        semester,
        section,
        email,
        image_path,
        embedding_path
    ))

    conn.commit()
    conn.close()


def get_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            student_id,
            name,
            department,
            semester,
            section,
            email
        FROM students
        ORDER BY student_id
    """)

    students = cursor.fetchall()

    conn.close()

    return students

def get_student_photo(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT image_path
        FROM students
        WHERE student_id=?
    """, (student_id,))

    photo = cursor.fetchone()

    conn.close()

    return photo[0] if photo else None

def get_student(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            student_id,
            name,
            department,
            semester,
            section,
            email,
            image_path
        FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    conn.close()

    return student

def search_students(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            student_id,
            name,
            department,
            semester,
            section,
            email
        FROM students

        WHERE
            student_id LIKE ?
            OR name LIKE ?
            OR department LIKE ?
    """,
    (
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    students = cursor.fetchall()

    conn.close()

    return students


def delete_student(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()

def total_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count