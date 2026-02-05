import json

from fastapi import FastAPI, Request, Body
from dotenv import load_dotenv

import Week_4.Task_02.constants as const
import Week_4.Task_02.methods as meth
import Week_4.Task_02.AI as AI



load_dotenv()


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
        meth.send_message(text, const.URL, chat_id)

    return {"ok": True}


@app.get("/chat/{chat_id}/messages/{message_id}")
async def get_message(
        chat_id: str,
        message_id: str
):
    message = meth.get_messages(chat_id, message_id)

    return {"ok": True, "message": message}

@app.put("/chat/{chat_id}/messages/{message_id}")
async def update_message(
        chat_id: str,
        message_id: str,
        payload: dict = Body()
):
    response = meth.upsert_message(payload["text"], message_id, const.URL, chat_id)
    return response

@app.delete("/chat/{chat_id}/messages/{message_id}")
async def delete_message(
        chat_id: str,
        message_id: str,
):
    response = meth.delete_message(message_id, const.URL, chat_id)
    return response


@app.get("/chat/{chat_id}/messages")
async def get_messages(chat_id: str):
    messages = meth.get_all_chat_messages(chat_id)
    return {"ok": True, "messages": messages}

@app.delete("/chat/{chat_id}/messages")
async def delete_messages(chat_id: str):
    with open(const.DB, "r") as f:
        db = json.load(f)

    for i in db:
        meth.delete_message(i["message_id"], const.URL, chat_id)

    return {"ok": True}