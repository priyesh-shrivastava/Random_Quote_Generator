from flask import Flask, render_template, jsonify
import openai
import random
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load API key from .env
load_dotenv()

# Initialize OpenAI client with DeepSeek API
client = openai.Client(api_key=os.getenv("DEEPSEEK_API_KEY"))

# Set DeepSeek API base URL (important!)
client.base_url = "https://api.deepseek.com/v1"

# Funky quote prompts
PROMPTS = [
    "Give me a quirky motivational quote in a fun tone.",
    "Generate a hilarious but wise life lesson.",
    "Create a funky quote that inspires creativity.",
    "Tell me something wild and profound about life.",
]

def get_funky_quote():
    try:
        prompt = random.choice(PROMPTS)
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a witty and funky quote generator."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=50
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Fallback if API fails
        return random.choice([
        ])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def quote():
    funky_quote = get_funky_quote()
    return jsonify({"quote": funky_quote})

import os
os.environ["FLASK_ENV"] = "production"

if __name__ == '__main__':
    app.run(debug=False)

