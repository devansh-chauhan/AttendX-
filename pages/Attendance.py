import streamlit as st

from utils.theme import load_theme
load_theme()

from modules.attendance import (
    get_attendance,
    search_attendance
)

st.title("📋 Attendance Records")

search = st.text_input(
    "🔍 Search by Student ID"
)

if search:

    records = search_attendance(search)

else:

    records = get_attendance()

st.dataframe(
    records,
    use_container_width=True,
    hide_index=True
)