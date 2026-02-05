from fastapi import FastAPI, Request
from dotenv import load_dotenv

import Week_4.Task_01.constants as const
import Week_4.Task_01.methods as meth
import Week_4.Task_01.AI as AI



load_dotenv()


app = FastAPI()

@app.post("/telegram")
async def telegram_webhook(req: Request):
    data = await req.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        # Two realisations. The choosen one works like echo. If you want the AI version create an API and paste into the evn
        # response = AI.ask_ai(text)
        # meth.send_message(response.text, const.URL, chat_id)

        text = f"You've written {text}"
        meth.send_message(text, const.URL, chat_id)

    return {"ok": True}

