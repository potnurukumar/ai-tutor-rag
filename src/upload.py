import os
import shutil

from src.loader import load_documents
from src.splitter import split_documents
from src.embeddings import create_vector_store


from src.config import DATA_DIR

DATA_FOLDER = DATA_DIR



def process_uploaded_file(file_path):

    os.makedirs(DATA_FOLDER, exist_ok=True)

    destination = os.path.join(
        DATA_FOLDER,
        os.path.basename(file_path)
    )

    shutil.copy(file_path, destination)

    documents = load_documents(DATA_FOLDER)

    chunks = split_documents(documents)

    create_vector_store(chunks)

    return {
        "message": "Document uploaded successfully.",
        "filename": os.path.basename(file_path),
        "chunks": len(chunks)
    }