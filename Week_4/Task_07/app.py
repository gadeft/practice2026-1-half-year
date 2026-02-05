import json
import os

from fastapi import FastAPI, Request, Body, HTTPException, Header
from dotenv import load_dotenv

import methods as meth
import AI as AI
import security as security



load_dotenv()
DB = os.getenv("DB")
URL = os.getenv("URL")
USERS = os.getenv("USERS")


app = FastAPI()

@app.post("/telegram")
async def telegram_webhook(req: Request):
    data = await req.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        # Two realisations. The chosen one works like echo. If you want the AI version create an API and paste into the evn
        # response = AI.ask_ai(text)
        # meth.send_message(response.text, const.URL, chat_id)

        text = f"You've written {text}"
        meth.send_message(text, URL, chat_id)

    return {"ok": True}


@app.get("/chat/{chat_id}/messages/{message_id}")
async def get_message(
        chat_id: str,
        message_id: str,
        token = Header()
):
    if not security.verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid JWT token")

    message = meth.get_messages(chat_id, message_id)

    return {"ok": True, "message": message}

@app.put("/chat/{chat_id}/messages/{message_id}")
async def update_message(
        chat_id: str,
        message_id: str,
        payload: dict = Body(),
        token = Header()
):
    if not security.verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid JWT token")

    response = meth.upsert_message(payload["text"], message_id, URL, chat_id)
    return response

@app.delete("/chat/{chat_id}/messages/{message_id}")
async def delete_message(
        chat_id: str,
        message_id: str,
        token = Header()
):
    if not security.verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid JWT token")

    response = meth.delete_message(message_id, URL, chat_id)
    return response


@app.get("/chat/{chat_id}/messages")
async def get_messages(
        chat_id: str,
        token = Header()
):
    if not security.verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid JWT token")

    messages = meth.get_all_chat_messages(chat_id)
    return {"ok": True, "messages": messages}

@app.delete("/chat/{chat_id}/messages")
async def delete_messages(
        chat_id: str,
        token = Header()
):
    if not security.verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid JWT token")

    with open(DB, "r") as f:
        db = json.load(f)

    for i in db:
        meth.delete_message(i["message_id"], URL, chat_id)

    return {"ok": True}


@app.post("/profile")
async def add_profile(payload: dict = Body()):
    print(payload["password"])
    data = {
        "username": payload["username"],
        "hashed_password": security.hash_password(payload["password"]),
    }

    with open(USERS, "r+") as f:
        users = json.load(f)
        if data in users:
            raise HTTPException(status_code=409, detail="User already exists")

        users.append(data)
        f.seek(0)
        json.dump(users, f, indent=2)

    return security.create_access_token(data)

@app.get("/profile")
async def get_profile(token = Header()):
    if not security.verify_token(token):
        return HTTPException(status_code=401, detail="Invalid JWT token")

    payload = security.decode_access_token(token)

    return meth.get_user(payload["username"], payload["hashed_password"])


