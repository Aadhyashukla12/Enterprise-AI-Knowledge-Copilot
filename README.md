# Enterprise AI Knowledge Copilot

An AI-powered knowledge assistant that allows users to upload PDF documents and ask questions based on their content. The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate contextual answers.

## 🚀 Live Demo

[Enterprise AI Knowledge Copilot](https://enterprise-ai-knowledge-copilot-production-807e.up.railway.app)

## ✨ Features

- Upload PDF documents
- Extract and process document content
- Generate embeddings using HuggingFace
- Store and retrieve document embeddings using FAISS
- Ask questions about uploaded documents
- Context-aware AI responses using RAG
- Chat history
- React-based user interface
- Separate frontend and backend architecture
- Deployed on Railway

## 🛠️ Tech Stack

### Frontend
- React.js
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- Uvicorn

### AI & RAG
- LangChain
- HuggingFace Embeddings
- FAISS
- OpenRouter API

### Deployment
- Railway
- GitHub

## 🧠 How It Works

```text
User
  ↓
React Frontend
  ↓
FastAPI Backend
  ↓
PDF Processing
  ↓
Text Chunking
  ↓
HuggingFace Embeddings
  ↓
FAISS Vector Store
  ↓
Relevant Context Retrieval
  ↓
OpenRouter LLM
  ↓
AI Generated Response
## 📁 Project Structure

```text
Enterprise-AI-Knowledge-Copilot/
│
├── backend/
│   ├── main.py
│   ├── rag.py
│   ├── vectorstore.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── package.json
│   ├── vite.config.js
│   └── ...
│
├── .gitignore
└── README.md

### 2. Local Setup

Then below that:

```markdown
## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aadhyashukla12/Enterprise-AI-Knowledge-Copilot.git
cd Enterprise-AI-Knowledge-Copilot
## 📁 Project Structure

```text
Enterprise-AI-Knowledge-Copilot/
│
├── backend/
│   ├── main.py
│   ├── rag.py
│   ├── vectorstore.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── package.json
│   ├── vite.config.js
│   └── ...
│
├── .gitignore
└── README.md

### 2. Local Setup

```markdown
## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aadhyashukla12/Enterprise-AI-Knowledge-Copilot.git
cd Enterprise-AI-Knowledge-Copilot
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
OPENROUTER_API_KEY=your_api_key_here
uvicorn main:app --reload --port 8001

FRONTEND SETUP
cd frontend
npm install
npm run dev


### 3. Environment Variables

```markdown
## 🔐 Environment Variables

The backend requires the following environment variable:

```env
OPENROUTER_API_KEY=your_api_key_here


### 4. Deployment

```markdown
## ☁️ Deployment

The application is deployed on Railway using separate services for the frontend and backend.

- Frontend: React + Vite
- Backend: FastAPI + Uvicorn
- Repository: GitHub

The frontend communicates with the deployed FastAPI backend through the production API URL.

## 🔮 Future Improvements

- Improve handling of chat before document upload
- Support additional document formats
- Improve document management
- Enhance retrieval accuracy
