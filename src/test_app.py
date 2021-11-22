from fastapi.testclient import TestClient
from app import app

def test_read_main():
    client = TestClient(app)
    response = client.post("/invert")

    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}