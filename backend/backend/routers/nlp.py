from fastapi import APIRouter, HTTPException,  Form
import json
import requests
import openai

from ..configs import logger, settings

router = APIRouter()
openai.api_key = settings.openai_secret_key

@router.post("/dummy/completions")
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


@router.post("/gpt3/completions")
async def gpt3_completions(prompt:str = Form(...),word_count:int=Form(...),temperature:float=Form(...),stream_result:bool=False):
    if stream_result:
        raise HTTPException(status_code=503, detail='streaming completion not yet implemented')
    
    preamble = "I am a software engineer and I am writing a description of a new feature I want to implement for a web application. I am designing this feature in Angular JS and I have deep understanding of all facets of web development. I am writing a Jira ticket that outlines software activites around user authentication with an OAuth plugin."
    default_text = " "
    text_input = preamble + prompt if prompt else default_text

    resp = openai.Completion.create(engine="davinci", prompt=text_input, max_tokens=word_count,temperature=temperature)
    try:
        output = resp['choices'][0]['text']
        return {'text':output}
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail='OpenAI backend query failed')


@router.post("/gpt3/jira")
async def gpt3_completions(jira_title:str=Form(...),word_count:int=Form(...),temperature:float=Form(...)):
    
    jira_text= ["A team of software developers are discussing the work needed to complete various software tasks. Each user is given a problem statement and they are asked to define how they would complete the work."
          "Program Manager: What would you use to design our web-app's login screen?",
          "Developer: I am going to use an Angular template that incorporates an OAuth interface to our SSO authentication service. The design of the component relies on Material UI and the code for logging in the user is written in Javascript.",
          "Program Manager: What are you going to do to handle Two Factor Authentication?",
          "Developer: I first need to set up a ReCAPTCHA verifier through Google, which allows me to send SNS messages to the end user. I then need to create an interface, which allows the user to assign a phone number to their account for 2FA. I then need to implement a 2FA service using an existing AWS platform.",
          f"Program Manager: {jira_title}","Developer: "]

    resp = openai.Completion.create(engine="davinci", prompt=jira_text, max_tokens=word_count,temperature=temperature)
    try:
        output = resp['choices'][0]['text']
        return {'text':output}
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail='OpenAI backend query failed')