import cv2

from models.face_engine import (
    detect_faces,
    recognize_face
)

from modules.student import get_student

camera = cv2.VideoCapture(0)

# Reduce camera resolution
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frame_count = 0
faces = []

while True:

    success, frame = camera.read()

    if not success:
        break

    frame_count += 1

    # Run AI only every 3rd frame
    if frame_count % 3 == 0:
        faces = detect_faces(frame)

    for face in faces:

        x1, y1, x2, y2 = map(int, face.bbox)

        student_id, score = recognize_face(face.embedding)

    if score > 0.6:

        student = get_student(student_id)

        if student:
            text = f"{student[1]} | {student[2]} | {score:.2f}"

        else:
            text = "Student Not Found"

        color = (0, 255, 0)

    else:
        text = "Unknown"
        color = (0, 0, 255)

        
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

    cv2.imshow("AttendX AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()