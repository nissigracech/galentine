import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Galentine's Day 💖", page_icon="💌", layout="centered")

# Light pink background
page_bg_color = """
<style>   
[data-testid="stHeader"] {
    background-color: #ffb3d9;
}
.stButton>button {
    background-color: #ff66b2 !important;
    color: white !important;
    border-radius: 15px;
    font-size: 20px;
    transition: all 0.3s ease-in-out;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Title & message
st.title("💖 Happy Galentine's Day! 💖")
st.header("On this Galentine's Day, I want to ask you something")
st.subheader("Will you be my Galentine 🥰💌?")
st.image("gal.jpg", width=300)

# Session state to handle button clicks
if 'declined' not in st.session_state:
    st.session_state.declined = False
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

col1, col2 = st.columns([1, 2])  # col2 is empty
with col1:
    sub_col1, sub_col2 = st.columns(2)

    if not st.session_state.accepted and not st.session_state.declined:
        with sub_col1:
            if st.button("Yes🥹🥹, I will"):
                st.session_state.accepted = True
                st.balloons()
                st.success("Yay! You're my Galentine forever! 💕✨")

        with sub_col2:
            if st.button("No😒, I can't"):
                st.session_state.declined = True
                st.rerun()

if st.session_state.declined:
    st.subheader("You can't escape! Think again! 😜💖")
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        if st.button("😒 No 😒", key="no_button"):
            # Move button to a random position
            st.session_state.declined = True
            st.rerun()
    with sub_col2:
        if st.button("🤔 Think Again 🤔"):
            st.session_state.declined = False
            st.rerun()

    # Apply random positioning for "No" button
    st.markdown(
        f"""
        <style>
        div[data-testid="stButton"]:nth-of-type(1) button {{
            position: absolute;
            left: {random.randint(50, 300)}px;
            top: {random.randint(50, 300)}px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
