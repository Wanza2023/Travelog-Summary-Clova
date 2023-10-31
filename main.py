from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import Document, Summary
from utils import cleanhtml, clova_api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summary", response_model=Summary)
async def get_summary(document:Document):
    title = document.title
    content = cleanhtml(document.content)

    result = clova_api(title, content)

    return result