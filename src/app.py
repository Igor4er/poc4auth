from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import CONFIG
from routers import email
from fastapi.staticfiles import StaticFiles


app = FastAPI(debug=CONFIG.debug)


app.mount("/static", StaticFiles(directory="./src/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(email.router)

