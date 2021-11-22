from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/invert")
async def invert_image():
    return "OK"

uvicorn.run(app, host="0.0.0.0", port=4000)