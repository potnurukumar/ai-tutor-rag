
# 🤖 AI Tutor RAG

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-purple)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)

An AI-powered **Retrieval-Augmented Generation (RAG)** application that answers questions from uploaded PDF documents using semantic search and Google Gemini. The project combines FastAPI, Streamlit, LangChain, Hugging Face embeddings, and FAISS to provide accurate document-based question answering.

---

# ✨ Features

* 📄 Upload PDF documents
* 🔍 Automatic text extraction
* ✂️ Intelligent document chunking
* 🧠 Semantic embeddings using Hugging Face
* ⚡ Fast similarity search with FAISS
* 🤖 AI-powered answers using Google Gemini
* 🌐 FastAPI REST API
* 🎨 Streamlit web interface
* 📝 Logging and exception handling
* 🐳 Docker support

---

# 🏗️ Architecture

```text
           PDF Upload
                │
                ▼
        Text Extraction
                │
                ▼
      Text Chunking (LangChain)
                │
                ▼
      Hugging Face Embeddings
                │
                ▼
         FAISS Vector Store
                │
     User Question
                │
                ▼
     Similarity Search (Top-K)
                │
                ▼
        Google Gemini LLM
                │
                ▼
         Final AI Response
```

---

# 🛠️ Tech Stack

| Category         | Technology                             |
| ---------------- | -------------------------------------- |
| Language         | Python                                 |
| Backend          | FastAPI                                |
| Frontend         | Streamlit                              |
| LLM              | Google Gemini                          |
| Framework        | LangChain                              |
| Vector Database  | FAISS                                  |
| Embeddings       | sentence-transformers/all-MiniLM-L6-v2 |
| Containerization | Docker                                 |

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
│   ├── llm.py
│   ├── retriever.py
│   ├── upload.py
│   ├── logger.py
│   ├── middleware.py
│   └── exceptions.py
│
├── vectorstore/
├── Dockerfile
├── requirements.txt
├── README.md
└── .env.example
```

---

# ⚙️ Installation

```bash
git clone https://github.com/potnurukumar/ai-tutor-rag.git
cd ai-tutor-rag
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Run the FastAPI server:

```bash
python -m uvicorn src.api:app --reload
```

Run the Streamlit app:

```bash
streamlit run src/app.py
```

---

# 📡 API Endpoints

| Method | Endpoint         | Description                            |
| ------ | ---------------- | -------------------------------------- |
| GET    | `/api/v1/health` | Health check                           |
| POST   | `/api/v1/upload` | Upload and index a PDF                 |
| POST   | `/api/v1/ask`    | Ask questions about uploaded documents |

---

# 🐳 Docker

Build:

```bash
docker build -t ai-tutor-rag .
```

Run:

```bash
docker run -p 8501:8501 ai-tutor-rag
```

---

# 📸 Screenshots

Add screenshots here after deployment:

* Home page
* PDF upload
* Question answering
* Swagger API documentation

---

# 🚀 Future Enhancements

* Multiple document support
* Chat history
* Authentication
* Hybrid search
* Vector database migration (Chroma/Pinecone)
* Cloud deployment

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Potnuru Rakesh Kumar**

* GitHub: https://github.com/potnurukumar
* LinkedIn: https://www.linkedin.com/in/potnuru-rakesh-kumar-36b7832a6

If you found this project useful, consider giving it a ⭐ on GitHub.
