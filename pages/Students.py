import streamlit as st
import pandas as pd
if "selected_student" not in st.session_state:
    st.session_state.selected_student = None

from PIL import Image
from modules.student import get_student_photo

from utils.theme import load_theme

load_theme()

from modules.student import (
    add_student,
    get_students,
    get_student,
    search_students,
    delete_student
)

from modules.attendance import (
    student_attendance_stats,
    attendance_percentage_student,
    student_history
)

from modules.dashboard import total_students
from modules.register_face import capture_face
from modules.id_card import generate_id_card

st.title("👨‍🎓 Student Management")

# --------------------------
# Statistics
# --------------------------

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Registered Students",
        total_students()
    )

with col2:
    st.metric(
        "Database Status",
        "Connected"
    )

st.divider()

# --------------------------
# Student Registration
# --------------------------

st.subheader("➕ Register Student")

with st.form("student_form"):

    student_id = st.text_input("Student ID")
    name = st.text_input("Student Name")

    col1, col2 = st.columns(2)

    with col1:
        department = st.text_input("Department")
        section = st.text_input("Section")

    with col2:
        semester = st.number_input(
            "Semester",
            min_value=1,
            max_value=8,
            value=3
        )

        email = st.text_input("Email")

        # photo = st.file_uploader(
        #         "Student Photo",
        #         type=["jpg", "jpeg", "png"]
# )

    submitted = st.form_submit_button(
        "➕ Register Student",
        use_container_width=True
    )

    if submitted:

        if student_id.strip() == "" or name.strip() == "":
            st.error("Student ID and Name are required.")

        else:

            with st.spinner("Opening camera..."):

                image_path = capture_face(student_id)

            if image_path:

                embedding_path = f"data/embeddings/{student_id}.npy"

                add_student(
                    student_id,
                    name,
                    department,
                    semester,
                    section,
                    email,
                    image_path,
                    embedding_path
                )

                st.success("✅ Student Registered Successfully!")

                st.balloons()

                st.rerun()

            else:

                st.error("Face registration cancelled.")

# --------------------------
# Registered Students
# --------------------------

st.divider()

st.subheader("📋 Registered Students")

students = get_students()
st.subheader("👤 Student Profiles")

for student in students:

    sid = student[0]
    photo = get_student_photo(sid)

    with st.container(border=True):

        col1, col2, col3 = st.columns([1,3,1])

        with col1:

            if photo:
                st.image(photo, width=120)
            else:
                st.image("assets/default_user.png", width=120)

        with col2:

            st.markdown(f"## {student[1]}")

            st.write(f"**🎓 Student ID:** {student[0]}")
            st.write(f"**🏫 Department:** {student[2]}")
            st.write(f"**📚 Semester:** {student[3]}")
            st.write(f"**👥 Section:** {student[4]}")
            st.write(f"**📧 Email:** {student[5]}")

            st.success("✅ Face Registered")

        with col3:

            if st.button(
                "👁 View",
                key=f"view_{sid}"
            ):
                st.session_state.selected_student = sid

            if st.button(
                "🗑 Delete",
                key=f"delete_{sid}"
            ):
                delete_student(sid)

if st.session_state.selected_student:

    student = get_student(st.session_state.selected_student)

    photo = get_student_photo(st.session_state.selected_student)

    st.divider()

    st.subheader("👤 Student Profile")

    left, right = st.columns([1,3])

    with left:

        if photo:
            st.image(photo, width=220)
        else:
            st.image("assets/default_user.png", width=220)

    with right:

        st.markdown(f"## {student[1]}")

        st.write(f"**Student ID:** {student[0]}")
        st.write(f"**Department:** {student[2]}")
        st.write(f"**Semester:** {student[3]}")
        st.write(f"**Section:** {student[4]}")
        st.write(f"**Email:** {student[5]}")

        st.success("Face Registered")

    stats = student_attendance_stats(student[0])

    attendance = attendance_percentage_student(student[0])

    if st.button("🆔 Generate ID Card"):

        card_path = generate_id_card(
            student,
            photo
        )

        st.success("ID Card Generated Successfully!")

        st.image(
            card_path,
            width=350
        )

        with open(card_path, "rb") as file:

            st.download_button(
                "⬇ Download ID Card",
                file,
                file_name=f"{student[0]}_ID_Card.png",
                mime="image/png"
            )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
        "Attendance %",
        f"{attendance}%"
    )

    with c2:

        st.metric(
        "Present Days",
        stats["total"]
    )

    st.progress(attendance / 100)

    st.metric(
        "Average Recognition",
        f'{stats["confidence"]}%'
    )

    st.metric(
        "Last Attendance",
        stats["last"]
    )

    history = student_history(student[0])

    if not history.empty:

        st.divider()

        st.write("### 📈 Attendance Confidence Trend")

        st.line_chart(
        history.set_index("date")["confidence"]
        )

    if attendance >= 90:

        st.success("🏆 Excellent Attendance")

    elif attendance >= 75:

        st.info("🥈 Good Attendance")

    elif attendance >= 60:

        st.warning("🥉 Average Attendance")

    else:

        st.error("⚠ Needs Improvement")

    st.divider()

    left, right = st.columns(2)

    with left:

        st.metric(
        "Registration",
        "Completed"
        )

    with right:

        st.metric(
        "Face Status",
        "Verified"
        )

# --------------------------
# Search Student
# --------------------------

st.divider()

st.subheader("🔍 Search Student")

search = st.text_input("Search by ID, Name or Department")

if search:

    result = search_students(search)

else:

    result = get_students()

if result:

    df = pd.DataFrame(
        result,
        columns=[
            "Student ID",
            "Name",
            "Department",
            "Semester",
            "Section",
            "Email"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:
    st.warning("No matching student found.")

# --------------------------
# Delete Student
# --------------------------

st.divider()

st.subheader("🗑 Delete Student")

delete_id = st.text_input("Student ID")

if st.button(
    "🗑 Delete Student",
    use_container_width=True
):

    if delete_id.strip():

        delete_student(delete_id)

        st.success("Student Deleted Successfully!")

        st.rerun()

    else:
        st.warning("Please enter a Student ID.")