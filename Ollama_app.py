from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

# Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = "Simple Q&A Chatbot with Ollama"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpfull assistant, answer the questions to the best of your knowledge"),
        ("user", "Question:{question}")
    ]
)

def generate_answer(question, engine, temperature, max_token):
    llm = Ollama(model=engine)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({'question':question})
    return answer

# Title of the app
st.title("Q&A ChatBot using OpenAI")


# Drop down to select various Open AI models
engine = st.sidebar.selectbox("Select an Open Source Model", ["llama2"])

# Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_token = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main Interface for user
st.write("GO ahead and ask any question")
user_input = st.text_input("You: ")

if user_input:
    response = generate_answer(user_input, engine, temperature, max_token)
    st.write(response)
else:
    st.write("Please provide a query")