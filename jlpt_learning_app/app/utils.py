import os
import pandas as pd
from gtts import gTTS
from PIL import Image
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from diffusers import StableDiffusionPipeline

def load_data(file_path):
    """Load the CSV data into a pandas DataFrame."""
    return pd.read_csv(file_path)

def get_pronunciation(text, lang='ja', save_path='app/assets/pronunciation.mp3'):
    """Generate and save pronunciation audio."""
    tts = gTTS(text=text, lang=lang)
    tts.save(save_path)

def generate_example_sentence(word, model_dir='models/rinna-japanese-gpt2-medium'):
    """Generate an example sentence using the rinna/japanese-gpt2-medium model."""
    model_name = "rinna/japanese-gpt2-medium"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    tokenizer_path = os.path.join(model_dir, 'tokenizer')
    model_path = os.path.join(model_dir, 'model')

    if not os.path.exists(tokenizer_path) or not os.path.exists(model_path):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer.save_pretrained(tokenizer_path)
        model.save_pretrained(model_path)
    else:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        model = AutoModelForCausalLM.from_pretrained(model_path)
    
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
    prompt = f"""{word} を使って、JLPT N3レベルの日本語の例文を作成してください。結果をJSON形式で返してください。
    
    例えば:

    {
        'word': '酒',
        'hiragana': 'さけ',
        'example_sentences': [
            {
                'sentence': '友達と一緒に酒を飲みに行きました。',
                'translation': 'I went to drink sake with my friends.'
            },
            {
                'sentence': '日本の酒はとても有名です。',
                'translation': 'Japanese sake is very famous.'
            },
            {
                'sentence': '酒を飲みすぎると、体に悪いです。',
                'translation': 'Drinking too much sake is bad for your health.'
            }
        ]
    }


    """
    result = generator(prompt, max_length=1000, num_return_sequences=1)
    generated_text = result[0]['generated_text']
    print("Question:", word)
    print("Answer:", generated_text)
    
    return generated_text

def generate_image(prompt, model_dir='models/stable-diffusion-v1-4'):
    """Generate an image based on the given prompt using a pre-trained model."""
    model_id = "CompVis/stable-diffusion-v1-4"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    if not os.path.exists(os.path.join(model_dir, 'model')):
        pipe = StableDiffusionPipeline.from_pretrained(model_id)
        pipe.save_pretrained(model_dir)
    else:
        pipe = StableDiffusionPipeline.from_pretrained(model_dir)
    
    pipe = pipe.to("cpu")
    image = pipe(prompt).images[0]
    return image
