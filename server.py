from fastapi import FastAPI, Request
from pydantic import BaseModel
from educhain_tools.generator import generate_mcqs, generate_lesson_plan
from fastapi.responses import JSONResponse

app = FastAPI()

class MCQRequest(BaseModel):
    topic: str
    num: int = 5

class LessonPlanRequest(BaseModel):
    topic: str

@app.post("/mcq")
async def mcq_endpoint(req: MCQRequest):
    result = generate_mcqs(req.topic, req.num)
    try:
        return JSONResponse(content=result if isinstance(result, dict) else eval(result))
    except Exception:
        return JSONResponse(content={"raw": result})

@app.post("/lesson")
async def lesson_endpoint(req: LessonPlanRequest):
    result = generate_lesson_plan(req.topic)
    try:
        return JSONResponse(content=result if isinstance(result, dict) else eval(result))
    except Exception:
        return JSONResponse(content={"raw": result})

@app.get("/")
def root():
    return {"message": "EduChain MCP FastAPI server is running."} 