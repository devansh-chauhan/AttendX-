import streamlit as st
from utils.components import metric_card
from utils.theme import load_theme
load_theme()

from modules.dashboard import (
    total_students,
    today_attendance,
    attendance_percentage,
    average_confidence,
    camera_status,
    attendance_by_day,
    department_statistics,
    recent_attendance,
    recent_students
)

# -----------------------------
# Page Configuration
# -----------------------------

# st.set_page_config(
#     page_title="AttendX AI",
#     page_icon="🎓",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# -----------------------------
# Header
# -----------------------------

st.markdown("""
<h1 style='font-size:48px;'>
🎓 AttendX AI
</h1>

<p style='font-size:18px;color:gray'>
AI Powered Face Recognition Attendance Management System
</p>
""",
unsafe_allow_html=True)

st.divider()

# -----------------------------
# Dashboard Metrics
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card(
        title="Students",
        value=total_students(),
        subtitle="Registered",
        icon="👨‍🎓"
    )

with col2:
    metric_card(
        title="Today's Attendance",
        value=today_attendance(),
        subtitle="Present Today",
        icon="✅"
    )

with col3:
    metric_card(
        title="Average Confidence",
        value=f"{average_confidence()}%",
        subtitle="Recognition Accuracy",
        icon="🎯"
    )

with col4:
    metric_card(
        title="Camera Status",
        value=camera_status(),
        subtitle="Device Status",
        icon="📷"
    )

st.divider()

# -----------------------------
# Charts
# -----------------------------

left, right = st.columns(2)

with left:

    st.subheader("📈 Attendance Trend")

    attendance = attendance_by_day()

    if attendance.empty:

        st.info("No attendance records available.")

    else:

        st.line_chart(
            attendance.set_index("date")
        )

with right:

    st.subheader("🏫 Department Distribution")

    dept = department_statistics()

    if dept.empty:

        st.info("No student records available.")

    else:

        st.bar_chart(
            dept.set_index("department")
        )

st.divider()

st.subheader("⚡ Dashboard Overview")

left, right = st.columns(2)

with left:

    st.write("### 🕒 Recent Attendance")

    attendance = recent_attendance()

    if attendance.empty:

        st.info("No attendance yet.")

    else:

        st.dataframe(
            attendance,
            use_container_width=True,
            hide_index=True
        )

with right:

    st.write("### 👨‍🎓 Recently Registered")

    students = recent_students()

    if students.empty:

        st.info("No students found.")

    else:

        st.dataframe(
            students,
            use_container_width=True,
            hide_index=True
        )

st.divider()

st.subheader("⚡ Quick Actions")

c1, c2, c3 = st.columns(3)

with c1:

    st.info("📸 Register a new face from the Face Enrollment page.")

with c2:

    st.info("📹 Start Live Recognition from the Live Recognition page.")

with c3:

    st.info("📊 Generate reports from the Reports page.")

st.divider()

# -----------------------------
# System Information
# -----------------------------

st.subheader("🖥 System Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🟢 Face Recognition Engine")

with col2:
    st.success("🟢 SQLite Database")

with col3:
    st.success("🟢 Camera Ready")

st.divider()

st.success("✔ AttendX AI is running successfully.")

st.caption(
    "Developed using Python • Streamlit • SQLite • InsightFace • OpenCV"
)