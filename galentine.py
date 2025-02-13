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
st.header("On this Galentine's Day, I want to ask you something")
st.subheader("Will you be my Galentine 🥰💌?")
st.image("gal.jpg", width=300)

# Session state initialization
if 'declined' not in st.session_state:
    st.session_state.declined = False
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

if not st.session_state.accepted and not st.session_state.declined:
    # First set of buttons (shown initially)
    col1, col2 = st.columns([1, 1])  # col1 for buttons, col2 empty
    with col1:
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            if st.button("Yes🥹🥹, I will", key="yes"):
                st.session_state.accepted = True
                st.session_state.declined = False
                st.balloons()
        with sub_col2:
            if st.button("No😒, I can't", key="no"):
                st.session_state.declined = True
                st.session_state.accepted = False
                st.rerun()

if st.session_state.accepted:
    st.success("Yay! You're my Galentine forever! 💕✨")

if st.session_state.declined and not st.session_state.accepted:
    # Show "You can't escape!" message first
    st.subheader("You can't escape! Think again! 😜💖")

    # Second set of buttons (after clicking "No")
    col1, col2 = st.columns([1, 1])  # Same layout
    with col1:
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            if st.button("😒 No 😒", key="no_again"):
                st.rerun()
        with sub_col2:
            if st.button("🤔 Think Again 🤔", key="think_again"):
                st.session_state.declined = False
                st.rerun()
