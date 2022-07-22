import uvicorn
import os
from src.app import app

port = os.environ.get('PORT') or 8000
uvicorn.run(app, host="0.0.0.0", port=port)
