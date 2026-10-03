from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="gsaivinay/Llama-2-7b-Chat-GPTQ",
    task="text-generation"
    )


model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is the prime Minister of Pakistan")

print(result)