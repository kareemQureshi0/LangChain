from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

class Review(TypedDict):
    summary:str
    sentiment:str
 
 
structured_output = model.with_structured_output(Review)

result = structured_output.invoke("Super fast memory that delivers exactly what it promises on modern DDR5 platforms. 8GB is plenty for regular tasks, but it fills up fast if you run multiple heavy apps simultaneously. Still a solid, reliable purchase that leaves an easy upgrade path for dual-channel later.")

print(result['sentiment'])

