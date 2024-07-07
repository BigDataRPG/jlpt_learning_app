import transformers
import torch
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def generate_example_sentence(word, model_dir='models/rinna-llama-3-youko-8b'):
    """Generate an example sentence using the rinna/llama-3-youko-8b model."""
    model_name = "rinna/llama-3-youko-8b"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    tokenizer_path = os.path.join(model_dir, 'tokenizer')
    model_path = os.path.join(model_dir, 'model')

    if not os.path.exists(tokenizer_path) or not os.path.exists(model_path):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
        tokenizer.save_pretrained(tokenizer_path)
        model.save_pretrained(model_path)
    else:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16)
    
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer, device_map="auto")
    prompt = f"""{word} を使って、JLPT N3レベルの日本語の例文を作成してください。結果をJSON形式で返してください。
    
    例えば:

    {{
        'word': '酒',
        'hiragana': 'さけ',
        'example_sentences': [
            {{
                'sentence': '友達と一緒に酒を飲みに行きました。',
                'translation': 'I went to drink sake with my friends.'
            }},
            {{
                'sentence': '日本の酒はとても有名です。',
                'translation': 'Japanese sake is very famous.'
            }},
            {{
                'sentence': '酒を飲みすぎると、体に悪いです。',
                'translation': 'Drinking too much sake is bad for your health.'
            }}
        ]
    }}
    """

    result = generator(prompt, max_length=1000, num_return_sequences=1)
    generated_text = result[0]['generated_text']  
    print("Question:", word)
    print("Answer:", generated_text)
    
    return generated_text

if __name__ == '__main__':
    word = '車'
    output = generate_example_sentence(word)
    print(output)
