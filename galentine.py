import streamlit as st

# Set page config
st.set_page_config(page_title="Galentine's Day 💖", page_icon="💌", layout="centered")

# Light pink background
page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #ffe6f2;
}
[data-testid="stHeader"] {
    background-color: #ffb3d9;
}
.stButton>button {
    background-color: #ff66b2 !important;
    color: white !important;
    border-radius: 15px;
    font-size: 20px;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Title & message
st.title("💖 Happy Galentine's Day! 💖")
st.subheader("Will you be my Galentine forever? 🥰💌")

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("💝 Yes, bestie! 💝"):
        st.balloons()
        st.success("Yay! You're my Galentine forever! 💕✨")
        st.image("http://static1.squarespace.com/static/5bb143b5e5f7d140b41f19a5/5c059a23032be416404f126c/65cbd3f71bd5a2703b12866d/1707857520845/w4Ab1TDWnD60pVIxnlXWfP6TiW5TXun27-TgAk-cW5IgVxobTnw94SDesg1fi7u7Op09OcqVl0hBMKR2xkZvU1TdGCXlkpY4_uu1dyEEjQaXPtskt1F_IloUuHS6.jpg?format=1500w")

with col2:
    if st.button("🤔 Let me think... 🤔"):
        st.warning("Take your time, but you know you can't resist! 😜💖")
