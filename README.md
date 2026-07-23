# 🤖 AI Tutor RAG

<div align="center">

### 📄 AI-Powered Document Question Answering using Retrieval-Augmented Generation (RAG)

**FastAPI • Streamlit • LangChain • FAISS • Google Gemini • Docker**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-purple)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# 📖 Overview

AI Tutor RAG is a production-style **Retrieval-Augmented Generation (RAG)** application that enables users to upload PDF documents and ask natural language questions.

Instead of relying only on the Large Language Model's general knowledge, the application first retrieves the most relevant information from uploaded documents using **semantic search with FAISS**, then sends the retrieved context to **Google Gemini** to generate accurate, context-aware answers.

This project demonstrates an end-to-end AI pipeline including:

* Document ingestion
* Text extraction
* Text chunking
* Embedding generation
* Vector search
* Context retrieval
* LLM-based answer generation
* REST API development
* Interactive Streamlit interface
* Docker containerization

---

# ✨ Features

* 📄 Upload PDF documents
* 📚 Automatic text extraction
* ✂️ Intelligent document chunking
* 🧠 Hugging Face sentence embeddings
* ⚡ FAISS vector database
* 🔍 Semantic similarity search
* 🤖 Google Gemini integration
* 🌐 FastAPI REST API
* 🎨 Streamlit web interface
* 📝 Structured logging
* ⚠️ Global exception handling
* 🐳 Docker support
* 🚀 Modular project architecture

---

# 🏗️ System Architecture

```text
                    User Uploads PDF
                            │
                            ▼
                  PDF Text Extraction
                            │
                            ▼
                 Text Chunking (LangChain)
                            │
                            ▼
           Hugging Face Embedding Model
                            │
                            ▼
                  FAISS Vector Database
                            ▲
                            │
                  User Question
                            │
                            ▼
                 Semantic Similarity Search
                            │
                            ▼
                 Retrieved Context Chunks
                            │
                            ▼
                  Google Gemini LLM
                            │
                            ▼
                      Final Answer
```

---

# 🔄 Project Workflow

```text
Upload PDF
     │
     ▼
Extract Text
     │
     ▼
Split into Chunks
     │
     ▼
Generate Embeddings
     │
     ▼
Store in FAISS
     │
     ▼
User asks Question
     │
     ▼
Retrieve Top Relevant Chunks
     │
     ▼
Send Context + Question to Gemini
     │
     ▼
Generate AI Answer
     │
     ▼
Return Answer + Source References
```

---

# 🛠️ Tech Stack

| Category             | Technology                             |
| -------------------- | -------------------------------------- |
| Programming Language | Python 3.11                            |
| Backend              | FastAPI                                |
| Frontend             | Streamlit                              |
| Framework            | LangChain                              |
| LLM                  | Google Gemini                          |
| Embeddings           | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database      | FAISS                                  |
| API Documentation    | Swagger UI                             |
| Containerization     | Docker                                 |
| Version Control      | Git & GitHub                           |

---

# 📁 Project Structure

```text
ai-tutor-rag/
│
├── data/
├── logs/
├── src/
│   ├── api.py
│   ├── app.py
│   ├── config.py
│   ├── embeddings.py
│   ├── exceptions.py
│   ├── llm.py
│   ├── loader.py
│   ├── logger.py
│   ├── middleware.py
│   ├── retriever.py
│   ├── splitter.py
│   ├── upload.py
│   └── __init__.py
│
├── vectorstore/
├── Dockerfile
├── requirements.txt
├── README.md
└── .env.example
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/potnurukumar/ai-tutor-rag.git
cd ai-tutor-rag
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

## ▶️ Run the Application

### FastAPI Backend

```bash
python -m uvicorn src.api:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

### Streamlit Frontend

```bash
streamlit run src/app.py
```

The Streamlit application will launch in your browser.

---
# 📡 REST API

After starting the FastAPI server, open:

```text
http://127.0.0.1:8000/docs
```

Interactive Swagger documentation will be available.

---

## Health Check

**Request**

```http
GET /api/v1/health
```

**Response**

```json
{
    "status": "healthy",
    "service": "AI Tutor RAG"
}
```

---

## Upload PDF

**Request**

```http
POST /api/v1/upload
```

**Form Data**

| Parameter | Type | Required |
| --------- | ---- | -------- |
| file      | PDF  | ✅        |

**Response**

```json
{
    "status": "success",
    "message": "Document uploaded successfully.",
    "filename": "RAG_Project_Report.pdf",
    "chunks": 9
}
```

---

## Ask Question

**Request**

```http
POST /api/v1/ask
```

**Request Body**

```json
{
    "question": "Summarize the uploaded document."
}
```

**Response**

```json
{
    "status": "success",
    "question": "Summarize the uploaded document.",
    "answer": "The uploaded document explains...",
    "sources": [
        {
            "page": 1,
            "source": "RAG_Project_Report.pdf"
        }
    ]
}
```

---

# 🐳 Docker

## Build Docker Image

```bash
docker build -t ai-tutor-rag .
```

## Run Docker Container

```bash
docker run -p 8501:8501 ai-tutor-rag
```

---

# 📷 Screenshots

Create a folder named:

```text
screenshots/
```

Add these screenshots:

```text
screenshots/
│
├── home.png
├── upload.png
├── question.png
├── answer.png
├── swagger.png
```

Then display them:

```markdown
## Home Page

![Home](screenshots/home.png)

---

## Upload PDF

![Upload](screenshots/upload.png)

---

## Ask Questions

![Question](screenshots/question.png)

---

## AI Response

![Answer](screenshots/answer.png)

---

## Swagger API

![Swagger](screenshots/swagger.png)
```

---

# 💡 Skills Demonstrated

This project demonstrates practical experience with:

* Python
* FastAPI
* Streamlit
* LangChain
* Retrieval-Augmented Generation (RAG)
* Google Gemini API
* Hugging Face Embeddings
* FAISS Vector Database
* Semantic Search
* REST API Development
* Prompt Engineering
* Docker
* Environment Variables
* Logging
* Exception Handling
* Software Architecture
* Git & GitHub

---

# 📈 Complete RAG Pipeline

```text
                PDF Document
                      │
                      ▼
             Extract Text from PDF
                      │
                      ▼
              Split into Chunks
                      │
                      ▼
          Generate Sentence Embeddings
                      │
                      ▼
            Store in FAISS Index
                      │
────────────────────────────────────────────
                User Question
                      │
                      ▼
      Similarity Search in FAISS
                      │
                      ▼
      Retrieve Relevant Context
                      │
                      ▼
         Google Gemini LLM
                      │
                      ▼
        AI Generated Response
                      │
                      ▼
     Return Answer + Source References
```

---

# 🚀 Future Improvements

* ✅ Multiple PDF support
* ✅ Chat history
* ✅ Authentication & user accounts
* ✅ Hybrid Search (BM25 + FAISS)
* ✅ Pinecone integration
* ✅ ChromaDB integration
* ✅ Cloud deployment
* ✅ Streaming AI responses
* ✅ Conversation memory
* ✅ Admin dashboard
* ✅ Unit testing
* ✅ CI/CD pipeline
* ✅ Kubernetes deployment
* ✅ AWS deployment
* ✅ Azure deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Potnuru Rakesh Kumar

**Computer Science Student | AI & Machine Learning Enthusiast | Python Developer | Generative AI | LangChain | RAG | Docker**

### Connect with me

* GitHub: https://github.com/potnurukumar
* LinkedIn: https://www.linkedin.com/in/potnuru-rakesh-kumar-36b7832a6

---

# ⭐ Support

If you found this project helpful:

⭐ Star this repository

🍴 Fork the repository

📢 Share it with others

---

# 🙏 Acknowledgements

This project uses the following open-source technologies:

* Python
* FastAPI
* Streamlit
* LangChain
* FAISS
* Hugging Face
* Google Gemini
* Docker

Special thanks to the open-source community for providing the tools and libraries that made this project possible.

