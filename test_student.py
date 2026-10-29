from database.schema import create_database
from modules.student import add_student

create_database()

add_student(
    "CSE001",
    "Dev",
    "CSE-AIML",
    3,
    "A",
    "dev@gmail.com"
)