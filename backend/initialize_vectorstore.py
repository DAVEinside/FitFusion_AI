from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


import os

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv
import os

load_dotenv()

OPEANAI_API_KEY = os.getenv('OPEANAI_API_KEY')

loader_meal = PyPDFLoader("C:/Users/DELL/FitFusion_AI/Datasets/dinners_cookbook_508-compliant.pdf")
document_meal = loader_meal.load()

# Split text into chunks

text_splitter  = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
text_chunks = text_splitter.split_documents(document_meal)

vectorstore_meal = Chroma.from_documents(documents=text_chunks,
                                    embedding=OpenAIEmbeddings(api_key=OPEANAI_API_KEY),
                                    persist_directory="C:/Users/DELL/FitFusion_AI/vectorstore")
vectorstore_meal.persist()




# Initialize an empty list to hold documents_workout
documents_workout = []

# Specify the folder path containing subfolders with PDF files
folder_path = 'C:/Users/DELL/FitFusion_AI/Datasets/Fitness Guides-20240701T232648Z-002'

# Walk through the folder and its subfolders to find all PDF files
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".pdf"):
            file_path = os.path.join(root, file)
            loader = PyPDFLoader(file_path)
            doc = loader.load()
            documents_workout.extend(doc)

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
text_chunks = text_splitter.split_documents(documents_workout)

# Create and persist the vector store
vectorstore_workout = Chroma.from_documents(documents=text_chunks,
                                    embedding=OpenAIEmbeddings(api_key=OPEANAI_API_KEY),
                                    persist_directory="C:/Users/DELL/FitFusion_AI/vectorstore")
vectorstore_workout.persist()