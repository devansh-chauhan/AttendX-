import cv2
import numpy as np

from models.face_engine import (
    detect_faces,
    recognize_face
)

from modules.student import get_student
from modules.attendance import mark_attendance


# -----------------------------
# Check Lighting
# -----------------------------

def check_light(frame):

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    return np.mean(gray)


# -----------------------------
# Live Attendance
# -----------------------------

def start_attendance():

    camera = cv2.VideoCapture(0)

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    frame_count = 0
    faces = []

    while True:

        success, frame = camera.read()

        if not success:
            break

        frame_count += 1

        # -----------------------------
        # Lighting Check
        # -----------------------------

        brightness = check_light(frame)

        if brightness < 60:

            cv2.putText(
                frame,
                "Low Light! Improve Lighting",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        # -----------------------------
        # Detect Faces
        # -----------------------------

        if frame_count % 3 == 0:
            faces = detect_faces(frame)

        # -----------------------------
        # No Face
        # -----------------------------

        if len(faces) == 0:

            cv2.putText(
                frame,
                "No Face Detected",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

            cv2.putText(
                frame,
                "AttendX AI Running | Press Q to Exit",
                (20, 450),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

            cv2.imshow("AttendX AI", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            continue

        # -----------------------------
        # Multiple Faces
        # -----------------------------

        if len(faces) > 1:

            cv2.putText(
                frame,
                "Multiple Faces Detected",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

            cv2.putText(
                frame,
                "Attendance Blocked",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

            cv2.imshow("AttendX AI", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            continue

        # -----------------------------
        # Process Face
        # -----------------------------

        for face in faces:

            x1, y1, x2, y2 = map(int, face.bbox)

            face_width = x2 - x1
            face_height = y2 - y1

            area = face_width * face_height

            if area < 12000:

                cv2.putText(
                    frame,
                    "Move Closer",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2
                )

            elif area > 70000:

                cv2.putText(
                    frame,
                    "Move Back",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2
                )

            else:

                cv2.putText(
                    frame,
                    "Perfect Distance",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

            # -----------------------------
            # Face Recognition
            # -----------------------------

            student_id, score = recognize_face(
                face.embedding
            )

            if student_id is not None and score > 0.6:

                student = get_student(student_id)

                if student:

                    marked = mark_attendance(
                        student_id,
                        float(score)
                    )

                    if marked:

                        text = f"{student[1]} ({score*100:.1f}%)"

                        color = (0, 255, 0)

                    else:

                        text = f"{student[1]} Already Marked"

                        color = (255, 0, 0)

                else:

                    text = "Student Not Found"

                    color = (0, 0, 255)

            else:

                text = f"Unknown ({score*100:.1f}%)"

                color = (0, 0, 255)

            # -----------------------------
            # Draw Face Box
            # -----------------------------

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                color,
                2
            )

            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )

        # -----------------------------
        # Footer
        # -----------------------------

        cv2.putText(
            frame,
            "AttendX AI Running | Press Q to Exit",
            (20, 450),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        cv2.imshow(
            "AttendX AI",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()

    cv2.destroyAllWindows()