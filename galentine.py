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
st.write("on this galentine's day, I want to ask you something")
st.subheader("Will you be my Galentine forever? 🥰💌")

# Session state to handle button clicks
if 'declined' not in st.session_state:
    st.session_state.declined = False
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

if not st.session_state.accepted:
    if not st.session_state.declined:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("💝 Yes, bestie! 💝"):
                st.session_state.accepted = True
                st.balloons()
                st.success("Yay! You're my Galentine forever! 💕✨")
                st.image("https://media.giphy.com/media/l41lTnA4Lohw5hO2U/giphy.gif")
                st.rerun()

        with col2:
            if st.button("🤔 No 🤔"):
                st.session_state.declined = True
                st.rerun()
    else:
        st.subheader("You can't escape! Think again! 😜💖")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("😒 No 😒"):
                st.rerun()
        with col2:
            if st.button("🤔 Think Again 🤔"):
                st.session_state.declined = False
                st.rerun()
