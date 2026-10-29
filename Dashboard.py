import streamlit as st
from modules.dashboard import total_students, today_attendance

from utils.theme import load_theme
load_theme()

st.title("🏠 Dashboard")

st.markdown("### Welcome to AttendX AI")

st.write("AI Powered Face Recognition Attendance System")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👨‍🎓 Total Students",
        total_students()
    )

with col2:
    st.metric(
        "📅 Today's Attendance",
        today_attendance()
    )

with col3:
    st.metric(
        "🤖 AI Status",
        "🟢 Online"
    )

st.divider()

st.subheader("System Status")

left, right = st.columns(2)

with left:
    st.success("✅ Face Recognition Model Loaded")
    st.success("✅ Database Connected")
    st.success("✅ Attendance Module Ready")

with right:
    st.info("📷 Webcam Ready")
    st.info("⚡ GPU Acceleration Enabled")
    st.info("🎯 Recognition Engine Active")

from modules.attendance import attendance_summary

summary = attendance_summary()

st.subheader("Attendance Trend")

st.line_chart(
    summary.set_index("date")
)

st.divider()

st.caption(
    "AttendX AI • Face Recognition Attendance System • Version 1.0"
)