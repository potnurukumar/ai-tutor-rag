from loader import load_documents
from splitter import split_documents
from embeddings import create_vector_store

print("Loading documents...")
documents = load_documents("../data")

print(f"Loaded {len(documents)} documents.")

print("Splitting documents...")
chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks.")

print("Creating vector database...")
create_vector_store(chunks)

print("✅ Vector database created successfully!")