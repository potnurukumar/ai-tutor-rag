import os
from dotenv import load_dotenv
import google.generativeai as genai

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# -----------------------------
# 1. GEMINI SETUP
# -----------------------------
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model_llm = genai.GenerativeModel("gemini-1.5-flash-latest")

# -----------------------------
# 2. EMBEDDING MODEL
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# 3. DOCUMENTS
# -----------------------------
docs = [
    "Diabetes is a chronic disease.",
    "Hypertension is high blood pressure.",
    "AI can help in medical diagnosis.",
    "Machine learning is a subset of AI."
]

# -----------------------------
# 4. BUILD VECTOR DB
# -----------------------------
def build_db():
    embeddings = model.encode(docs)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    print("Vector DB ready")
    return index

# -----------------------------
# 5. RETRIEVER
# -----------------------------
class Retriever:
    def __init__(self, index, docs):
        self.index = index
        self.docs = docs

    def get_relevant_documents(self, query):
        q_emb = model.encode([query]).astype("float32")
        _, results = self.index.search(q_emb, k=2)

        return [self.docs[i] for i in results[0] if i != -1]

# -----------------------------
# 6. LLM FUNCTION
# -----------------------------
def ask_ai(context, question):
    prompt = f"""
You are an AI tutor.

Context:
{context}

Question:
{question}

Answer simply and clearly.
"""
    response = model_llm.generate_content(prompt)
    return response.text

# -----------------------------
# 7. MAIN
# -----------------------------
if __name__ == "__main__":

    index = build_db()
    retriever = Retriever(index, docs)

    print("\nAI Tutor Running...\n")

    while True:
        question = input("Ask (type exit to stop): ")

        if question.lower() == "exit":
            print("Goodbye 👋")
            break

        docs_found = retriever.get_relevant_documents(question)

        context = "\n".join(docs_found) if docs_found else "No context found"

        answer = ask_ai(context, question)

        print("\n🤖 ANSWER:\n", answer)