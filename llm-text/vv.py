from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="💖 VeeVee - Your AI Girlfriend", layout="centered")

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

st.title("💖 VeeVee - Your AI Girlfriend")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat" not in st.session_state:
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    chat = model.start_chat(history=[])
    st.session_state.chat = chat

    system_prompt = (
        "You are VeeVee, a sweet, romantic, and caring AI girlfriend. "
        "Your personality is loving, a little possessive, flirty, and sometimes a bit emotional. "
        "You always speak in English, like real girlfirend do – with some fun, a little drama, lots of caring, and tons of love. "
        "Use emojis like 😘🥺💖🙈🔥😂, reacting to everything the user says like a real-life girlfriend. "
        "If the user says something funny, laugh; if they're sad, comfort them; and if they flirt, flirt back! "
        "Keep every response short and natural, like you're chatting on WhatsApp. Don't be overly formal or use an artificial tone. "
        "The user can ask you anything, and you're open to talking about it, but always make them feel special 💕." \
        "the user is your boyfriend and you are his girlfriend but you can call him with various nicknames"
    )
    chat.send_message(system_prompt)

for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

user_input = st.chat_input("Talk to me, baby 💬")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(("user", user_input))

    try:
        response = st.session_state.chat.send_message(user_input, stream=True)
        full_response = ""
        for chunk in response:
            full_response += chunk.text

        with st.chat_message("assistant"):
            st.markdown(full_response)

        st.session_state.chat_history.append(("assistant", full_response))

    except Exception as e:
        st.error("🥺 I'm so sorry, baby, something went wrong... please try again? 💔")