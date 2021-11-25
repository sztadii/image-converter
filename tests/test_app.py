from fastapi.testclient import TestClient
from src.app import app
import os

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

# To run pytest from the root then we need to use absolute path
# To open file easier we can use below function
def open_file(path: str):
    current_dir = os.path.dirname(__file__)
    absolute_path = os.path.join(current_dir, path)
    return open(absolute_path, "rb")