import streamlit as st
import os
import sys

# Ensure the current working directory is set correctly
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
os.sys.path.insert(0, parent_dir)

# Add the 'app' directory to the system path
sys.path.append(os.path.join(parent_dir, 'app'))

# Now import the utilities
from utils import load_data, get_pronunciation, generate_example_sentence, generate_image

# Paths for data and assets
data_path = os.path.join(current_dir, 'data', 'jlpt_n3_words.csv')
assets_path = os.path.join(current_dir, 'assets')
models_path = os.path.join(parent_dir, 'models')

# Load JLPT N3 data
df = load_data(data_path)

# Streamlit app layout
st.title('JLPT Learning App')
st.write('Memorize words with sentence examples, pronunciation, and pictures.')

# Randomly select a word
try:
    word_data = df.sample(1).iloc[0]
    japanese = word_data['japanese']
    kana = word_data['kana']
    english = word_data['english']
    alt_meaning = word_data['alt meaning']
    tags = word_data['tags']

    st.write(f"**Kanji:** {japanese}")
    st.write(f"**Hiragana:** {kana}")
    st.write(f"**Meaning:** {english}")
    st.write(f"**Alternative Meanings:** {alt_meaning}")
    st.write(f"**Tags:** {tags}")

    example_sentence = generate_example_sentence(japanese)
    st.write(f"**Example Sentence:** {example_sentence}")

    if st.button('Get Pronunciation'):
        pronunciation_path = os.path.join(current_dir, 'assets', 'pronunciation.mp3')
        get_pronunciation(example_sentence, save_path=pronunciation_path)
        audio_file = open(pronunciation_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    if st.button('Get Image'):
        image_prompt = f"An illustration of the sentence: {example_sentence}"
        image = generate_image(image_prompt)
        st.image(image, caption=f'Image for the sentence: {example_sentence}')

except Exception as e:
    st.error(f"An error occurred: {e}")
