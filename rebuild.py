from src.loader import load_documents
from src.splitter import split_documents
from src.embeddings import create_vector_store

print("Loading documents...")
docs = load_documents("data")

print("Splitting...")
chunks = split_documents(docs)

print("Building FAISS...")
create_vector_store(chunks)

print("DONE - Vectorstore created successfully")