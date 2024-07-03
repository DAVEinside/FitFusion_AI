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


# Calorie calculation function
def calories_calc(sex, weight, height, age):
    if sex == "Male":
        BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        return int(BMR * 1.55)
    elif sex == "Female":
        BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return int(BMR * 1.55)
    else:
        print("Please enter a valid sex")

def generate_meal_plan(user):
    calories = calories_calc(user.sex, user.weight, user.height, user.age)

    prompt = ChatPromptTemplate(
        input_variables=['context', 'Diet', 'calories'],
        messages=[
            HumanMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=['context', 'Diet', 'calories'],
                    template=(
                        "You are a Fitness Chef responsible for generating a Meal plan for the given Diet."
                        " You are to generate step-by-step instructions for preparing meals for Breakfast, Lunch, and Dinner for 7 days of the week, totaling 21 meals"
                        " for the specified Diet. Also, provide the calorie count for each meal, aiming to reach a total daily calorie intake of {calories} calories."
                        " Use the following pieces of retrieved context to generate detailed step-by-step recipes."
                        "\nDiet: {Diet}\nContext: {context}\nTarget Daily Calories: {calories}\nAnswer:"
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
        {"context": retriever | format_docs, "Diet": lambda _: user.dietary_preferences, "calories": lambda _: calories}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain.invoke(user.dietary_preferences)