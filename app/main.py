from fastapi import FastAPI
import py_eureka_client.eureka_client as eureka_client
from contextlib import asynccontextmanager

import constant
from schemas import Document, Summary
from utils import cleanhtml, clova_api

@asynccontextmanager
async def lifespan(app: FastAPI):
    await eureka_client.init_async(eureka_server=constant.EUREKA_SERVER,
                       app_name=constant.SERVICE_NAME,
                       instance_host=constant.SERVICE_IP,
                       instance_port=constant.SERVICE_PORT
                       )
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/summary", response_model=Summary)
async def get_summary(document:Document):
    title = document.title
    content = cleanhtml(document.content)

    result = clova_api(title, content)

    return result