from fastapi import APIRouter, HTTPException,  Form, File
import json
import requests

from ..configs import logger,settings

router = APIRouter()


@router.post("/densenet161/classify")
def create_upload_file(file: bytes = File(...)):

    model_name = "densenet161"

    try:
        req = requests.post(
            f"{settings.serving_inference_url}/predictions/{model_name}", data=file
        )
        resp = json.loads(req.content.decode())
        return resp
    except Exception as e:
        print(e)
        logger.error(e)
        return {"error": "????"}