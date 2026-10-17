from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model ="gemini-embedding-2",output_dimensionality=300)

document = [
    "Every MS student will be allotted a qualified Supervisor, recommended/appointed by the BOS and then endorsed by the BOF.",
    "The maximum number of students per supervisor for MS or equivalent research will normally be seven (7) as per approved policy of HEC. It may be changed subsequent upon the changes in HEC policy.",
    "Close relative of the scholar/student cannot be a supervisor or examiner."
]

question = "who will appoint a supervisor"

doc = model.embed_documents(document)
query = model.embed_query(question)

score = cosine_similarity([query],doc)[0]

index, score = sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(question)
print(document[index])
print("Similarity is ",score)