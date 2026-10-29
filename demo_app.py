"""Public, privacy-safe AttendX AI showcase.

This file intentionally does not import the local biometric application, SQLite
database, OpenCV, InsightFace, or any local student records.
"""

from datetime import date

import pandas as pd
import streamlit as st


st.set_page_config(page_title="AttendX AI | Safe Demo", page_icon="🎓", layout="wide")

st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(135deg, #07142d 0%, #102a56 55%, #0b1b39 100%); color: #f6f9ff; }
    [data-testid="stMetric"] { background: rgba(255,255,255,.08); padding: 1rem; border-radius: 14px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("AttendX AI")
st.caption("Public product showcase · fictional data only · no webcam, biometric processing, or persistent records")

st.info(
    "This is a privacy-safe demonstration. The live face-enrollment and camera attendance workflow runs locally only, "
    "with consented users and appropriate safeguards."
)

today = date.today().isoformat()
attendance = pd.DataFrame(
    [
        ("DEMO-001", "Student A", "Computer Science", "09:04", 0.91, "Present"),
        ("DEMO-002", "Student B", "Computer Science", "09:08", 0.88, "Present"),
        ("DEMO-003", "Student C", "Electronics", "09:11", 0.93, "Present"),
        ("DEMO-004", "Student D", "Mechanical", "09:16", 0.86, "Present"),
    ],
    columns=["Student ID", "Display name", "Department", "Time", "Confidence", "Status"],
)
trend = pd.DataFrame(
    {"Date": pd.date_range(end=date.today(), periods=7), "Present": [42, 48, 45, 53, 51, 55, 58]}
).set_index("Date")

metrics = st.columns(4)
metrics[0].metric("Demo students", "60")
metrics[1].metric("Today’s sample attendance", "58")
metrics[2].metric("Average confidence", "89.5%")
metrics[3].metric("System status", "Showcase mode")

left, right = st.columns([1.25, 1])
with left:
    st.subheader("Attendance trend")
    st.line_chart(trend, color="#42a5ff")
with right:
    st.subheader("How AttendX works locally")
    st.markdown(
        """
        1. Register a student with consent.
        2. Capture a face locally and create an embedding.
        3. Verify one face at a time through the local camera.
        4. Record attendance in a local database.
        5. Review trends and export reports.
        """
    )

st.subheader(f"Sample attendance log — {today}")
st.dataframe(
    attendance.style.format({"Confidence": "{:.0%}"}),
    width="stretch",
    hide_index=True,
)

st.subheader("Built-in safeguards")
safeguards = st.columns(3)
safeguards[0].success("Single-face validation\n\nBlocks attendance when multiple faces are detected.")
safeguards[1].info("Duplicate prevention\n\nRecords one entry per student per day.")
safeguards[2].warning("Public-demo privacy\n\nNo face images, embeddings, database, or real student details are used here.")

with st.expander("Technology and deployment note"):
    st.markdown(
        "**Local application:** Python, Streamlit, OpenCV, InsightFace, SQLite, Pandas, and NumPy.\n\n"
        "**Hosted showcase:** Streamlit and Pandas only. The server cannot access a visitor’s webcam through OpenCV, "
        "and free-hosted local storage is not suitable for biometric records."
    )

st.caption("Illustrative demo values only — not measured recognition accuracy or real attendance data.")
