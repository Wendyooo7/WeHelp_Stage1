from typing import Optional
from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="my-secret-key")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request,
                                      name="home.html",
                                      context={})


@app.post("/signin", response_class=HTMLResponse)
async def signin(request: Request,
                 username: Optional[str] = Form(None),
                 password: Optional[str] = Form(None)):
    if not username or not password:
        return RedirectResponse(url="/error?message=請輸入帳號或密碼",
                                status_code=status.HTTP_303_SEE_OTHER)

    if username != "test" or password != "test":
        return RedirectResponse(url="/error?message=帳號或密碼不正確",
                                status_code=status.HTTP_303_SEE_OTHER)

    request.session["signed_in"] = True

    return RedirectResponse(url="/member",
                            status_code=status.HTTP_303_SEE_OTHER)


@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    if not request.session.get("signed_in", False):
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    return templates.TemplateResponse(request=request,
                                      name="member.html",
                                      context={})


@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, message: str):
    return templates.TemplateResponse(request=request,
                                      name="error.html",
                                      context={"message": message})


@app.get("/signout", response_class=HTMLResponse)
async def signout(request: Request):
    request.session["signed_in"] = False

    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


if __name__ == "__main__":
    import uvicorn  # 這行也可以寫在本檔最頂
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
