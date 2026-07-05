from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embedding model once
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database once
vector_store = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)


def retrieve_context(query):
    """
    Retrieve the top 3 relevant document chunks.
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