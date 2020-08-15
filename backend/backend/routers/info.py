from fastapi import APIRouter, HTTPException,  Form, File
import json
import requests

from backend.configs import settings, logger

router = APIRouter()

@router.get("/models")
async def get_models():
    url = f"{settings.serving_management_url}/models"
    try:
        resp = requests.get(url=url)
        logger.warning(resp)
        res = json.loads(resp.content)
    except Exception as e:
        logger.error(f"Error\n{e}")
        raise HTTPException(status_code=500, detail="Failed to connect to torchserving")
    return res
