from fastapi import FastAPI
from pydantic import BaseModel
from main import get_answer

app = FastAPI()

class Question(BaseModel):
    query: str

@app.post("/query")
def ask_question(q: Question):
    try:
        answer = get_answer(q.query)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
