from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import get_llm_reply

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(req: ChatRequest):
    reply = get_llm_reply(req.message)
    return {"reply": reply}
