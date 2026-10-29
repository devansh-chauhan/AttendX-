import streamlit as st
import matplotlib.pyplot as plt
from datetime import date

from utils.theme import load_theme
load_theme()

from modules.attendance import (
    get_all_attendance,
    get_attendance_by_date
)

from modules.pdf_report import generate_pdf

# -------------------------------------------------
# Page Title
# -------------------------------------------------

st.title("📊 Attendance Reports")
st.caption("View, analyze and export attendance records.")

# -------------------------------------------------
# Date Filter
# -------------------------------------------------

selected_date = st.date_input(
    "📅 Select Date",
    value=date.today()
)

if st.button("Generate Report"):
    report = get_attendance_by_date(str(selected_date))
else:
    report = get_all_attendance()

# -------------------------------------------------
# Statistics
# -------------------------------------------------

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📄 Total Records",
        len(report)
    )

with col2:

    if len(report) > 0:

        present = report[
            report["Status"] == "Present"
        ]

        st.metric(
            "✅ Present",
            len(present)
        )

    else:
        st.metric("✅ Present", 0)

with col3:

    if len(report) > 0:

        avg_confidence = round(
            report["Confidence"].mean(),
            2
        )

        st.metric(
            "🎯 Avg Confidence",
            avg_confidence
        )

    else:

        st.metric(
            "🎯 Avg Confidence",
            0
        )

st.info(f"Showing {len(report)} attendance record(s).")

# -------------------------------------------------
# Attendance Table
# -------------------------------------------------

st.divider()

st.subheader("📋 Attendance Records")

st.dataframe(
    report,
    use_container_width=True,
    hide_index=True
)

# -------------------------------------------------
# Analytics
# -------------------------------------------------

st.divider()

st.subheader("📈 Attendance Analytics")

if len(report) > 0:

    status_count = report["Status"].value_counts()

    col1, col2 = st.columns(2)

    # -------------------------
    # Left Column
    # -------------------------

    with col1:

        st.write("### 📊 Status Distribution")

        st.bar_chart(status_count)

        st.write("### 📈 Confidence Trend")

        st.line_chart(
            report["Confidence"]
        )

    # -------------------------
    # Right Column
    # -------------------------

    with col2:

        st.write("### 🥧 Attendance Percentage")

        fig, ax = plt.subplots(figsize=(3.8, 3.8))

        ax.pie(
            status_count,
            labels=status_count.index,
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops={
                "edgecolor": "white"
            },
            textprops={
                "fontsize": 10
            }
        )

        ax.axis("equal")

        st.pyplot(
            fig,
            use_container_width=False
        )

else:

    st.info("No attendance records found.")

# -------------------------------------------------
# Export Reports
# -------------------------------------------------

st.divider()

st.subheader("📤 Export Reports")

csv = report.to_csv(
    index=False
).encode("utf-8")

col1, col2 = st.columns(2)

# CSV

with col1:

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="attendance_report.csv",
        mime="text/csv",
        use_container_width=True
    )

# PDF

with col2:

    if st.button(
        "📄 Generate PDF Report",
        use_container_width=True
    ):

        filename = "attendance_report.pdf"

        generate_pdf(
            report,
            filename
        )

        with open(filename, "rb") as file:

            st.download_button(
                label="⬇ Download PDF",
                data=file,
                file_name=filename,
                mime="application/pdf",
                use_container_width=True
            )