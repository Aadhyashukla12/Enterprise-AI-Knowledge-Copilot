from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import os
import shutil
from dotenv import load_dotenv
from openai import OpenAI

from rag import (
    extract_text,
    extract_all_pdfs,
    chunk_text,
    retrieve_chunks
)
from vectorstore import create_vector_store, load_vector_store

# ==========================
# Load Environment Variables
# ==========================

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# ==========================
# FastAPI App
# ==========================

app = FastAPI()

# ==========================
# CORS
# ==========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Home API
# ==========================

@app.get("/")
def home():
    return {
        "message": "Backend Running Successfully"
    }

# ==========================
# Request Model
# ==========================

class ChatRequest(BaseModel):
    message: str
class DeleteRequest(BaseModel):
    filename: str
# ==========================
# Upload PDF
# ==========================

@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)
    print("Uploading file:", file.filename)

    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print("Saved to:", file_path)
    print("Exists:", os.path.exists(file_path))
    print("Size:", os.path.getsize(file_path))
    print("Files in uploads:", os.listdir("uploads"))

    # Extract Text
    text = extract_all_pdfs("uploads")

    # Chunk Text
    chunks = chunk_text(text)
    
    # Create Vector Database
    create_vector_store(
    chunks,
    file.filename
)

    return {
        "message": "File uploaded successfully!",
        "filename": file.filename,
        "total_chunks": len(chunks),
        "vector_database": "Created Successfully"
    }
@app.get("/documents")
def get_documents():

    os.makedirs("uploads", exist_ok=True)

    documents = []

    for file in os.listdir("uploads"):

        if file.lower().endswith(".pdf"):
            documents.append(file)

    return {
        "documents": documents
    }
@app.delete("/delete")
def delete_document(request: DeleteRequest):

    try:

        file_path = os.path.join("uploads", request.filename)

        if os.path.exists(file_path):
            os.remove(file_path)

        # Remaining PDFs
        if os.path.exists("uploads"):

            files = [
                f for f in os.listdir("uploads")
                if f.lower().endswith(".pdf")
            ]

        else:
            files = []

        # If no PDFs remain
        if len(files) == 0:

            if os.path.exists("faiss_index"):
                shutil.rmtree("faiss_index")

            return {
                "message": "Document deleted successfully."
            }

        # Rebuild Vector Database
        text = extract_all_pdfs("uploads")

        chunks = chunk_text(text)

        create_vector_store(
            chunks,
            "Multiple Documents"
        )

        return {
            "message": "Document deleted successfully."
        }

    except Exception as e:

        return {
            "message": str(e)
        }
# ==========================
# Chat API
# ==========================

@app.post("/chat")
def chat(request: ChatRequest):

    try:

        # Load Vector Store
        vector_db = load_vector_store()

        # Retrieve Relevant Context
        context, sources = retrieve_chunks(
           vector_db,
           request.message
)

        print("\n========================================")
        print("QUESTION:")
        print(request.message)
        print("\nRETRIEVED CONTEXT:\n")
        print(context)
        print("========================================\n")

        # No Context Found
        if not context.strip():
            return {
                "response": "I could not find this information in the uploaded document."
            }

        completion = client.chat.completions.create(

            model="openai/gpt-oss-20b:free",

            messages=[

                {
                    "role": "system",
                    "content": """
You are an Enterprise AI Knowledge Assistant.

You answer questions ONLY using the DOCUMENT CONTEXT provided.

Rules:

1. Read the DOCUMENT CONTEXT carefully.

2. Never use outside knowledge.

3. Never guess or assume anything.

4. Never invent information.

5. If the answer exists in the document, answer clearly.

6. Format every response using Markdown.
- Use headings when appropriate.
- Use bullet points for lists.
- Use numbered lists for steps.
- Use tables whenever comparison is useful.
- Use code blocks for code.
- Keep formatting clean and readable.

7. If the answer is NOT found in the document,
reply EXACTLY:

I could not find this information in the uploaded document.

8. Never ask the user to upload the document again.

9. Keep answers concise and professional.
"""
                },

                {
                    "role": "user",
                    "content": f"""
DOCUMENT CONTEXT

{context}

--------------------------------

QUESTION

{request.message}

--------------------------------

ANSWER
"""
                }

            ]

        )

        answer = completion.choices[0].message.content

        return {
           "response": answer,
           "sources": sources
}

    except Exception as e:

        print(e)

        return {
            "response": str(e)
        }