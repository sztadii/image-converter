from fastapi import FastAPI, UploadFile, File, Response
from src.image_converter import ImageConverter

app = FastAPI(docs_url="/")

@app.post("/invert")
def invert_image(file: UploadFile = File(...)):
    converter = ImageConverter(file.file)
    converter.invert()
    image_bytes = converter.get_image_bytes()

    return to_image_response(file.filename, image_bytes)

@app.post("/rotate/{angle}")
def rotate_image(angle: int, file: UploadFile = File(...)):
    converter = ImageConverter(file.file)
    converter.rotate(angle)
    image_bytes = converter.get_image_bytes()

    return to_image_response(file.filename, image_bytes)

@app.post("/mirror")
def mirror_image(file: UploadFile = File(...)):
    converter = ImageConverter(file.file)
    converter.mirror()
    image_bytes = converter.get_image_bytes()

    return to_image_response(file.filename, image_bytes)

@app.post("/grayscale")
def grayscale_image(file: UploadFile = File(...)):
    converter = ImageConverter(file.file)
    converter.grayscale()
    image_bytes = converter.get_image_bytes()

    return to_image_response(file.filename, image_bytes)

def to_image_response(filename: str, image_bytes: bytes):
    file_format = filename.split(".")[1]
    media_type = f"image/{file_format}"

    return Response(image_bytes, media_type=media_type)