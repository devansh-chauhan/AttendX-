from database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
UPDATE attendance
SET confidence = 0.98
WHERE typeof(confidence)='blob'
""")

conn.commit()

print("Rows Fixed:", conn.total_changes)

conn.close()