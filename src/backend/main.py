import uvicorn
from fastapi import FastAPI, Form, Request, File, UploadFile, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import requests
import json
import logging
import os

serving_management_url = "http://torch:8081"
serving_inference_url = "http://torch:8080"
openai_completion_url = 'https://api.openai.com/v1/engines/davinci/completions'


logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

origins = ["http://localhost", "http://localhost:8080", "http://localhost:8081"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.mount("/static", StaticFiles(directory="./src/frontend/assets"), name="static")

templates = Jinja2Templates(directory="./src/frontend/templates")

@app.get("/models")
async def get_models():
    url = f"{serving_management_url}/models"
    logging.warning(url)
    resp = requests.get(url=url)
    logging.warning(resp)
    res = json.loads(resp.content)
    logging.warning(res)
    return res


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("/index.html", {"request": request})


@app.get("/test")
async def test():
    return {"msg": "Hello World"}


@app.post("/uploadfile/")
def create_upload_file(file: bytes = File(...)):

    model_name = "densenet161"

    try:
        req = requests.post(
            f"{serving_inference_url}/predictions/{model_name}", data=file
        )
        resp = json.loads(req.content.decode())
        return resp
    except Exception as e:
        logging.error(e)
        return {"error": "????"}


@app.post("/bullshit/")
async def generate_ticket(input_text: str = Form(...), word_count: int = Form(...)):
    req = requests.get(
        f"http://www.randomtext.me/api/gibberish/p-1/{word_count}-{word_count}"
    )
    resp = json.loads(req.content)
    return {"text": resp["text_out"][3:-6]}


@app.post("/v1/nlp/dummy/completions")
async def dummy_completions(prompt:str = Form(...),word_count:int=Form(...),temperature:float=Form(...),stream_result:bool=False):

    if stream_result:
        raise HTTPException(status_code=503, detail='streaming completion not yet implemented')

    headers = {
        'Authorization': 'dummy',
        'Content-Type': 'application/json'
    }

    body = {
        'prompt': prompt,
        'max_tokens': word_count,
        'temperature': temperature,
        'stream': stream_result
    }

    req = requests.get(
        f"http://www.randomtext.me/api/gibberish/p-1/{word_count}-{word_count}"
    )
    resp = json.loads(req.content)
    
    return {"text": resp["text_out"][3:-6]}


@app.post("/v1/nlp/gpt3/completions")
async def gpt3_completions(prompt:str = Form(...),word_count:int=Form(...),temperature:float=Form(...),stream_result:bool=False):
    if stream_result:
        raise HTTPException(status_code=503, detail='streaming completion not yet implemented')

    headers = {
        'Authorization': f'Bearer {os.getenv(openai_secret, "")}',
        'Content-Type': 'application/json'
    }

    body = {
        'prompt': prompt,
        'max_tokens': word_count,
        'temperature': temperature,
        'stream': stream_result
    }

    req = requests.post(openai_completion_url,data=body,headers=headers)

    if req.status_code!=200:
        raise HTTPException(status_code=req.status_code, detail='failed to retrieve completion from openai server')

    data = req.json()
    if 'choices' in data and data['choices']:
        return {'text':data['choices'][0]['text']}
    else:
        return {'text': ''}



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=80, log_level="info")
