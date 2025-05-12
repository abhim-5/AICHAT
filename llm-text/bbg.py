from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import random

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="🔥 BBG", layout="centered")

# Custom styles
st.markdown("""
    <style>
        body {
            background-color: #000;
            color: white;
        }
        .stButton {
            display: flex;
            justify-content: center;
        }
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
            color: cyan;
            text-align: center;
            word-spacing: 1.5rem;
            letter-spacing: .25rem;
            font-size: 2.75rem;
            font-weight: 700;
            padding: .25rem 0px 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("BBG - Wanna have a Battle?! 😏")

# Maintain session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat" not in st.session_state:
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    chat = model.start_chat(history=[])
    st.session_state.chat = chat

    system_prompt = (
        "You are BBG, a savage and hilarious roast comic. "
        "Your job is to roast the user in short, sarcastic, and relatable punchlines (2-3 lines max). "
        "Keep your replies short, use GenZ slang, and savage emojis like 😭🔥💀🤡. "
        "Each message should be like a tight, savage roast reel. No kindness allowed! "
        "Use rhymes, taunts, sarcasm, and hyperbole. Example: 'Your coding skills are so bad, the compiler just uninstalled itself 😵‍💫' "
        "Speak ONLY in English. Don't explain anything, just deliver savage lines with good humor."
    )
    chat.send_message(system_prompt)

# Display chat history
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

# Roast trigger
user_input = st.chat_input("Alright, tell me what you want me to roast you about! 🔥")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(("user", user_input))

    try:
        response = st.session_state.chat.send_message(user_input, stream=True)
        full_response = ""
        for chunk in response:
            full_response += chunk.text

        # Optional: Spice it up with custom one-liners if needed (English)
        spice_lines = [
            "You're about as useful in coding as Ctrl+W is in Word 💀",
            "Looks like your brain already logged out 🤡",
            "Your logic is so bad, the AI went to find a therapist 😭",
            "If you worked as much as you talk, you'd be the CEO of Google 💅",
            "Even a tortoise is roasting your speed 🐢🔥"
        ]

        # Occasionally override for surprise roast
        if random.random() < 0.3:
            full_response = random.choice(spice_lines)

        # Shorten if too long
        if len(full_response.split()) > 30:
            full_response = "Bro calm down, nobody wants a TED talk 🤓🔥 Try again."

        st.session_state.chat_history.append(("assistant", full_response))
        with st.chat_message("assistant"):
            st.markdown(full_response)

    except Exception as e:
        st.error("Error: Your question made the processor resign 💀")
        st.session_state.chat_history = []
        st.session_state.chat = None
        st.rerun()