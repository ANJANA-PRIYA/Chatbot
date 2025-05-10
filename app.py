import streamlit as st
import google.generativeai as genai

# Set Streamlit page config
st.set_page_config(page_title="Gemini Chat App", layout="centered")

# Gemini API configuration
GOOGLE_API_KEY = "AIzaSyD9qMcPLvmDJOZzjBueOL17_f0EuhJgl64"
genai.configure(api_key=GOOGLE_API_KEY)

# Load the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# Title and styling
st.markdown("<h2 style='text-align: center; color: white; background-color: #007bff; padding: 1rem;'>AI CHATBOT</h2>", unsafe_allow_html=True)

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"<div style='background-color:#007bff;color:white;padding:10px;border-radius:5px;margin:5px;text-align:right;width:fit-content;margin-left:auto;'>{message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color:#e2e3e5;color:black;padding:10px;border-radius:5px;margin:5px;text-align:left;width:fit-content;margin-right:auto;'>{message['content']}</div>", unsafe_allow_html=True)

# User input box
user_input = st.text_input("Type your message here...", key="user_input")

if st.button("Send") and user_input:
    # Store and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # Get response from Gemini
        bot_response = chat.send_message(user_input).text
        st.session_state.messages.append({"role": "bot", "content": bot_response})
    except Exception as e:
        st.session_state.messages.append({"role": "bot", "content": f"⚠️ Error: {e}"})

    st.experimental_rerun()  # Refresh to display new messages
