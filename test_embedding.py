import cv2
from models.face_engine import detect_faces, save_embedding

camera = cv2.VideoCapture(0)

print("Press S to save embedding")
print("Press Q to quit")

while True:

    success, frame = camera.read()

    if not success:
        break

    faces = detect_faces(frame)

    for face in faces:

        x1, y1, x2, y2 = map(int, face.bbox)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

    cv2.imshow("Register Face", frame)

    key = cv2.waitKey(1)

    if key == ord("s"):

        if len(faces) == 1:

            save_embedding("TEST001", faces[0].embedding)

            print("Embedding Saved!")

        else:
            print("Exactly one face required.")

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()