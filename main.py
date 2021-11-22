from fastapi import FastAPI, UploadFile, File, Response
from PIL import Image, ImageOps
import uvicorn
from io import BytesIO

app = FastAPI()

@app.post("/invert")
async def invert_image(file: UploadFile = File(...)):
    image = Image.open(file.file)
    inverted_image = ImageOps.invert(image.convert("RGB"))

    buffer = BytesIO()
    inverted_image.save(buffer, format="png")
    image_bytes = buffer.getvalue()

    return Response(content=image_bytes, media_type="image/png")

uvicorn.run(app, host="0.0.0.0", port=4000)