\# 📄 AI Tutor RAG



An AI-powered Tutor built using \*\*Retrieval-Augmented Generation (RAG)\*\* that answers questions from uploaded PDF documents using Google Gemini, LangChain, and FAISS.



\## 🚀 Features



\- Upload PDF documents

\- Extract text automatically

\- Create vector embeddings

\- Store embeddings using FAISS

\- Retrieve relevant document chunks

\- Generate accurate answers using Google Gemini

\- Streamlit web interface



\---



\## 🛠 Tech Stack



\- Python

\- Streamlit

\- LangChain

\- FAISS

\- Google Gemini API

\- HuggingFace Embeddings

\- PyPDF



\---



\## 📂 Project Structure



```

ai-tutor-rag/

│

├── data/

├── src/

├── vectorstore/

├── rag\_pipeline.py

├── rebuild.py

├── requirements.txt

├── README.md

└── .env.example

```



\---



\## ⚙ Installation



Clone the repository



```bash

git clone https://github.com/potnurukumar/ai-tutor-rag.git

cd ai-tutor-rag

```



Create a virtual environment



```bash

python -m venv venv

```



Activate the environment



```bash

venv\\Scripts\\activate

```



Install dependencies



```bash

pip install -r requirements.txt

```



Create a `.env` file



```

GOOGLE\_API\_KEY=your\_api\_key\_here

```



Run the application



```bash

streamlit run src/app.py

```



\---



\## 📸 Demo



(Add screenshots here)



\---



\## Future Improvements



\- Multi-PDF support

\- Chat history

\- Source citation

\- OCR for scanned PDFs

\- Cloud deployment



\---



\## Author



\*\*Potnuru Rakesh Kumar\*\*



GitHub:

https://github.com/potnurukumar

