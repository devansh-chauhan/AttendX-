import streamlit as st

from utils.theme import load_theme
load_theme()

st.title("ℹ About AttendX AI")

st.write("""
AttendX AI is an AI-powered attendance management system
that uses InsightFace for real-time face recognition.

Features:
- Face Registration
- Student Management
- Live Attendance
- Reports
- Analytics
- CSV Export

Technology Stack

• Python
• Streamlit
• OpenCV
• InsightFace
• SQLite
• NumPy
• Pandas
""")