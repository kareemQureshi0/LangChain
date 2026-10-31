from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser,ResponseSchema


load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")

schema = [
    ResponseSchema(name='fact_1', description = "Fact 1 about the topic"),
    ResponseSchema(name='fact_2', description = "Fact 2 about the topic"),
    ResponseSchema(name='fact_3', description = "Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template1 = PromptTemplate(
    template="Give three facts about the {topic} \n {format_instructions} ",
    input_variables=[],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

#prompt = template1.invoke({'topic':'Black Hole'})

#result = model.invoke(prompt)

# new_result=parser.parse(result.content)


chain = template1 | model |parser
print(chain.invoke({'topic':"black hole"}))


# with structure output parser we cannot do data validation