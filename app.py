import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API endpoint and authentication token from environment variables
API_URL = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_TOKEN")

# Streamlit app setup
st.title("🎥 Streaming Platform Recommendation Assistant 🎬🍿")
st.write("Ask for movie or series recommendations across Netflix, HBO Max, and Paramount Plus!")

# Create a text input field for the user to enter their message
user_message = st.text_input("Enter your message")

# Create a button to send the message to the backend API
if st.button("Send"):
    # Send the user's message to the backend API
    # Replace the URL with your actual API endpoint
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "input_value": user_message,
        "output_type": "chat",
        "input_type": "chat",
        # Add any other required parameters here
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)

        # Display the response from the backend API
        if response.status_code == 200:
            # Get the response message
            data = response.json()
            ai_message = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.write("AI Response:")
            st.write(ai_message)

            # Keep the conversation history
            if 'conversation_history' not in st.session_state:
                st.session_state.conversation_history = []
            st.session_state.conversation_history.append({"user": user_message, "ai": ai_message})
            st.write("Conversation History:")
            for i, message in enumerate(st.session_state.conversation_history):
                st.write(f"**Turn {i+1}**")
                st.write(f"User: {message['user']}")
                st.write(f"AI: {message['ai']}")
                st.write("")
    except Exception as e:
        st.error(f"Error sending message to the backend API: {e}")