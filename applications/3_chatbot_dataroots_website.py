import streamlit as st
import langchain_helper as lch
from dotenv import load_dotenv
import os

load_dotenv("openapi_key.txt")
openai_api_key = os.getenv('OPENAI_API_KEY')

st.title(":dataroots: Dataroots website chatbot")

# Create a list to store the entered URLs persistently throughout the session
if 'url_list' not in st.session_state:
    st.session_state.url_list = []

# Function to display entered URLs
def display_urls(urls):
    st.sidebar.header("Entered URLs")
    for url in urls:
        st.sidebar.write(url)

# Display all entered URLs
display_urls(st.session_state.url_list)

# Text input for adding a new URL
new_url = st.text_input(label="url", label_visibility="hidden")

# Add URL button
if st.button("Add URL") and new_url:
    st.session_state.url_list.append(new_url)
    st.sidebar.success(f"Added: {new_url}")
    st.rerun()

# Temperature slider
temperature = st.sidebar.slider("Select temperature", min_value=0.0, max_value=1.0, value=0.0)

# User input for asking a question
user_input = st.text_area("Ask your question")

# Generate button
if st.button("Answer"):
    if st.session_state.url_list and user_input:
        response = lch.ask_dataroots_chatbot(openai_api_key, temperature, st.session_state.url_list, user_input)
        st.text_area(
            label="answer",
            value=response['answer'] + '\n' + response['sources'],
            height=200)
