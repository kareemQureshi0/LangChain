from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2",output_dimensionality=32)
query = model.embed_query("What is the capital of Pakistan?")

print(str(query))