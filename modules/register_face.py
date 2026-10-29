import os
import cv2

from utils.theme import load_theme
load_theme()

from models.face_engine import (
    detect_faces,
    save_embedding
)

IMAGE_FOLDER = "data/images"

os.makedirs(IMAGE_FOLDER, exist_ok=True)


def capture_face(student_id):

    camera = cv2.VideoCapture(0)

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:

        success, frame = camera.read()

        if not success:
            break

        faces = detect_faces(frame)

        if len(faces) == 1:

            face = faces[0]

            x1, y1, x2, y2 = map(int, face.bbox)

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Press SPACE to Capture",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        elif len(faces) > 1:

            cv2.putText(
                frame,
                "Only One Face Allowed",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        else:

            cv2.putText(
                frame,
                "No Face Detected",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        cv2.imshow("Register Face", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == 32 and len(faces) == 1:

            image_path = os.path.join(
                IMAGE_FOLDER,
                f"{student_id}.jpg"
            )

            cv2.imwrite(image_path, frame)

            save_embedding(
                student_id,
                faces[0].embedding
            )

            camera.release()
            cv2.destroyAllWindows()

            return image_path

        elif key == ord("q"):

            break

    camera.release()
    cv2.destroyAllWindows()

    return None