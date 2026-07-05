from dotenv import load_dotenv

from retriever import retrieve_context
from llm import get_answer

# Load environment variables
load_dotenv("../.env")

while True:
    query = input("\nAsk something (type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    context, docs = retrieve_context(query)

    answer = get_answer(context, query)

    print("\n===== FINAL ANSWER =====\n")
    print(answer)

    print("\n===== SOURCES =====")
    for i, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "Unknown")
        print(f"{i}. {source}")





import os
from dotenv import load_dotenv

from retriever import retrieve_context
from llm import get_answer

# Load environment variables
load_dotenv("../.env")

while True:
    query = input("\nAsk something (type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    context = retrieve_context(query)

    answer = get_answer(context, query)

    print("\n===== FINAL ANSWER =====\n")
    print(answer)