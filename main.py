from fastapi import FastAPI
from pydantic import BaseModel
from app.tutor_agent import get_ai_tutor_response

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
async def root():
    return {"message": "AI Tutor API is running."}

@app.post("/ask")
async def ask_tutor(request: QueryRequest):
    response = get_ai_tutor_response(request.query)
    return {"response": response}
