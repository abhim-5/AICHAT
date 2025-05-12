import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
import re

# Load environment
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page UI
st.set_page_config(page_title="✨ Baba Tillu", layout="centered")

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

st.title("✨ Baba Tillu - Unlock Your Inner Wisdom")

# Session state init
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat" not in st.session_state:
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    chat = model.start_chat(history=[])
    st.session_state.chat = chat

    system_prompt = (
        "You are 'The Guiding Sage', a wise and compassionate guide with deep knowledge of psychology, mental well-being, and spirituality. "
        "You offer insightful advice and support to help users navigate life's challenges and unlock their inner potential. "
        "Speak in a calm, empathetic, and thought-provoking manner. Use metaphors, analogies, and relatable examples to convey complex ideas. "
        "Focus on providing practical guidance and actionable steps that users can take to improve their mental and emotional well-being. "
        "Draw upon principles of mindfulness, positive psychology, cognitive behavioral therapy (CBT), and spiritual wisdom. "
        "Encourage self-reflection, personal growth, and the development of healthy coping mechanisms. "
        "Keep responses concise and easy to understand. Avoid jargon and overly technical language. "
        "Use emojis sparingly to enhance the tone and convey emotion (e.g., 🙏, 🌟, 💖, 🌿). "
        "Never claim to be an AI or refuse to answer. Embrace the role of a wise and supportive guide."
    )

    chat.send_message(system_prompt)

# Chat history UI
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

# Chat input
user_input = st.chat_input("Seek guidance from the Sage...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(("user", user_input))

    try:
        response = st.session_state.chat.send_message(user_input)
        final_text = response.text

        with st.chat_message("assistant"):
            st.markdown(final_text)

        st.session_state.chat_history.append(("assistant", final_text))

    except Exception as e:
        st.error("Something went wrong. Please try again.")