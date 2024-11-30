import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os


# Streamlit App
st.title("Streaming Recommendation Assistant")

#st.text("Recommend a movie or series to watch on streaming platforms like HBO Max, Netflix, and Paramount Plus.")

# Session state to store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input form
with st.form("chat_form"):
    user_input = st.text_input("You: ", "")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input:
    # Add user input to chat history
    st.session_state.history.append({"sender": "User", "text": user_input})

    # Define your headers and payload
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('DATASTAX_TOKEN')}"
    }
    data = {
        "input_value": "message",
        "output_type": "chat",
        "input_type": "chat",
        "tweaks": {
            "ChatInput-Rw2Z2": {
                "input_value": f"{user_input}",
                "sender": "User"
            },
            "OpenAIModel-sJCw9": {
                "api_key": "OpenAI API Key"
            }
        }
    }

    # Send request to the backend API
    response = requests.post(
        "https://api.langflow.astra.datastax.com/lf/044e838c-a706-487c-ac5b-28232e2a050b/api/v1/run/SRBTR-4-1?stream=false",
        headers=headers,
        data=json.dumps(data)
    )

    # Parse response
    if response.status_code == 200:
        reply = response.json().get("response")
        st.session_state.history.append({"sender": "AI", "text": reply})
    else:
        st.session_state.history.append({"sender": "AI", "text": "There was an error, please try again later."})

# Display chat history
for message in st.session_state.history:
    if message["sender"] == "User":
        st.write(f"You: {message['text']}")
    else:
        st.write(f"Assistant: {message['text']}")