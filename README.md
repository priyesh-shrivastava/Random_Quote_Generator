# 🎤 Funky Quote Generator

Unleash your inner funk with this **Funky Quote Generator**—a Flask-powered app that dishes out the freshest, quirkiest, and most creative quotes! Whether powered by AI or our secret stash of funky phrases, this app keeps the vibes groovy. 🕺✨

## 📌 Features

- 🔮 **AI-Powered Quotes**: Uses cutting-edge AI (DeepSeek API) to generate funky and unique quotes.
- 🔥 **Fallback Quotes**: No API? No problem! We’ve got a stash of funky lines ready to roll.
- 🎨 **Stylish Interface**: A playful, designer look to match the funky spirit.
- 🚀 **Fast & Fun**: Built with Flask for quick and easy deployment.

## 🛠️ Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/Funky-Quote-Generator.git
cd Funky-Quote-Generator
```

2. **Set up a virtual environment** (optional but recommended):

```bash
python -m venv venv
# Activate it:
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Set up your API key**:

- Sign up at [DeepSeek](https://deepseek.com) and get your API key.
- Create a `.env` file in the project directory:

```bash
touch .env
```

Add this inside `.env`:

```
DEEPSEEK_API_KEY=your_api_key_here
```

## ▶️ Running the App

```bash
python app.py
```

Visit `http://localhost:5000` and get your daily dose of funk! 🎷

## 📤 Deployment

For production, use a WSGI server like **Gunicorn**:

```bash
pip install gunicorn
gunicorn app:app
```

## 🤖 API-Free Mode

If you run out of API quota, the app will gracefully fall back to pre-defined funky quotes.

## 📚 Example Quote

> "Life’s too short for boring quotes – stay funky!"

## 🧡 Contributing

Feel the funk? Open a pull request and add your favorite funky quotes!

## 📜 License

MIT License – because funk should be free! 🎶

