from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.llms import Cohere
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from .env
load_dotenv()

# Load API keys
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

# Set them as environment variables (some tools require it this way)
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["COHERE_API_KEY"] = COHERE_API_KEY

# Load HuggingFace embedding model
embeddings = download_hugging_face_embeddings()

# Pinecone index name
index_name = "medibot"

# Load from existing Pinecone index
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

# Create retriever from the vector store
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Create Cohere LLM instance
llm = Cohere(model="command-light", temperature=0.4, max_tokens=500)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Setup RAG pipeline
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Routes
@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print("User Query:", msg)

    try:
        result = rag_chain.invoke({"input": msg})
        answer = result.get("answer") or result.get("result", "❌ No valid response.")
        print("Response:", answer)
        return str(answer)
    except Exception as e:
        print("Error:", e)
        return "❌ Something went wrong: " + str(e)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
