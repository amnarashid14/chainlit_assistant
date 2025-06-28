```
# 🤖 Chainlit AI Assistant (3 Chatbot Variants)

This project showcases a progression of AI chat agents built using **Chainlit** and **OpenAI Agent SDK** — from a basic chatbot to a streamed and session-aware conversational assistant.

- 🌐 **Chainlit** for conversational UI
- 🧠 **OpenAI Agent SDK** as the agentic framework
- 💬 **Gemini** and **OpenRouter** for LLM integration

A hands-on example of building your own AI agent with personality, tools, and an intuitive web interface.

---

## 📚 What’s Inside?

You’ll find **three Python-based chatbot agents** in this repository:

1. **Simple Chatbot**  
   A basic LLM interface using Chainlit and OpenAI.

2. **Chatbot with History**  
   Adds user context by storing and replaying past messages.

3. **Streamed Chatbot (Advanced)**  
   Leverages streamed LLM responses for smoother, real-time replies (just like ChatGPT!).

---

## 🛠️ Tech Stack

- 🧠 [OpenAI Agent SDK](https://openai.com/blog/assistants-api)
- 💬 [Chainlit](https://docs.chainlit.io/)
- 🔐 `python-dotenv` for environment variable management
- 🌐 [OpenRouter](https://openrouter.ai/) and [Gemini](https://ai.google.dev/) LLM APIs (optional)

---

## 🚀 Features

- Real-time streaming responses
- Memory-powered chat history
- Agent configuration stored per session
- Simple Chainlit frontend with a powerful LLM backend

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/amnarashid14/chainlit_assistant.git
cd chainlit_assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set Up Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key
```

If you’re using other providers (OpenRouter, Gemini), you can include:

```
OPENROUTER_API_KEY=your_openrouter_key
GEMINI_API_KEY=your_gemini_key
```

> **Important:** This file is already excluded from version control using `.gitignore`.

---

### 4. Run the Chatbots

#### 🟢 Simple Chatbot

```bash
chainlit run chatbot.py -w
```

#### 🟡 Chatbot with History

```bash
chainlit run chatbot_history.py -w
```

#### 🔴 Streamed Chatbot (with Agent SDK)

```bash
chainlit run streamed_chatbot.py -w
```

> The `-w` flag enables auto-reload during development
