from fastapi import FastAPI, UploadFile, File, Response
import uvicorn
from image_converter import ImageConverter

app = FastAPI()

@app.post("/invert")
async def invert_image(file: UploadFile = File(...)):
    converter = ImageConverter(file.file)
    image_bytes = converter.invert()

    return Response(image_bytes)

@app.post("/rotate/{angle}")
async def rotate_image(angle: int, file: UploadFile = File(...)):
    converter = ImageConverter(file.file)
    image_bytes = converter.rotate(angle)

    return Response(image_bytes)

uvicorn.run(app, host="0.0.0.0", port=4000)