from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# use case i want to communicate two times with my llm
# llm give me detail report on black hole as i get the report i want to send that eport back 
# to llm to generate the summary for it

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")

template1 = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = "Write a summary on the followed text. \n {text}"
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

print(chain.invoke({'topic':"Cricket"}))