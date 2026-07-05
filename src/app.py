import streamlit as st
from dotenv import load_dotenv

from retriever import retrieve_context
from llm import get_answer

# Load environment variables
load_dotenv("../.env")

# Page configuration
st.set_page_config(
    page_title="AI Tutor RAG",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
st.sidebar.title("🤖 AI Tutor RAG")
st.sidebar.markdown("""
### 🚀 Features
- 📄 PDF & TXT Support
- 🔍 FAISS Vector Search
- 🧠 Google Gemini 2.5 Flash
- 📚 LangChain RAG Pipeline
- ⚡ Fast Semantic Search

---
Developed by **Rakesh Kumar**
""")

# Main title
st.title("🤖 AI Tutor RAG")
st.write("Ask questions from your uploaded documents.")

# User input
query = st.text_area(
    "Enter your question:",
    height=120,
    placeholder="Example: What is Artificial Intelligence?"
)

# Ask button
if st.button("🚀 Ask AI"):

    if not query.strip():
        st.warning("⚠ Please enter a question.")

    else:
        try:
            with st.spinner("🔍 Searching documents and generating answer..."):

                context, docs = retrieve_context(query)

                answer = get_answer(context, query)

            st.success("✅ Answer generated successfully!")

            st.subheader("📖 Answer")
            st.write(answer)

            st.subheader("📄 Source Documents")

            if docs:
                for doc in docs:
                    source = doc.metadata.get("source", "Unknown")
                    st.markdown(f"📄 **{source}**")
            else:
                st.info("No source documents found.")

            with st.expander("📚 View Retrieved Context"):
                st.write(context)

        except Exception as e:
            st.error(f"❌ Error: {e}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit • LangChain • FAISS • Google Gemini")