from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2",output_dimensionality=32)

document =[
    "What is the capital of Pakistan",
    "Who is the founder of Pakistan",
    "Who is the president of iiui"
]
query = model.embed_documents(document)

print(str(query))