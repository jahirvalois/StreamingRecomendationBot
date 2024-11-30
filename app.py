import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API endpoint and authentication token from environment variables
API_URL = os.getenv("API_ENDPOINT")
API_TOKEN = os.getenv("API_TOKEN")

# Create a Streamlit app title
st.title("Streaming Platform Recommendation Assistant")

# Create a text input field
user_input = st.text_input("What's your favorite genre or movie/TV show?")

# Create a button to send the request
if st.button("Get Recommendations"):
    # Send the request to your API
    response = requests.post(
        API_URL,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_TOKEN}"},
        json={"input_value": user_input, "output_type": "chat", "input_type": "chat"}
    )

    # Check if the response was successful
    if response.status_code == 200:
        # Get the response data
        data = response.json()

        # Extract the message from the response
        message = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]

        # Display the message in a more user-friendly format
        st.write(f"**AI:** {message}")

        # Add a text input field to respond to the AI
        response_input = st.text_input("Your response:")

        # Create a button to send the response
        if st.button("Send"):
            # Send the response to the API
            response = requests.post(
                API_URL,
                headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_TOKEN}"},
                json={"input_value": response_input, "output_type": "chat", "input_type": "chat"}
            )

            # Check if the response was successful
            if response.status_code == 200:
                # Get the response data
                data = response.json()

                # Extract the message from the response
                message = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]

                # Display the message in a more user-friendly format
                st.write(f"**AI:** {message}")