import cv2
from models.face_engine import detect_faces

camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        break

    faces = detect_faces(frame)

    for face in faces:

        x1, y1, x2, y2 = map(int, face.bbox)

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()