# TechPoint AI Chatbot

A full-stack RAG (Retrieval-Augmented Generation) chatbot designed for "TechPoint Computers". This application uses a FastAPI backend with Ollama for intelligent responses and a React-based "glassmorphism" frontend.

## Project Structure

- **`chatbot-backend/`**: FastAPI server, document ingestion logic, and vector database (ChromaDB).
- **`chatbot-ui/`**: React frontend built with Vite, featuring a premium glassmorphism design.
- **`docs/`**: (In backend) Place your PDF knowledge base files here for ingestion.

## Key Features

- **RAG Integration**: Queries a local ChromaDB vector store for context-aware answers.
- **Ollama Backend**: Uses the Qwen 3: 8b model (configurable) for high-quality AI responses.
- **Glassmorphism UI**: A modern, transparent, and responsive interface.
- **Markdown Support**: Beautifully formatted responses including tables, lists, and code blocks.

## Getting Started

### Prerequisites

- [Python 3.10+](https://www.python.org/)
- [Node.js & npm](https://nodejs.org/)
- [Ollama](https://ollama.com/) (running locally)

### Setup Instructions

1. **Backend Setup**:
   - Navigate to `chatbot-backend/`.
   - Install dependencies: `pip install -r requirements.txt`.
   - Place your PDFs in `chatbot-backend/docs/`.
   - Run ingestion: `python ingest.py`.
   - Start the server: `uvicorn main:app --reload`.

2. **Frontend Setup**:
   - Navigate to `chatbot-ui/`.
   - Install dependencies: `npm install`.
   - Start the dev server: `npm run dev`.

3. **Environment Configuration**:
   - In `chatbot-backend/`, copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Update `OLLAM_HOST_URL` in `.env` if necessary.

## License

MIT
