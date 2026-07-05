# Load data from file
with open("ai_notes.txt", "r", encoding="utf-8") as f:
    text = f.read()

docs = text.split("\n")




import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "ai_notes.txt")

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()


print("RAG starting...")

with open("ai_notes.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Loaded text:")
print(text)



from sentence_transformers import SentenceTransformer
import numpy as np

print("RAG starting...")

# STEP 1: Load data
with open("ai_notes.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Loaded text:\n", text)

# STEP 2: Split into chunks
chunks = text.split("\n")

print("\nChunks:")
print(chunks)

# STEP 3: Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# STEP 4: Create embeddings
embeddings = model.encode(chunks)

print("\nEmbeddings created!")

# STEP 5: Query
query = input("\nAsk something: ")

query_vec = model.encode([query])[0]

# STEP 6: Similarity search
scores = np.dot(embeddings, query_vec)

best_idx = np.argmax(scores)

print("\nBest answer:")
print(chunks[best_idx])