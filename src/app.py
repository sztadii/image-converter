from fastapi import FastAPI, UploadFile, File, Response
from src.image_converter import ImageConverter

app = FastAPI()

@app.get("/")
async def index():
    return Response("image-converter")

@app.post("/invert")
async def invert_image(file: UploadFile = File(...)):
    converter = ImageConverter(file.file)
    converter.invert()
    image_bytes = converter.get_image_bytes()

    return Response(image_bytes)

@app.post("/rotate/{angle}")
async def rotate_image(angle: int, file: UploadFile = File(...)):
    converter = ImageConverter(file.file)
    converter.rotate(angle)
    image_bytes = converter.get_image_bytes()

    return Response(image_bytes)


