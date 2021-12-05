import uvicorn
import os
from src.app import app

port = os.environ.get('PORT') or 4000
uvicorn.run(app, port=port)