# Chatbot Backend (FastAPI + RAG)

The engine behind the TechPoint AI Chatbot. It handles document processing, vector storage, and AI communication.

## Tech Stack

- **Framework**: FastAPI
- **LLM Engine**: Ollama (Client API)
- **Vector Database**: ChromaDB
- **NLP/RAG**: LangChain & HuggingFace Embeddings
- **Models**: 
  - LLM: `qwen3:8b` (via Ollama)
  - Embeddings: `sentence-transformers/all-MiniLM-L6-v2`

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**:
   Create a `.env` file:
   ```env
   OLLAM_HOST_URL=http://localhost:11434
   ```

3. **Ingest Documents**:
   Place your `.pdf` files in the `docs/` folder and run:
   ```bash
   python ingest.py
   ```
   This will create a `chroma_db/` directory containing your vector embeddings.

4. **Run the Server**:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

- **POST `/chat`**: Accepts a list of messages and returns a RAG-augmented AI response.
  - Payload: `{ "messages": [{ "role": "user", "content": "Hello" }] }`
  - Response: `{ "reply": "..." }`
