import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embedding model once
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ALWAYS use absolute working directory (Streamlit-safe)
VECTOR_PATH = os.path.abspath("vectorstore")


def load_vectorstore():
    if not os.path.exists(VECTOR_PATH):
        raise FileNotFoundError(f"Vectorstore not found at {VECTOR_PATH}")

    return FAISS.load_local(
        VECTOR_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


vector_store = load_vectorstore()


def retrieve_context(query):
    try:
        docs = vector_store.similarity_search(query, k=3)

        if not docs:
            return "", []

        context = "\n\n".join(doc.page_content for doc in docs)

        return context, docs

    except Exception as e:
        print("Retriever Error:", e)
        return "", []