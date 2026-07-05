from loader import load_documents
from splitter import split_documents
from embeddings import create_vector_store

documents = load_documents("data")
chunks = split_documents(documents)
create_vector_store(chunks)

print("Vectorstore rebuilt")