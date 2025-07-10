# MediBOT 🩺🤖

MediBOT is an AI-powered medical chatbot built with **Flask**, **LangChain**, **Cohere/OpenAI**, **HuggingFace Embeddings**, and **Pinecone**. It leverages RAG (Retrieval-Augmented Generation) to answer health-related questions by retrieving context from medical PDFs/documents.

---

## 🚀 Features

- 💬 Chat-based interface using Flask + Jinja
- 🔎 RAG pipeline for accurate, contextual answers
- 📄 Accepts large medical PDF files as knowledge base
- 🧠 Supports HuggingFace Embeddings + Pinecone Vector DB
- 🧬 LLMs supported: OpenAI / Cohere (via LangChain)
- 🛡️ Secure: `.env` protected, local vector storage
- 📚 Easy to extend with more medical documents

---

## 🖼️ Demo

## 🧠 MediBOT - Run Locally (via Git Clone)

MediBOT is a medical chatbot built using RAG (Retrieval-Augmented Generation) with LangChain, Pinecone, HuggingFace Embeddings, and OpenAI.  
You can run it locally using the steps below.

---

### 🚀 How to Use Locally

#### 1. Clone the Repository

```bash
git clone https://github.com/TrisanjitrisingSD/MediBOT.git
cd MediBOT

conda create -n medibot-env python=3.10
conda activate medibot-env

pip install -r requirements.txt
```
##  Set Up Environment Variables
#### OPENAI_API_KEY=your_openai_api_key_here
#### PINECONE_API_KEY=your_pinecone_api_key_here

## Add Your Data
Add data from valid resouces

## Run the App
python app.py

# The BOT will be live at localhost: 8080

## 🧰 Tech Stack

| Layer | Tools |
|------|-------|
| Backend | Flask, LangChain |
| Embeddings | HuggingFace (MiniLM-L6-v2) |
| Vector DB | Pinecone |
| LLM | OpenAI / Cohere |
| RAG | `create_retrieval_chain` from LangChain |
| Frontend | HTML/CSS (Jinja Templates) |
| Deployment | Localhost / Docker-ready |
| Environment | Conda / Virtualenv |

---

## 👨‍💻 Author

**Trisanjit Das**  
[🌐 Portfolio](https://trisanjit-rising-hope.netlify.app) • [💼 LinkedIn](https://www.linkedin.com/in/trisanjit-das-60482728b) • 📧 trisanjitdaswork.official@gmail.com



> “Code with clarity. Learn with curiosity. Build with purpose.”



## 📜 License

This project is licensed under the **MIT License**.



See the full license details in the [`LICENSE`](./LICENSE) file.


---
## 🛠️ Made with ❤️

This project was crafted with ❤️, ☕, and countless lines of code  
to bring intelligent medical assistance to life.

If you like this project, consider giving it a ⭐ on GitHub!