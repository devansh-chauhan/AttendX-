import streamlit as st
from modules.live_attendance import start_attendance

from utils.theme import load_theme
load_theme()

st.title("📷 Live Attendance")

st.caption("Real-Time AI Face Recognition Attendance")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📷 Camera",
        "Ready"
    )

with col2:
    st.metric(
        "🤖 AI Model",
        "Loaded"
    )

with col3:
    st.metric(
        "👤 Recognition",
        "Waiting..."
    )

st.divider()

status = st.empty()

status.info("Press the button below to start attendance.")

if st.button(
    "▶ Start Camera",
    use_container_width=True
):
    start_attendance()