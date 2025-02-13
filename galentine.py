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
st.image("gal.jpg", width=300)  # Adjusted image size

# Session state to handle button clicks
if 'declined' not in st.session_state:
    st.session_state.declined = False
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# Buttons
yes_button = st.button("Yes🥹🥹, I will")
no_button = st.button("No😒, I can't")

# Handling button clicks
if yes_button:
    st.session_state.accepted = True
    st.balloons()
    st.success("Yay! You're my Galentine forever! 💕✨")

if no_button:
    st.session_state.declined = True

# Loop if "No" is clicked
while st.session_state.declined and not st.session_state.accepted:
    st.subheader("You can't escape! Think again! 😜💖")
    
    no_again = st.button("😒 No 😒")
    think_again = st.button("🤔 Think Again 🤔")

    if think_again:
        st.session_state.declined = False

    if no_again:
        st.session_state.declined = True  # Keeps looping
