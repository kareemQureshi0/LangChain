from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_chroma import Chroma
from dotenv import load_dotenv


load_dotenv()

pdf_path="output.pdf"

loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load()

# print(f"Total Pages Loaded: {len(docs)}")
# print(docs[0].page_content[:100])
# print(docs[0].metadata)

# text Splitters

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    keep_separator = ["\n\n","\n"," ",""],
)

chunks =text_splitter.split_documents(docs)

# print(f"total chunks created {len(chunks)}")
# print(chunks[0].page_content)
# print(chunks[0].metadata)

embeddings = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-2",output_dimensionality=768)

vector_store = Chroma.from_documents(
    documents = chunks,
    embedding = embeddings,
)

print("Vectors are stored Successfully")

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k":2}
)

query = "Who was Elbert Einstein and what was his age when he died"

retrieved_docs = retriever.invoke(query)

# for i,doc in enumerate(retrieved_docs):
#     print(f"\n--- Retrieved Chunks {i+1} (Page {doc.metadata.get('page')})")
#     print(doc.page_content)

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash-lite"
)

template = """
    You are a helpful assistant. Answer the question using ONLY the provided context.
If you do not know the answer or it is not in the context, say "I cannot find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)

def formatDocs(docs):
    return "\n\n" .join(doc.page_content for doc in docs)

rag_chain =(
    {"context": retriever | formatDocs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()

)

query = "Who is elbert Einstein and when he died? and what his contribution for the world"


response = rag_chain.invoke(query)

print("=== FINAL ANSWER FROM RAG ===")
print(response)
