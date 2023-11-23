import streamlit as st
import langchain_helper as lch
from dotenv import load_dotenv
import os

load_dotenv("openapi_key.txt")
openai_api_key = os.getenv('OPENAI_API_KEY')

st.title(":iphone: Dataroots Posts Generator")

# Sidebar select box
st.sidebar.title('Customize your post')
social_network = st.sidebar.selectbox('Select Social Network:', ['Instagram', 'LinkedIn'])
position = st.sidebar.selectbox('Select Position:', ['Machine Learning Engineer', 'Data Engineer', 'Data Strategy'])
tone = st.sidebar.selectbox('Select Tone:', ['Formal', 'Informal'])
max_words = st.sidebar.slider('Max Number of Words', min_value=100, max_value=1000, value=200)
temperature = st.sidebar.slider('Model temperature', min_value=0.0, max_value=1.0, value=0.5, step=0.01)

# Generate button
if st.sidebar.button('Generate'):
    response = lch.generate_post_dataroots(social_network, position, tone, max_words, temperature, openai_api_key)
    st.text(response['generated_post'])
