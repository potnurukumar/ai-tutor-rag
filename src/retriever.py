import os

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from src.config import VECTORSTORE_DIR
from src.logger import logger

# ----------------------------------------
# Embedding Model
# ----------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ----------------------------------------
# Vectorstore Path
# ----------------------------------------

VECTOR_PATH = VECTORSTORE_DIR

logger.info(f"Loading vectorstore from: {VECTOR_PATH}")

# ----------------------------------------
# Load FAISS Vector Store
# ----------------------------------------

def load_vectorstore():
    if not os.path.exists(VECTOR_PATH):
        raise FileNotFoundError(
            f"Vectorstore not found: {VECTOR_PATH}"
        )

    return FAISS.load_local(
        VECTOR_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

# Load once during application startup
vector_store = load_vectorstore()

# ----------------------------------------
# Retrieve Context
# ----------------------------------------

def retrieve_context(query: str):
    try:
        docs = vector_store.similarity_search(query, k=3)

        if not docs:
            return "", []

        context = "\n\n".join(doc.page_content for doc in docs)

        return context, docs

    except Exception:
        logger.exception("Retriever error")
        return "", []