from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# use case i want to communicate two times with my llm
# llm give me detail report on black hole as i get the report i want to send that eport back 
# to llm to generate the summary for it

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")

parser = JsonOutputParser()

template1 = PromptTemplate(
    template="Give me age,name and country of fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt1 = template1.invoke({})

result = model.invoke(prompt1)

final_result = parser.parse(result)


print(final_result)