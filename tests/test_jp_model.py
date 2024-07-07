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
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path).to("cuda")
        model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16).to("cuda")
    
    generator = pipeline(
        'text-generation', 
        model=model, 
        tokenizer=tokenizer, 
        device_map="auto"
    )


    prompt = f"""'{word}' を使って、JLPT N3レベルの日本語の例文を作成してください。結果をJSON形式で返してください。
    
    例えば:

    {{
    "言葉": "車",
    "ひらがな": "くるま",
    "例文": [
        {
            "文": "彼（かれ）は新（あたら）しい車（くるま）を買（か）いました。",
            "英語": "He bought a new car."
        },
        {
            "文": "車（くるま）が壊（こわ）れたので修理（しゅうり）に出（だ）しました。",
            "英語": "I took my car to the repair shop because it broke down."
        },
        {
            "文": "この車（くるま）は燃費（ねんぴ）が良（よ）くて経済的（けいざいてき）だ。",
            "英語": "This car has good fuel efficiency and is economical."
        }
    ]
    }}
    """

    result = generator(
        prompt, 
        max_length=1000, 
        max_new_tokens=256,
        num_return_sequences=1
    )
    
    generated_text = result[0]['generated_text']  
    print("Question:", word)
    print("Answer:", generated_text)
    
    return generated_text

if __name__ == '__main__':
    word = '飛行機'
    output = generate_example_sentence(word)
    print(output)
