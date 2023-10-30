from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client_id = ''
client_secret = ''

class Document(BaseModel):
    title: Optional[str] = None
    content: str

class Summary(BaseModel):
    summary: str

def clova_api(title, content):
    r = httpx.post(
        'https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize',
        json ={
            "document": {
                "title": title,
                "content": content,
            },
            "option": {
                "language": "ko",
                "model": "general",
                "tone": 0,
                "summaryCount": 3
            }
        },
        headers = {
            'Content-Type': 'application/json;UTF-8',
            'X-NCP-APIGW-API-KEY-ID': client_id,
            'X-NCP-APIGW-API-KEY': client_secret
        }
    )

    return json.loads(r.text)

@app.post("/summary", response_model=Summary)
async def get_summary(document:Document):
    title = document.title
    content = BeautifulSoup(document.content, 'lxml').text

    result = clova_api(title,content)

    return result
