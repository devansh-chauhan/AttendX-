import os
import cv2
import numpy as np
from insightface.app import FaceAnalysis

# ----------------------------
# Initialize Face Model
# ----------------------------

app = FaceAnalysis(name="buffalo_s")
app.prepare(
    ctx_id=0,
    det_size=(480, 480)
)

# ----------------------------
# Load All Embeddings Once
# ----------------------------

EMBEDDING_FOLDER = "data/embeddings"

registered_embeddings = {}


def load_registered_embeddings():
    """
    Loads all embeddings into RAM.
    Called only once when application starts.
    """

    registered_embeddings.clear()

    if not os.path.exists(EMBEDDING_FOLDER):
        os.makedirs(EMBEDDING_FOLDER)
        return

    for file in os.listdir(EMBEDDING_FOLDER):

        if file.endswith(".npy"):

            student_id = file[:-4]

            path = os.path.join(
                EMBEDDING_FOLDER,
                file
            )

            registered_embeddings[student_id] = np.load(path)

    print(f"{len(registered_embeddings)} embeddings loaded.")


load_registered_embeddings()

# ----------------------------
# Face Detection
# ----------------------------


def detect_faces(frame):
    return app.get(frame)

# ----------------------------
# Save Embedding
# ----------------------------


def save_embedding(student_id, embedding):

    path = os.path.join(
        EMBEDDING_FOLDER,
        f"{student_id}.npy"
    )

    np.save(path, embedding)

    registered_embeddings[student_id] = embedding

# ----------------------------
# Cosine Similarity
# ----------------------------


def cosine_similarity(e1, e2):

    e1 = e1 / np.linalg.norm(e1)
    e2 = e2 / np.linalg.norm(e2)

    return np.dot(e1, e2)

# ----------------------------
# Face Recognition
# ----------------------------


def recognize_face(face_embedding):

    best_match = None
    best_score = -1

    for student_id, embedding in registered_embeddings.items():

        score = cosine_similarity(
            face_embedding,
            embedding
        )

        if score > best_score:

            best_score = score
            best_match = student_id

    return best_match, best_score