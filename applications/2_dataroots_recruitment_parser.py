import streamlit as st
import langchain_helper as lch
from dotenv import load_dotenv
import os

load_dotenv("openapi_key.txt")
openai_api_key = os.getenv('OPENAI_API_KEY')

st.title(":iphone: Dataroots Posts Generator")

# Sidebar select box
st.sidebar.title('Customize your post')
n_posts = st.sidebar.selectbox('How many posts:', [1, 2, 3, 4])
social_network = st.sidebar.selectbox('Select Social Network:', ['Instagram', 'LinkedIn'])
position = st.sidebar.selectbox('Select Position:', ['Machine Learning Engineer', 'Data Engineer', 'Data Strategy'])
tone = st.sidebar.selectbox('Select Tone:', ['Informal', 'Formal'])
max_words = st.sidebar.slider('Max Number of Words', min_value=100, max_value=1000, value=200, step=10)
extra_info = st.sidebar.text_area('Additional Information:', max_chars=500)

temperature = st.sidebar.slider('Model temperature', min_value=0.0, max_value=1.0, value=0.0, step=0.01)

# Generate button
if st.sidebar.button('Generate'):
    response = lch.generate_post_dataroots_with_parsing(
        openai_api_key=openai_api_key,
        temperature=temperature,
        n_posts=n_posts,
        social_network=social_network, 
        position=position, 
        tone=tone, 
        max_words=max_words,
        extra_info=extra_info
        )
    st.dataframe(response)
