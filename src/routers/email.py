from fastapi import APIRouter, Request, WebSocket, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from asyncio import sleep
import jwt
import resend
import time
from config import CONFIG


PREFIX = "/email"
router = APIRouter(prefix=PREFIX)
templates = Jinja2Templates(directory="./src/templates"+PREFIX)


resend.api_key = CONFIG.RESEND_TOKEN.get_secret_value()


ACTIVE_SOCKETS = {}
CONFIRMED_EMAILS = []


async def send_confirmation_email_to(request: Request, email: str) -> bool:
    token = jwt.encode({"email": email, "exp": int(time.time()) + 2*60*60}, key=CONFIG.JWT_SECRET.get_secret_value())

    tmp = templates.get_template("inbox.html")
    html = tmp.render(request=request, token=token)

    params = {
        "from": CONFIG.FROM_MAIL,
        "to": [email],
        "subject": "Підтвердження від POC4Auth",
        "html": html
    }
    try:
        email = resend.Emails.send(params=params)
        print("WEMAIL", email)
    except Exception as E:
        print("EXCEPTION", E)
        return False
    return True


@router.websocket("/ws")
async def ws_handle_email( ws: WebSocket):
    await ws.accept()
    email = await ws.receive_text()
    sent = await send_confirmation_email_to(ws, email)
    if not sent:
        print("NOT SENT")
        await ws.send_text("failed")
        await ws.close()
        return
    ACTIVE_SOCKETS[email] = ws
    while True:
        print("CONFIRMED_EMAILS", CONFIRMED_EMAILS)
        if email in CONFIRMED_EMAILS:
            print("sent success")
            await ws.send_text("success")

            CONFIRMED_EMAILS.remove(email)
            del ACTIVE_SOCKETS[email]

            await ws.close()
            return {}
        try:
            print("sent await")
            await ws.send_text("await")
            await sleep(5)
        except:
            del ACTIVE_SOCKETS[email]


@router.get("")
async def index_email(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={}
)

@router.get("/cfirm")
async def confirm_email(request: Request, token: str):
    try:
        tok = jwt.decode(token, key=CONFIG.JWT_SECRET.get_secret_value(), algorithms=["HS256"])
    except Exception as E:
        print("NOt CONFIREMD", E)
        return JSONResponse(status_code=status.HTTP_408_REQUEST_TIMEOUT, content={"msg": "Email не було підтверджено. Спробуйте ще раз."})
    email = tok["email"]
    CONFIRMED_EMAILS.append(email)
    return {"msg": "Email підтверджено! Ви можете покинути сторінку"}

@router.get("/confirm")
async def confirm_email_page(request: Request, token: str = "NOTOKEN"):
    return templates.TemplateResponse(
        request=request, name="confirm_email.html", context={"token": token}
    )

