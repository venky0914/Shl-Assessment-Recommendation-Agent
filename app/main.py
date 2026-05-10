from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.agent import generate_response

app = FastAPI()


# Request models
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


# Health endpoint
@app.get("/health")
def health_check():

    return {
        "status": "ok"
    }


# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):

    # Get latest user message
    latest_message = request.messages[-1].content

    response = generate_response(latest_message)

    return response