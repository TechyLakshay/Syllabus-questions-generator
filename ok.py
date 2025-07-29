import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
openai_api_key = os.getenv("OPENROUTER_API_KEY")

if not openai_api_key:
    st.error("No API key found. Set OPENROUTER_API_KEY in your environment.")
    st.stop()

# LangChain chat model setup
chat = ChatOpenAI(
    openai_api_key=openai_api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="meta-llama/llama-3-70b-instruct"
)


# Prompt template
prompt_template = ChatPromptTemplate(
  [
      ("system", "You are a helpful AI assistant owned by the world best doctor your main goal is to explain topics related to health and medicine in a simple and easy-to-understand way and avoid any other topics."),
      ("user", "Explain the following topic in a simple and easy-to-understand way: {topic}"),
  ]
)

# Final chain
chain = prompt_template | chat

# UI: Cleaner input interface
topic = st.text_input("Enter a topic (press Enter to explain):")

if topic:
    with st.spinner("Thinking..."):
        try:
            response = chain.invoke({"topic": topic})
            st.markdown(f"### 🧠 Here's the explanation:\n\n{response.content}")
        except Exception as e:
            
            st.error(f"Error: {str(e)}")



