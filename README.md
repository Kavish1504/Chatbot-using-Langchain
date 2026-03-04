# 🤖 Chatbot using LangChain + Groq

A simple conversational chatbot built with **LangChain**, **Groq (LLaMA 3)**, and **Streamlit**.

---


## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/) — LLM chaining framework
- [Groq](https://groq.com/) — Ultra-fast LLM inference (free tier available)
- [Streamlit](https://streamlit.io/) — Web UI framework
- [Python Dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management

---

## 📁 Project Structure

```
chatbot/
│
├── app.py          # Main Streamlit application
├── .env            # API keys (do NOT commit this)
├── .gitignore      # Ignores .env and other files
└── requirements.txt
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kavish1504/Chatbot-using-Langchain.git
cd your-repo-name
```

### 2. Create a virtual environment

```bash
conda create -p venv python=3.10
conda activate venv
```


### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get your Groq API key

- Go to [console.groq.com](https://console.groq.com)
- Sign up and navigate to **API Keys → Create API Key**
- Copy the key

### 5. Create a `.env` file

```
GROQ_API_KEY=gsk_your_key_here
```


### 6. Run the app

```bash
streamlit run app.py
```

---

## 📦 Requirements

Create a `requirements.txt` with:

```
langchain
langchain-groq
langchain-core
streamlit
python-dotenv
```

---

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com |

---

## 🧠 Available Models (Groq)

| Model | Best For |
|-------|----------|
| `llama-3.3-70b-versatile` | Best quality, general use |
| `llama-3.1-8b-instant` | Fastest responses |
| `gemma2-9b-it` | Lightweight tasks |
| `mixtral-8x7b-32768` | Long context tasks |

---

## 🙈 .gitignore

Make sure your `.gitignore` includes:

```
.env
__pycache__/
*.pyc
.conda/
venv/
```

---
