# 📄 AI Tutor RAG

> An AI-powered document-based tutor that uses **Retrieval-Augmented Generation (RAG)** to answer questions from uploaded PDF and text documents.

AI Tutor RAG is an intelligent question-answering application built using **LangChain, FAISS, Hugging Face Embeddings, Google Gemini, and Streamlit**.

The system retrieves relevant information from user-provided documents and generates context-aware answers using a Large Language Model.

---

## 🚀 Features

* 📄 Upload and process PDF and text documents
* 🔍 Automatic document text extraction
* ✂️ Intelligent text chunking
* 🧠 Semantic embeddings using Hugging Face
* ⚡ Fast similarity search using FAISS
* 🤖 Retrieval-Augmented Generation pipeline
* 💬 Context-aware answers using Google Gemini
* 🌐 Interactive Streamlit web interface
* 🐳 Docker-ready application

---

## 🔄 RAG Workflow

```text
Document Upload
       ↓
Text Extraction
       ↓
Text Chunking
       ↓
Embedding Generation
       ↓
FAISS Vector Store
       ↓
Similarity Search
       ↓
Relevant Context Retrieval
       ↓
Google Gemini
       ↓
AI-Generated Answer
```

---

## 🧠 How It Works

1. The user uploads a document.
2. Text is extracted from the document.
3. The extracted text is divided into smaller chunks.
4. Each chunk is converted into a vector embedding.
5. Embeddings are stored in a **FAISS vector database**.
6. When the user asks a question, the system performs a similarity search.
7. Relevant document chunks are retrieved.
8. The retrieved context is passed to **Google Gemini**.
9. Gemini generates a context-aware answer based on the retrieved information.

This approach helps the AI answer questions using the information available in the uploaded documents.

---

## 🛠️ Tech Stack

| Technology                  | Purpose                    |
| --------------------------- | -------------------------- |
| **Python**                  | Core programming language  |
| **Streamlit**               | Web application interface  |
| **LangChain**               | RAG pipeline orchestration |
| **FAISS**                   | Vector similarity search   |
| **Hugging Face Embeddings** | Semantic text embeddings   |
| **Google Gemini**           | Large Language Model       |
| **PyPDF**                   | PDF text extraction        |
| **Docker**                  | Containerization           |

---

## 📂 Project Structure

```text
ai-tutor-rag/
│
├── data/
│   └── Documents used for processing
│
├── src/
│   └── Streamlit application files
│
├── vectorstore/
│   └── FAISS vector index
│
├── rag_pipeline.py
├── rebuild.py
├── test_models.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/potnurukumar/ai-tutor-rag.git
cd ai-tutor-rag
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> ⚠️ Never commit your `.env` file or API keys to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run src/app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 🐳 Run with Docker

### Build the Docker Image

```bash
docker build -t ai-tutor-rag .
```

### Run the Container

```bash
docker run -p 8501:8501 --env-file .env ai-tutor-rag
```

Open the application in your browser:

```text
http://localhost:8501
```

---

## 📸 Application Preview

*Add application screenshots here.*

---

## 🎯 Key Learning Outcomes

Through this project, I gained practical experience in:

* Retrieval-Augmented Generation (RAG)
* Vector databases and semantic search
* Text embeddings
* LangChain pipelines
* Large Language Model integration
* FAISS similarity search
* Streamlit application development
* Docker containerization

---

## 🔮 Future Improvements

* 💬 Chat history and multi-turn conversations
* 📚 Multi-document knowledge base
* 🔗 Source citation for generated answers
* 🖼️ OCR support for scanned documents
* ☁️ Cloud deployment
* 🔐 User authentication
* 📊 Document analytics

---

## 👨‍💻 Author

### Potnuru Rakesh Kumar

Computer Science Student | AI & Machine Learning Enthusiast

🔗 **GitHub:** https://github.com/potnurukumar

