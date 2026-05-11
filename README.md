# 🧵 AI Fabric Stylist

✨ AI-powered fashion assistant for fabric recommendations, outfit styling, and fashion consultation using Gemini API and Large Language Models (LLM).

---

## 🌟 Overview

AI Fabric Stylist is an interactive AI fashion chatbot designed to help users with:

* 👕 Recommending the best fabric materials
* 🧥 Providing outfit inspiration
* 🧵 Explaining fabric characteristics
* 💡 Giving fashion and fabric care tips
* 🤖 Answering fashion-related questions naturally using AI

This project uses:

* **Google Gemini API (LLM)**
* **Streamlit** as an interactive frontend
* **Simple RAG** implementation using an internal fabric dataset
* **Conversational Memory** to understand previous chat context
---

# ✨ Main Features

## 🤖 AI Fashion Chatbot

Interactive LLM-based fashion chatbot capable of understanding natural language.

## 🧵 Fabric Recommendation System

Provides fabric recommendations based on user needs and fashion context.

## 📚 Simple RAG (Retrieval-Augmented Generation)

Uses an internal dataset (`fabric_dataset.csv`) to provide more relevant responses.

## 🧠 Conversation Memory

The chatbot can understand previous conversation context.

## 🎨 Modern UI Design

Built with a modern and clean custom Streamlit UI.

## 🌐 Public Access

Can be accessed publicly using ngrok deployment.

---

# 🛠️ Tech Stack

| Technology        | Description                   |
| ----------------- | ----------------------------- |
| Python            | Main programming language     |
| Streamlit         | Interactive web app framework |
| Google Gemini API | Large Language Model          |
| Pandas            | Dataset processing            |
| Ngrok             | Public deployment tunnel      |

---

# 📂 Project Structure

```bash
ai-fabric-chatbot/
│
├── app.py
├── fabric_dataset.csv
├── test_gemini.py
├── google.py
└── README.md
```

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/silvyph/ai-fabric-chatbot.git
cd ai-fabric-chatbot
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install streamlit
pip install google-generativeai
pip install pandas
```

---

## 4️⃣ Configure Gemini API

Open file `app.py`

Replace:

```python
genai.configure(api_key="YOUR_API_KEY")
```

With your own Gemini API Key.

📌 Get API Key:

[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Open browser:

```bash
http://localhost:8501
```

---

# 🌍 Public Deployment with Ngrok

```bash
ngrok http 8501
```

Ngrok will generate a public URL such as:

```bash
https://xxxx.ngrok-free.app
```

---

# 💬 Example Questions

* "Bahan adem untuk kemeja kantor"
* "Kain terbaik untuk hoodie"
* "Tips perawatan chiffon"
* "Outfit linen cocok dipadukan dengan apa?"
* "Bahan premium untuk dress"

---

# 🧠 AI Concepts Used

This project implements:

* Large Language Model (LLM)
* Natural Language Processing (NLP)
* Retrieval-Augmented Generation (RAG)
* Conversational AI
* Prompt Engineering

---

# 📸 User Interface Preview

## 🏠 Main Interface

* Modern fashion-themed UI
* Interactive chatbot bubbles
* Fashion category cards
* Sidebar customization

## ✨ Features Preview

* AI outfit recommendation
* Fabric explanation
* Fashion consultation
* Conversational context memory

---

# 🎯 Final Project Objective

This project was developed as a Final Project for:

> LLM-Based Tools and Gemini API Integration for Data Scientists

organized by **Hacktiv8** as part of the AI learning and training program.

The project focuses on building an interactive AI chatbot using:

* Large Language Models (LLM)
* Natural Language Processing (NLP)
* Gemini API Integration
* Retrieval-Augmented Generation (RAG)

with a real-world use case in fashion and fabric recommendation systems.

---

# 👩‍💻 Author

**Silvy Putri**

AI Fabric Stylist Project ✨

---

# ⭐ Notes

* Use your own Gemini API Key.
* Gemini API free tier has usage quota limitations.
* Make sure your internet connection is active while running the chatbot.

---

# ❤️ Thank You

Thank you for visiting this project.

If you find this project interesting, feel free to give this repository a ⭐ on GitHub.

---

# 📌 Training Program

This project was created during the:

**LLM-Based Tools and Gemini API Integration for Data Scientists**

conducted by **Hacktiv8** under the AI Opportunity Fund program.

The training focused on:

* AI application development
* Gemini API integration
* NLP and LLM implementation
* Conversational AI systems
* AI-powered recommendation systems
