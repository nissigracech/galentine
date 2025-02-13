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

# Create two main columns
col1, col2 = st.columns([1, 1])  # col1 for buttons, col2 empty

# Place buttons inside sub-columns within col1
with col1:
    sub_col1, sub_col2 = st.columns(2)

    # "Yes" button
    with sub_col1:
        if st.button("Yes🥹🥹, I will", key="yes"):
            st.session_state.accepted = True
            st.session_state.declined = False
            st.balloons()

    # "No" button
    with sub_col2:
        if st.button("No😒, I can't", key="no"):
            st.session_state.declined = True
            st.session_state.accepted = False  # Ensure no conflict

# col2 is intentionally left empty

# Show success message if "Yes" is clicked
if st.session_state.accepted:
    st.success("Yay! You're my Galentine forever! 💕✨")  

# Show "Think Again" prompt if "No" is clicked
if st.session_state.declined and not st.session_state.accepted:
    st.subheader("You can't escape! Think again! 😜💖")

    with col1:
        sub_col1, sub_col2 = st.columns(2)

        with sub_col1:
            if st.button("😒 No 😒", key="no_again"):
                st.rerun()  # Forces rerun without resetting session state

        with sub_col2:
            if st.button("🤔 Think Again 🤔", key="think_again"):
                st.session_state.declined = False  # Reset declined
                st.rerun()
