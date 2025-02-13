import streamlit as st

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
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Title & message
st.title("💖 Happy Galentine's Day! 💖")
st.header("on this galentine's day, I want to ask you something")
st.subheader("Will you be my Galentine 🥰💌?")
st.image("gal.jpg")
# Session state to handle button clicks
if 'declined' not in st.session_state:
    st.session_state.declined = False
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

if not st.session_state.accepted:
    if not st.session_state.declined:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Yes🥹🥹, I will"):
                st.session_state.accepted = True
                st.balloons()
                st.success("Yay! You're my Galentine forever! 💕✨") 
                st.rerun()

        with col2:
            if st.button("No😒, I can't"):
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
