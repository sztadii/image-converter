from fastapi import FastAPI, UploadFile, File, Response
import uvicorn
from image_converter import ImageConverter

app = FastAPI()

@app.post("/invert")
async def invert_image(file: UploadFile = File(...)):
    converter = ImageConverter(file.file)
    image_bytes = converter.invert()

    return Response(content=image_bytes, media_type="image/png")

uvicorn.run(app, host="0.0.0.0", port=4000)