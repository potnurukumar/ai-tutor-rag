import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embedding model once
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Get correct absolute path (IMPORTANT for Streamlit Cloud)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
VECTOR_PATH = os.path.join(BASE_DIR, "vectorstore")


def load_vectorstore():
    return FAISS.load_local(
        VECTOR_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


vector_store = load_vectorstore()


def retrieve_context(query):
    """
    Retrieve top 3 relevant chunks
    """

    try:
        docs = vector_store.similarity_search(query, k=3)

        if not docs:
            return "", []

        context = "\n\n".join(doc.page_content for doc in docs)

        return context, docs

    except Exception as e:
        print(f"Retriever Error: {e}")
        return "", []