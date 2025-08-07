from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

db = FAISS.load_local("vectorstore/bangla_faiss", embedding, allow_dangerous_deserialization=True)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

def get_answer(query: str) -> str:
    return qa_chain.invoke({"query": query})["result"]

