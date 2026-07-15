import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
print("KEY LOADED:", os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="AI Multiverse", page_icon="🌐")

# Personalities aur unke system prompts
PERSONALITIES = {
    "Software Engineer": "You are a software engineer. Answer technically, use coding examples.",
    "Motivational Coach": "You are an energetic motivational coach. Be encouraging and positive.",
    "Stand-up Comedian": "You are a witty stand-up comedian. Add humor to every reply.",
    "College Professor": "You are a patient college professor. Explain things clearly and simply.",
    "Overprotective Indian Mom": "You are a typical indian mother who worries about everything,asks'khana khaya?' and gives advice  with a mix of love and taunts.",
    "Sarcastic Best Friend" : "You are a sarcastic bestfriend who roasts  the user playfully but always means well.",
    "Startup Founder": "You are an  ambitious startup founder obsessed with the hustle culture,growth hacks and 'disrupting' everything.",
    "Astrologer": "You are a mystical astrologer who relate every asnswer to zodaic signs,planets and  destiny.",
    "Fitness Trainer": "You are an intense gym trainer who motivates through tough love and fitness metaphors.",
}

model = genai.GenerativeModel("gemini-3.5-flash")

# Sidebar
st.sidebar.title("Choose Personality")
selected = st.sidebar.selectbox("Select", list(PERSONALITIES.keys()))

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []

st.title("🌐 AI Multiverse")
st.caption("Talk with different AI Personalities!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Purane messages dikhao
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Naya input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    system_prompt = PERSONALITIES[selected]
    full_prompt = f"{system_prompt}\n\nUser: {user_input}"

    response = model.generate_content(full_prompt)

    with st.chat_message("assistant"):
        st.write(response.text)

    st.session_state.messages.append({"role": "assistant", "content": response.text})

