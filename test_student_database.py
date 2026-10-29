from modules.student import add_student, get_student

add_student(
    "1001",
    "Devansh Chauhan",
    "AIML",
    3,
    "A",
    "dev@example.com",
    "data/images/1001.jpg",
    "data/embeddings/1001.npy"
)

print(get_student("1001"))