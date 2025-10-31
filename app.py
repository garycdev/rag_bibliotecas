import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=HOST, port=PORT, workers=int(os.getenv("WORKERS", 4)))
