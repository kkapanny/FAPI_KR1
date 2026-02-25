from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import models  

app = FastAPI()

user = models.User(
    name="Анна Капустинская",
    id=1
)

feedback_storage = []

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_path = Path("index.html")
    if html_path.exists():
        return html_path.read_text(encoding="utf-8")
    else:
        return HTMLResponse(content="<h1>Файл index.html не найден</h1>", status_code=404)

@app.get("/users")
async def get_user():
    return user

@app.post("/feedback")
async def create_feedback(feedback: models.Feedback):
    feedback_storage.append(feedback)
    
    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }

@app.get("/feedback")
async def get_all_feedback():
    return {
        "total_feedback": len(feedback_storage),
        "feedback": feedback_storage
    }