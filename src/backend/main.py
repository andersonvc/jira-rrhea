import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="./src/frontend/assets"), name="static")



templates = Jinja2Templates(directory="./src/frontend/templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/test")
async def root():
    return {"msg": "Hello World"}


@app.post("/login/")
async def login(username:str = Form(...), password: str = Form(...)):
    return {"username":username}

@app.post("/bullshit/")
async def generate_ticket(input_text:str=Form(...),word_count: int = Form(...)):
    req = requests.get(f'http://www.randomtext.me/api/gibberish/p-1/{word_count}-{word_count}')
    resp = json.loads(req.content)
    return {'text':resp['text_out'][3:-6]}



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5555, log_level="info")
