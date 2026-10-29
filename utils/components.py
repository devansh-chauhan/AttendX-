import streamlit as st


def metric_card(title, value, subtitle="", icon="📊"):

    st.markdown(
        f"""
        <div style="
            background: white;
            border-radius:18px;
            padding:25px;
            box-shadow:0 6px 20px rgba(0,0,0,.08);
            border-left:6px solid #6C63FF;
            margin-bottom:15px;
        ">

        <div style="
            font-size:18px;
            color:#666;
        ">
            {icon} {title}
        </div>

        <div style="
            font-size:42px;
            font-weight:700;
            margin-top:10px;
            color:#222;
        ">
            {value}
        </div>

        <div style="
            color:#888;
            font-size:14px;
        ">
            {subtitle}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )