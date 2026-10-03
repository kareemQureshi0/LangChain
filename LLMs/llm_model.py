from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-3.8-flash")

result = model.invoke("What is the capital of Punjab")
print(result)