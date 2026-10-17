from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
chat_history =[
    SystemMessage(content="Hey you are Skillfull research Assistant")
]

while True :
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input == 'exit':
        break
    result =  model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content[0]['text']))
    print("GEMINI-3.8-FLASH = ", result.content[0]['text'])
    
print(chat_history)