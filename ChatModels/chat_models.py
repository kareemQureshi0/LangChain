from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
result = chatModel.invoke("Generate Python code for taking two inputs from user and return the sum of them")
print(result.content)