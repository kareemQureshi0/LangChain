from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model ="gemini-3.5-flash-lite")

class Person(BaseModel):
    
    name: str = Field(description="Name of the Person")
    age: int = Field(gt = 18, description="Age of the person")
    city: str = Field(description='Name of the city the person belongs to')
    
    
parser = PydanticOutputParser(pydantic_object=Person)

template1 = PromptTemplate(
    template = "Generate the name of the person, age and city of a fictional {place} person \n {format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = template1 | model | parser

#prompt = template1.invoke({'place':'india'})

#result = model.invoke(prompt)

#final_result = parser.parse(result.content)
print(chain.invoke({'place':'israel'}))