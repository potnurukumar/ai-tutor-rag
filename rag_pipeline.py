
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample documents
docs = [
    "Diabetes is a chronic disease.",
    "Hypertension is high blood pressure.",
    "AI can help in medical diagnosis."
]

# Build vector database
def build_db():
    embeddings = model.encode(docs)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    print("Vector DB ready")
    return index

# Retriever
class Retriever:
    def __init__(self, index, docs):
        self.index = index
        self.docs = docs

    def get_relevant_documents(self, query):
        q_emb = model.encode([query]).astype("float32")
        _, results = self.index.search(q_emb, k=2)

        return [self.docs[i] for i in results[0] if i != -1]

# Main
if __name__ == "__main__":

    index = build_db()
    retriever = Retriever(index, docs)

    print("\nAI Tutor Running...\n")

    while True:
        question = input("Ask (type exit to stop): ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        docs_found = retriever.get_relevant_documents(question)

        print("\nRetrieved Documents:\n")

        for i, doc in enumerate(docs_found, 1):
            print(f"{i}. {doc}")

        print()