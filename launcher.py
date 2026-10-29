import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(BASE_DIR)

os.system(
    f'"{sys.executable}" -m streamlit run app.py'
)