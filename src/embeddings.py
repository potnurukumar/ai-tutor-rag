from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vector_store(chunks):
    # ALWAYS create fresh index
    vector_store = FAISS.from_documents(chunks, embeddings)

    # FORCE correct absolute path
    save_path = os.path.join(os.getcwd(), "vectorstore")

    # ensure folder exists
    os.makedirs(save_path, exist_ok=True)

    vector_store.save_local(save_path)

    print("✔ Vectorstore saved at:", save_path)