import os
from dotenv import load_dotenv

load_dotenv()

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Folders
DATA_DIR = os.path.join(BASE_DIR, "data")
VECTORSTORE_DIR = os.path.join(BASE_DIR, "vectorstore")
TEMP_DIR = os.path.join(BASE_DIR, "temp")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")