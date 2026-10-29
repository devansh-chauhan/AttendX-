import os
import streamlit as st


def load_theme():

    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "assets",
        "style.css"
    )

    path = os.path.abspath(path)

    with open(path) as css:

        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )