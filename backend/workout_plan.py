# In backend/plan_generation.py

import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


from dotenv import load_dotenv
import os

load_dotenv()

OPEANAI_API_KEY = os.getenv('OPEANAI_API_KEY')


def generate_workout_plan(user):
    prompt = ChatPromptTemplate(
        input_variables=['context', 'FitnessPlan'],
        messages=[
            HumanMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=['context', 'FitnessPlan'],
                    template=(
                        "You are a Fitness Trainer responsible for generating a detailed Workout plan for the given Fitness Plan. "
                        "You are to generate step-by-step instructions for exercises for each day, covering a full 7 days of the week. "
                        "In total, you will create a complete workout regimen with a mix of cardio, strength training, flexibility exercises, and rest days as needed. "
                        "Provide the duration and intensity of each workout, and include any necessary equipment. "
                        "Use the following pieces of retrieved context to generate the detailed workout plan.\n"
                        "Fitness Plan: {FitnessPlan}\nContext: {context}\nAnswer:"
                    )
                )
            )
        ]
    )

    llm = ChatOpenAI(api_key=OPEANAI_API_KEY, model_name="gpt-4", temperature=0)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    vectorstore = Chroma(persist_directory="C:/Users/DELL/FitFusion_AI/vectorstore")
    retriever = vectorstore.as_retriever(search_kwargs={'k': 20})

    rag_chain = (
        {"context": retriever | format_docs, "FitnessPlan": lambda _: user.fitness_goals}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain.invoke(user.fitness_goals)