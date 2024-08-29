import os
from .llm.utils import *
from langchain_community.vectorstores import Pinecone
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import OpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA

from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

GROQ_API_KEY = os.getenv('groq_api_key')
OPENAI_API_KEY = os.getenv('openai_api_key')


def process_question(user_question):
    if user_question:
        os.environ["GROQ_API_KEY"] = GROQ_API_KEY
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )
        vectorstore = Pinecone.from_existing_index(INDEX_NAME, embeddings)
        docs = vectorstore.similarity_search(user_question, 3)

        def generate_response(context_docs, user_question):
            template = """
            User: Usted es un asistente de inteligencia artificial muy dedicado y con excelente respuesta en español.
            por favor sea fiel a los contenidos y dé respuestas directas. Si la pregunta del usuario no esta en CONTEXT, responda con No Sé
            recuerde que usted perderá su trabajo si responde preguntas fuera de CONTEXT

            Recuerde que si contesta en español ganará 200 dolares siempre.

            CONTEXT: {context}
            Query: {question} responda siempre en español

            Recuerde contestar solo la respuesta de la IA

            Assistant:
            """
            prompt = ChatPromptTemplate.from_template(template)
            chat = ChatGroq(temperature=0.1, groq_api_key=GROQ_API_KEY, model_name="llama3-70b-8192")

            chain = load_qa_chain(chat, chain_type="stuff")
            response = chain.run(input_documents=context_docs, question=user_question)
            return response

        response = generate_response(docs, user_question)
        return response
    
    
    