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

# Session state initialization
if 'step' not in st.session_state:
    st.session_state.step = "ask_permission"
if 'declined' not in st.session_state:
    st.session_state.declined = False
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# Step 1: Asking for permission to ask something
if st.session_state.step == "ask_permission":
    st.subheader("I want to ask you something! 😏")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Yes, go ahead!", key="ask_yes"):
            st.session_state.step = "main_question"
            st.rerun()
    with col2:
        if st.button("No, don't ask!", key="ask_no"):
            st.session_state.step = "force_question"
            st.rerun()

# Step 2: If they say no, still proceed with fun message
if st.session_state.step == "force_question":
    st.subheader("How dare you stop me from asking? 😤 Anyway, I'll ask what I want! 😂")
    st.session_state.step = "main_question"
    

# Step 3: Main Galentine's Day question
if st.session_state.step == "main_question":
    st.header("On this Day, I want to ask you something")
    st.subheader("Will you be my Galentine 🥰💌?")
    st.image("gal.jpg", width=300)

    if not st.session_state.accepted and not st.session_state.declined:
        col1, col2 = st.columns([1, 1])
        with col1:
            sub_col1, sub_col2 = st.columns(2)
            with sub_col1:
                if st.button("Yes🥹🥹, I will", key="yes"):
                    st.session_state.accepted = True
                    st.session_state.declined = False
                    st.session_state.step = "letter"
                    st.rerun()
            with sub_col2:
                if st.button("No😒, I can't", key="no"):
                    st.session_state.declined = True
                    st.session_state.accepted = False
                    st.rerun()

    if st.session_state.accepted:
        st.session_state.step = "letter"
        st.rerun()
    
    if st.session_state.declined:
        st.subheader("You can't escape! Think again! 😜💖")
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("😒 No 😒", key="no_again"):
                st.rerun()
        with col2:
            if st.button("🤔 Think Again 🤔", key="think_again"):
                st.session_state.declined = False
                st.rerun()

# Step 4: Special Letter after "Yes"
if st.session_state.step == "letter":
    st.title("💖 Happy Galentine's Day! 💖") 
    st.write(
        "Dear frndduuu,\n\n"
        "On this beautiful Galentine's Day, I just want to remind you how amazing you are! "
        "You're my greatest friend, and someone who makes life so much brighter just by existing. "
        "Thank you for always being there, for laughing with me, and for being such a wonderful soul. 💕\n\n"
        "Let's celebrate our friendship today and always! 🥂✨\n\n"
        "With love,\n"
        "Your Favorite Person 😉"
    )
    st.image("th (2).jpeg", width=400)