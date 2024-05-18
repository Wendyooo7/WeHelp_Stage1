from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_HOST = os.getenv("DB_HOST")
DATABASE_USER = os.getenv("DB_USER")
DATABASE_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE_NAME = os.getenv("DB_NAME")

mydb = mysql.connector.connect(host=DATABASE_HOST,
                               user=DATABASE_USER,
                               password=DATABASE_PASSWORD,
                               database=DATABASE_NAME)

mycursor = mydb.cursor()

app = FastAPI()

# 添加SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="my-secret-key")

# 掛載靜態文件
app.mount("/static", StaticFiles(directory="static"), name="static")


# 通過添加快取控制標頭，禁止瀏覽器緩存 CSS 文件
@app.get("/styles.css")
async def get_styles():
    return FileResponse("styles.css", headers={"Cache-Control": "no-store"})


# 設置模板資料夾
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request,
                                      name="home.html",
                                      context={})


@app.post("/signup", response_class=HTMLResponse)
async def signup(request: Request,
                 name: str = Form(...),
                 username: str = Form(...),
                 password: str = Form(...)):
    sql = "SELECT username FROM member WHERE username = %s"
    # 上行原本寫成：sql = "SELECT username FROM website WHERE username = " + username，但因安全性考量，就不動態拼接
    mycursor.execute(sql, (username, ))
    myresult = mycursor.fetchone()

    if myresult == None:
        sql = "INSERT INTO member (name, username,password) VALUES (%s, %s, %s)"
        val = (name, username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        # print(mycursor.rowcount, "record inserted.")
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url="/error?message=帳號已存在，請改用其他帳號註冊，或以現有帳號登入",
                                status_code=status.HTTP_303_SEE_OTHER)


@app.post("/signin", response_class=HTMLResponse)
async def signin(request: Request,
                 username: str = Form(...),
                 password: str = Form(...)):
    print("來自前端的帳密: ", username, password)
    # 在帳密前面分別加BINARY是為了確保登入和註冊的帳密大小寫是完全相符的，因為SQL在查詢時會不分大小寫，但PY確實是大小寫敏感的，所以前端輸入的大小寫不會經過轉換，會被原封不動送到後端，所以註冊時送到資料庫的帳密會是使用者輸入的大小寫，登入時輸入的帳密也是使用者原始的大小寫
    sql = "SELECT id,name,username,password FROM member WHERE BINARY username = %s and BINARY password = %s"
    # 上行原本寫成：sql = "SELECT username FROM website WHERE username = " + username，但因安全性考量，就不動態拼接
    mycursor.execute(sql, (username, password))
    print("sql, (username, password): ", sql, (username, password))
    myresult = mycursor.fetchone()
    print("myresult: ", myresult)
    if myresult != None:
        # 設置用戶的登入狀態為True，並記錄會員的id,username和password
        request.session["signed_in"] = True
        request.session["id"] = myresult[0]
        request.session["name"] = myresult[1]
        request.session["username"] = myresult[2]

        return RedirectResponse(url="/member",
                                status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼輸入錯誤",
                                status_code=status.HTTP_303_SEE_OTHER)


def get_all_content():
    sql = "SELECT name, content FROM message JOIN member ON member.id = message.member_id"
    mycursor.execute(sql, )
    myresult = mycursor.fetchall()

    messages = []
    for item in myresult:
        message_dict = {"member_id": item[0], "content": item[1]}
        messages.append(message_dict)

    # 推導式寫法
    # messages = [{
    #     "member_id": item[0],
    #     "content": item[1]
    # } for item in myresult]

    print(messages)
    return messages


@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    # 檢查用戶的登入狀態
    if not request.session.get("signed_in", False):
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    # 獲取用戶名稱並傳遞給模板
    name = request.session.get("name")

    # 獲取所有會員的姓名和留言
    messages = get_all_content()  # 假設這是一個函數來從資料庫中獲取所有會員的留言

    # 將所有會員的留言傳遞給模板
    return templates.TemplateResponse(request=request,
                                      name="member.html",
                                      context={
                                          "name": name,
                                          "messages": messages
                                      })


@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, message: str):
    return templates.TemplateResponse(request=request,
                                      name="error.html",
                                      context={"message": message})


@app.get("/signout", response_class=HTMLResponse)
async def signout(request: Request):
    # 設置用戶的登入狀態為False
    request.session["signed_in"] = False
    request.session["id"] = None
    request.session["name"] = None
    request.session["username"] = None
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/createMessage", response_class=HTMLResponse)
async def create_message(request: Request, new_msg: str = Form(...)):

    member_id = request.session.get("id")
    sql = "INSERT INTO message (member_id, content) VALUES(%s, %s)"

    mycursor.execute(sql, (member_id, new_msg))
    mydb.commit()
    myresult = mycursor.fetchone()
    print(myresult)
    return RedirectResponse(url="/member",
                            status_code=status.HTTP_303_SEE_OTHER)


# Week7程式碼
@app.get("/api/member", response_model=dict)
async def query_member(request: Request, username: str = ...):
    # 檢查用戶的登入狀態
    if not request.session.get("signed_in", False):
        return {"data": None}

    sql = "SELECT id,name,username FROM member WHERE BINARY username = %s"
    mycursor.execute(sql, (username, ))
    # username後面要接,否則會產生bug

    myresult = mycursor.fetchone()
    # 因為myresult是tuple，所以才可用[i]來取值

    if myresult == None:
        return {"data": None}
    else:
        return {
            "data": {
                "id": myresult[0],
                "name": myresult[1],
                "username": myresult[2]
            }
        }


@app.patch("/api/member", response_model=dict)
async def update_member(request: Request):
    # 檢查用戶的登入狀態
    if not request.session.get("signed_in", False):
        return {"error": True}

    # 從request body拿到data
    data = await request.json()
    name = data.get("name")

    if not name:
        return {"error": True}

    original_name = request.session.get("name")
    sql = "UPDATE member SET name = %s  WHERE BINARY name = %s"

    try:
        mycursor.execute(sql, (name, original_name))
        mydb.commit()

        myresult = mycursor.rowcount
        if myresult == 0:
            return {"error": True}
        else:
            # 更新 session 中的 name
            request.session['name'] = name
            return {"ok": True}

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {"error": True}


if __name__ == "__main__":
    import uvicorn  # 這行也可以寫在本檔最頂
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
