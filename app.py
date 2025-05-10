import streamlit as st
import google.generativeai as genai

# Set page config
st.set_page_config(page_title="Gemini Chat App", layout="centered")

# Configure Gemini API key
GOOGLE_API_KEY = "AIzaSyD9qMcPLvmDJOZzjBueOL17_f0EuhJgl64"  # Replace with your own key in real usage
genai.configure(api_key=GOOGLE_API_KEY)

# Load the model and start a chat
if "chat" not in st.session_state:
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []

# Title bar
st.markdown("<h2 style='text-align: center; color: white; background-color: #007bff; padding: 1rem;'>AI CHATBOT</h2>", unsafe_allow_html=True)

# Show previous messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"<div style='background-color:#007bff;color:white;padding:10px;border-radius:5px;margin:5px;text-align:right;width:fit-content;margin-left:auto;'>{message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color:#e2e3e5;color:black;padding:10px;border-radius:5px;margin:5px;text-align:left;width:fit-content;margin-right:auto;'>{message['content']}</div>", unsafe_allow_html=True)

# User input box
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = st.session_state.chat.send_message(user_input).text
        st.session_state.messages.append({"role": "bot", "content": response})
    except Exception as e:
        st.session_state.messages.append({"role": "bot", "content": f"⚠️ Error: {str(e)}"})
