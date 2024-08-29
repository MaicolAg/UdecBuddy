import tempfile
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain





load_dotenv()

FILE_LIST = "archivos.txt"
PINECONE_ENV = "gcp-starter"
INDEX_NAME = 'arisma'

pinecone = Pinecone(api_key='d1422a1d-4d5a-4f68-be2e-81d6abf2aef7')

def save_name_files(path, new_files):
    old_files = load_name_files(path)
    with open(path, "a") as file:
        for item in new_files:
            if item not in old_files:
                file.write(item + "\n")
                old_files.append(item)
    
    return old_files


def load_name_files(path):
    archivos = []
    with open(path, "r") as file:
        for line in file:
            archivos.append(line.strip())
    return archivos


def clean_files():
    
    index = pinecone.Index("test")

    index.delete(delete_all=True, namespace='test')
    
    #pinecone.delete_index('test')
    #create_index()
    return True

'''def create_index():
    pinecone.create_index(
        name='test', 
        dimension=384, 
        metric="cosine", 
        spec=PodSpec(environment="us-west1-gcp", pod_type="p1.x1"))

## The following example creates an index that only indexes
## the 'color' metadata field. Queries against this index
## cannot filter based on any other metadata field.
    metadata_config = {
        'indexed': ['color']
    }

    pinecone.create_index(
        name='test', 
        dimension=384, 
        metric="cosine", 
        spec=PodSpec(environment="us-west1-gcp", pod_type="p1.x1", metadata_config=metadata_config))'''
    
def text_to_pinecone(pdf_content, pdf_name):
    temp_dir = tempfile.TemporaryDirectory()
    temp_filepath = os.path.join(temp_dir.name, pdf_name)
    with open(temp_filepath, "wb") as f:
        f.write(pdf_content)

    loader = PyPDFLoader(temp_filepath)
    text = loader.load()

    create_embeddings(pdf_name, text)

    return True

def create_embeddings(file_name, text):
    print(f"Creando embeddings del archivo: {file_name}")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        length_function=len
        )        
    chunks = text_splitter.split_documents(text)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )
    vectorstore = PineconeVectorStore.from_documents(chunks, embeddings, index_name=INDEX_NAME)
    return True

