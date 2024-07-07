import streamlit as st
import pandas as pd
from gtts import gTTS
from PIL import Image
import requests
from io import BytesIO

# Function to get pronunciation audio
def get_pronunciation(text, lang='ja'):
    tts = gTTS(text=text, lang=lang)
    tts.save('pronunciation.mp3')

# Function to get image from an API (placeholder implementation)
# def get_image(word):
#     response = requests.get(f"https://api.example.com/get_image?query={word}")
#     img = Image.open(BytesIO(response.content))
#     return img

# Example data
data = {
    'word': ['犬', '猫', '車'],
    'sentence': ['犬はかわいいです。', '猫が好きです。', '車が速いです。'],
}

df = pd.DataFrame(data)

# Streamlit app layout
st.title('JLPT Learning App')
st.write('Memorize words with sentence examples, pronunciation, and pictures.')

word = st.selectbox('Select a word', df['word'])
sentence = df[df['word'] == word]['sentence'].values[0]

st.write(f"**Word:** {word}")
st.write(f"**Sentence:** {sentence}")

if st.button('Get Pronunciation'):
    get_pronunciation(sentence)
    audio_file = open('pronunciation.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

# if st.button('Get Image'):
#     image = get_image(word)
#     st.image(image, caption=f'Image for {word}')

# Save this file as jlpt_learning_app/app.py
