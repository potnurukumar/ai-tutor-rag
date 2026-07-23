from fastapi import FastAPI, APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel, Field
import os

from src.logger import logger
from src.upload import process_uploaded_file
from src.retriever import retrieve_context
from src.llm import get_answer
from src.exceptions import global_exception_handler
from src.middleware import log_requests

# --------------------------------------------------
# FastAPI App
# --------------------------------------------------

app = FastAPI(
    title="AI Tutor RAG API",
    description="Production-style RAG backend",
    version="1.0.0"
)

# Middleware
app.middleware("http")(log_requests)

# Router
router = APIRouter(
    prefix="/api/v1",
    tags=["AI Tutor RAG"]
)

# Global Exception Handler
app.add_exception_handler(
    Exception,
    global_exception_handler
)


# --------------------------------------------------
# Request Model
# --------------------------------------------------

class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        description="Question to ask from the uploaded document"
    )


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@router.get("/health")
def health_check():
    logger.info("Health API called")

    return {
        "status": "healthy",
        "service": "AI Tutor RAG"
    }


# --------------------------------------------------
# Ask Question
# --------------------------------------------------

@router.post("/ask")
def ask_question(request: QuestionRequest):

    try:
        logger.info(f"Question received: {request.question}")

        context, docs = retrieve_context(request.question)

        answer = get_answer(
            context=context,
            question=request.question
        )

        sources = [
            {
                "page": doc.metadata.get("page", "Unknown"),
                "source": doc.metadata.get("source", "Unknown")
            }
            for doc in docs
        ]

        logger.info("Answer generated successfully")

        return {
            "status": "success",
            "question": request.question,
            "answer": answer,
            "sources": sources
        }

    except Exception:
        logger.exception("Error while generating answer")

        raise HTTPException(
            status_code=500,
            detail="Failed to generate answer."
        )


# --------------------------------------------------
# Upload PDF
# --------------------------------------------------

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    temp_path = None

    try:
        logger.info(f"Upload request received: {file.filename}")

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed."
            )

        os.makedirs("temp", exist_ok=True)

        temp_path = os.path.join("temp", file.filename)

        with open(temp_path, "wb") as buffer:
            buffer.write(await file.read())

        if os.path.getsize(temp_path) == 0:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        result = process_uploaded_file(temp_path)

        logger.info(f"{file.filename} uploaded successfully")

        return {
            "status": "success",
            "message": "PDF uploaded and indexed successfully.",
            **result
        }

    except HTTPException:
        raise

    except Exception:
        logger.exception("Upload failed")

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


# --------------------------------------------------
# Register Router
# --------------------------------------------------

app.include_router(router)