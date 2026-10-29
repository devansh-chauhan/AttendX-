from modules.attendance import mark_attendance

result = mark_attendance(
    "1001",
    0.98
)

if result:
    print("Attendance Marked")
else:
    print("Already Present")