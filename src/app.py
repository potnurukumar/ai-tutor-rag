from dotenv import load_dotenv
import streamlit as st

from src.logger import logger
from src.retriever import retrieve_context
from src.llm import get_answer
from src.upload import process_uploaded_file

load_dotenv()

st.set_page_config(
    page_title="AI Tutor RAG",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Sidebar ----------------

st.sidebar.title("🤖 AI Tutor RAG")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Indexing PDF..."):
        process_uploaded_file(uploaded_file.name)

    st.sidebar.success("PDF indexed successfully!")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.chat = []

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Features**

    ✅ PDF Upload

    ✅ FAISS Vector Search

    ✅ Google Gemini

    ✅ LangChain RAG

    ✅ Semantic Search
    """
)

# ---------------- Chat History ----------------

if "chat" not in st.session_state:
    st.session_state.chat = []

st.title("🤖 AI Tutor RAG")

st.write("Ask questions from your uploaded documents.")

question = st.text_input(
    "Ask your question"
)

if st.button("🚀 Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating answer..."):

            context, docs = retrieve_context(question)

            answer = get_answer(
                context,
                question
            )

        st.session_state.chat.append(
            {
                "question": question,
                "answer": answer,
                "docs": docs
            }
        )

# ---------------- Display Chat ----------------

for item in reversed(st.session_state.chat):

    st.markdown("---")

    st.markdown(f"### 🙋 Question")

    st.write(item["question"])

    st.markdown("### 🤖 Answer")

    st.write(item["answer"])

    with st.expander("📄 Source Documents"):

        if item["docs"]:

            for doc in item["docs"]:

                st.write(
                    f"📄 {doc.metadata.get('source','Unknown')} | "
                    f"Page: {doc.metadata.get('page','Unknown')}"
                )

    with st.expander("Retrieved Context"):

        context, _ = retrieve_context(item["question"])

        st.write(context)

st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit | LangChain | FAISS | Google Gemini"
)