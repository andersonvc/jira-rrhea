from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
