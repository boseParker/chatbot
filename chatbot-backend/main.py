import os

import ollama

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from rag import search_docs

# Load env
load_dotenv()

# Ollama Client
client = ollama.Client(
    host=os.getenv("OLLAM_HOST_URL")
)

# FastAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

# Chat API
@app.post("/chat")
async def chat(req: ChatRequest):

    try:

        latest_message = req.messages[-1].content

        # RAG Search
        context = search_docs(latest_message)

        # System Prompt
        system_prompt = f"""
You are an expert AI assistant for "TechPoint Computers". 

STRICT RULES:
1. ONLY use the provided "KNOWLEDGE BASE" below to answer questions.
2. If the answer is NOT in the KNOWLEDGE BASE, say: "I'm sorry, I don't have that specific information in my current database. Please contact TechPoint support at 9876543210 for more details."
3. Do NOT use your own internal knowledge to make up prices, specs, or services.
4. Always provide information in a beautiful, structured "Product Showcase" format.

KNOWLEDGE BASE:
{context}
"""

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        # Add conversation history
        for msg in req.messages:

            messages.append({
                "role": msg.role,
                "content": msg.content
            })

        response = client.chat(
            model="qwen3:8b",
            messages=messages,
            options={
                "temperature": 0.5,
                "num_predict": 1500
            }
        )

        return {
            "reply": response["message"]["content"]
        }

    except Exception as e:

        return {
            "reply": f"Error: {str(e)}"
        }