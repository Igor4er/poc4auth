from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
import time
from config import CONFIG


PREFIX = ""
router = APIRouter(prefix=PREFIX)

@router.get("/")
async def to_mail(request: Request):
    return RedirectResponse(request.url_for("index_email"))
