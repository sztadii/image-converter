from fastapi.testclient import TestClient
from src.app import app
from tests.helpers import open_file

def test_throw_the_error_when_the_image_is_missing():
    client = TestClient(app)
    response = client.post("/invert")

    assert response.status_code == 422

def test_when_send_the_image_then_return_200_status_code():
    client = TestClient(app)

    image = open_file("images/image.png")
    response = client.post("/invert", files={"file": image})

    assert response.status_code == 200

def test_invert_image():
    client = TestClient(app)

    image = open_file("images/image.png")
    inverted_image_sample = open_file("images/image_invert.png").read()
    response = client.post("/invert", files={"file": image})
    inverted_image_from_response = response.content

    assert inverted_image_sample == inverted_image_from_response

def test_rotate_image():
    client = TestClient(app)

    image = open_file("images/image.png")
    rotated_image_sample = open_file("images/image_180_deg.png").read()
    response = client.post("/rotate/180", files={"file": image})
    rotated_image_from_response = response.content

    assert rotated_image_sample == rotated_image_from_response