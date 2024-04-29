import uvicorn
from app import app
from config import CONFIG


if __name__ == "__main__":
    uvicorn.run("main:app", reload=CONFIG.debug)
