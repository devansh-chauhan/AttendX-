import streamlit as st

st.set_page_config(
    page_title="AttendX AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

dashboard = st.Page(
    "pages/Dashboard.py",
    title="Dashboard",
    icon="🏠"
)

students = st.Page(
    "pages/Students.py",
    title="Students",
    icon="👨‍🎓"
)

attendance = st.Page(
    "pages/Attendance.py",
    title="Attendance Logs",
    icon="📋"
)

live = st.Page(
    "pages/Live_Attendance.py",
    title="Live Attendance",
    icon="🎥"
)

reports = st.Page(
    "pages/Reports.py",
    title="Reports",
    icon="📊"
)

about = st.Page(
    "pages/About.py",
    title="About",
    icon="ℹ️"
)

pg = st.navigation(
    {
        "Main": [
            dashboard,
            students,
            attendance,
            live
        ],
        "Analytics": [
            reports
        ],
        "Information": [
            about
        ]
    }
)

pg.run()