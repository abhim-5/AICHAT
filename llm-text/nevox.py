from dotenv import load_dotenv
import streamlit as st
import os
import time
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page config with dark theme
st.set_page_config(
    page_title="Nevox AI",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom dark theme
st.markdown("""
    <style>
        body {
            background-color: #000;
            color: white;
        }
            .stButton {
            display: flex;
            justify-content: center;}
        .stButton>button {
            background-color: #6c63ff;
            color: white;
        }
    
        .st-emotion-cache-h4xjwg {
            position: fixed;
            top: 0px;
            left: 0px;
            right: 0px;
            height: 3.75rem;
            background: rgb(14, 17, 23);
            outline: none;
            z-index: 999990;
            display: none;
        }
        .st-emotion-cache-1d2o6qs {
            width: 100%;
            padding: 0.5rem 1rem 1rem;
            max-width: 736px;
        }
            .st-emotion-cache-seewz2 h1 {
            color : cyan;
            text-align : center;
     word-spacing: 1.5rem;
            letter-spacing: .25rem;
                font-size: 2.75rem;
    font-weight: 700;
    padding: .25rem 0px 1rem;
            
}
    </style>
""", unsafe_allow_html=True)

st.title("Nevox is here for you!")

# Buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        st.session_state.chat = model.start_chat(history=[])
        st.rerun()

with col2:
    if st.button("⬇️ Download Chat"):
        if "chat_history" in st.session_state:
            chat_log = ""
            for role, msg in st.session_state.chat_history:
                chat_log += f"{role.upper()}:\n{msg}\n\n"
            st.download_button(
                label="📄 Save Chat as .txt",
                data=chat_log,
                file_name="chat_history.txt",
                mime="text/plain"
            )

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chat" not in st.session_state:
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    st.session_state.chat = model.start_chat(history=[])

# Show history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# Chat input
user_input = st.chat_input("Type your message...")

# Process input
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(("user", user_input))

    time.sleep(0.5)  # Delay to reduce overload

    try:
        response = st.session_state.chat.send_message(user_input, stream=True)
        full_response = ""
        for chunk in response:
            full_response += chunk.text

        with st.chat_message("assistant"):
            st.markdown(full_response)

        st.session_state.chat_history.append(("assistant", full_response))

    except Exception as e:
        # Show error message and clear memory
        st.error("⚠️ Memory full. Clearing chat and restarting...")

        # Wait before resetting
        time.sleep(3)

        # Clear chat memory and restart model
        st.session_state.chat_history = []
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        st.session_state.chat = model.start_chat(history=[])

        # Rerun the app
        st.rerun()
