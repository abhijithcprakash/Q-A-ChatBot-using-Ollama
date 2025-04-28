
---

# 🧠 Simple Q&A Chatbot with Ollama and Streamlit

This project is a **Q&A Chatbot** built using **LangChain**, **Streamlit**, and an **Open Source LLM model** served via **Ollama**.  
The chatbot answers your questions to the best of its knowledge using a selected open-source model (e.g., `llama2`).

---

## 🚀 Features

- **Interactive** web UI using **Streamlit**.
- **Customizable** model parameters: `temperature` and `max_tokens`.
- Uses **LangChain** for prompt management and chaining.
- **Ollama** backend for hosting the LLM locally.
- **LangSmith** tracking integration.

---

## 🛠️ Setup Instructions

Follow these steps carefully to set up and run the project:

### 1. Install Ollama

You must install **Ollama** first, as it is responsible for running the open-source LLM models locally.

- Visit [Ollama's official website](https://ollama.ai/) and download the installer for your operating system.
- Follow their installation guide to set it up properly.

### 2. Pull the Required Model

Once Ollama is installed, you need to pull the specific model you'll be using (e.g., `llama2`):

```bash
ollama pull llama2
```

Make sure the model pull completes successfully.

### 3. Clone this Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

> Replace `your-username` and `your-repo-name` with your actual GitHub username and repo.

### 4. Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
```

### 5. Install Project Dependencies

Install all required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 6. Set Up Environment Variables

Create a `.env` file in the root of the project and add the following:

```bash
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

If you don't have a **LangSmith** account or API key, you can create a free account at [LangSmith](https://smith.langchain.com/).

---

## 🧠 Running the App

Start the **Streamlit** application with the following command:

```bash
streamlit run app.py
```

(Assuming your main file is named `app.py`; rename accordingly if different.)

The Streamlit app will open automatically in your default web browser at `http://localhost:8501`.

---

## 🎯 Usage

- Use the sidebar to:
  - Select your model (currently `llama2`).
  - Adjust the temperature for creativity.
  - Set the maximum token limit for responses.

- Type your question in the input box and receive an answer from the chatbot!

---

## 📝 Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Ollama** (for LLM inference)
- **LangSmith** (for tracing)

---

## 📌 Notes

- Ensure Ollama is running while you use the Streamlit app.
- Make sure you have enough resources to run the selected model (RAM, VRAM, CPU).
- You can customize the models and prompts according to your needs.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---
