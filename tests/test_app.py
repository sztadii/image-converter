from fastapi.testclient import TestClient
from src.app import app
from tests.helpers import open_file

client = TestClient(app)

def test_when_file_is_missing_then_throw_error():
    response = client.post("/invert")

    assert response.status_code == 422

def test_when_file_to_invert_was_send_properly_then_return_200_code():
    image = open_file("images/image.png")
    response = client.post("/invert", files={"file": image})

    assert response.status_code == 200

def test_when_file_was_send_then_invert_image_colors():
    image = open_file("images/image.png")
    inverted_image_sample = open_file("images/image_invert.png").read()
    response = client.post("/invert", files={"file": image})
    inverted_image_from_response = response.content

    assert inverted_image_sample == inverted_image_from_response

def test_when_file_to_rotate_was_send_properly_then_return_200_code():
    image = open_file("images/image.png")
    response = client.post("/rotate/90", files={"file": image})

    assert response.status_code == 200

def test_when_file_was_send_then_rotate_image():
    image = open_file("images/image.png")
    rotated_image_sample = open_file("images/image_180_deg.png").read()
    response = client.post("/rotate/180", files={"file": image})
    rotated_image_from_response = response.content

    assert rotated_image_sample == rotated_image_from_response

def test_when_file_to_mirror_was_send_properly_then_return_200_code():
    image = open_file("images/image.png")
    response = client.post("/mirror", files={"file": image})

    assert response.status_code == 200

def test_when_file_was_send_then_mirror_image():
    image = open_file("images/image.png")
    mirrored_image_sample = open_file("images/image_mirrored.png").read()
    response = client.post("/mirror", files={"file": image})
    mirrored_image_from_response = response.content

    assert mirrored_image_sample == mirrored_image_from_response

def test_when_file_to_grayscale_was_send_properly_then_return_200_code():
    image = open_file("images/image.png")
    response = client.post("/mirror", files={"file": image})

    assert response.status_code == 200

def test_when_file_was_send_then_grayscale_image():
    image = open_file("images/image.png")
    grayscale_image_sample = open_file("images/image_gray.png").read()
    response = client.post("/grayscale", files={"file": image})
    grayscale_image_from_response = response.content

    assert grayscale_image_sample == grayscale_image_from_response

# Tools like Postman will handle missing content-type header, but Swagger will not
def test_when_file_was_send_properly_then_return_image_header():
    image = open_file("images/image.png")
    response = client.post("/mirror", files={"file": image})
    content_type_header = response.headers["content-type"]

    assert content_type_header == "image/png"