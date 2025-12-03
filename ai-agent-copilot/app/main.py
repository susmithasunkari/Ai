from fastapi import FastAPI
from pydantic import BaseModel
from app.agent.agent import run_agent

app = FastAPI(title="AI Agent Copilot")

class Query(BaseModel):
    question: str
    user_id: str

@app.post("/ask")
def ask(q: Query):
    answer, sources = run_agent(q.question, q.user_id)
    return {"answer": answer, "sources": sources}
