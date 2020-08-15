import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging
import os

from backend.routers import nlp, cv, info


app = FastAPI()
app.include_router(nlp.router, prefix="/v1/nlp", tags=["nlp"])
app.include_router(cv.router, prefix="/v1/cv", tags=["cv"])
app.include_router(info.router, prefix="/v1/info", tags=['info'])



origins = ["http://localhost", "http://localhost:8080", "http://localhost:8081", "http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/test")
def test():
    return {'msg':'Hello World'}



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=80, log_level="info")
