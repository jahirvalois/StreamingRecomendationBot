# Streaming Platform Recommendation Assistant

## Overview

This project is a chat-based recommendation assistant for streaming platforms. It uses **LangFlow API** for natural language processing and **OpenAI** algorithms to provide personalized recommendations for movies and TV shows on popular streaming platforms such as Netflix, Paramount Plus, and HBO Max.

## Features

- **Chat-based interface**: Interact with the assistant using a conversational interface.
- **Personalized recommendations**: Get tailored recommendations based on your interests and preferences.
- **Multi-platform support**: Get recommendations for movies and TV shows on multiple streaming platforms, including Netflix, Paramount Plus, and HBO Max.
- **Natural language processing**: The assistant uses OpenAI and NLP to understand your inputs and provide relevant recommendations.

## Requirements

- **Python 3.11+**: The project uses Python 3.11 or later.
- **Streamlit**: The project uses Streamlit for the chat-based interface.
- **DataStax API token**: You need to obtain an API token from the LangFlow API to use this project.
- **DataStax API Endpoint**: You need to obtain an API Endpoint from the LangFlow API to use this project.

## Installation

1. **Create Conda environment with Python**: `conda create --name <env_name> python=3.11`
2. **Activate the environment**: `conda activate <env_name>`
3. **Install the required dependencies**: `pip install -r requirements.txt`
4. **Navigate to the repository directory**: `cd your-repo-name`
5. **create `.env` file in root folder and add the `API_TOKEN` and `API_ENDPOINT` variable to use with `app.py` file**.
6. **Run the application**: `streamlit run app.py`

## Usage

1. **Open the application in your web browser**: `http://localhost:8501`
2. **Interact with the assistant using the chat-based interface**.
3. **Provide your inputs and preferences to get personalized recommendations**.

## Acknowledgments

This project uses the **LangFlow API** for natural language processing and **OpenAI**. Thank you to the LangFlow team for providing this API.