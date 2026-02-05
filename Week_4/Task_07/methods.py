import json
import os

import requests
from dotenv import load_dotenv


load_dotenv()
DB = os.getenv("DB")
USERS = os.getenv("USERS")


def send_message(message_text, bot_url, chat_id):
    url = bot_url + "/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message_text,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=data).json()

    with open(DB, "r+") as f:
        db = json.load(f)
        db.append(response["result"])
        f.seek(0)
        json.dump(db, f, indent=2)

    return response

def edit_message(new_message_text, message_id, bot_url, chat_id):
    url = bot_url + "/editMessageText"
    data = {
        "chat_id": chat_id,
        "text": new_message_text,
        "message_id": message_id,
        "parse_mode": "HTML"
    }

    message = get_messages(chat_id, message_id)
    response = requests.post(url, json=data).json()

    if not response["ok"]:
        return response

    with open(DB, "r+") as f:
        db = json.load(f)

        db.remove(message[0])
        db.append(response["result"])

        f.seek(0)
        f.truncate()
        f.seek(0)
        json.dump(db, f, indent=2)

    return response

def upsert_message(message_text, message_id, bot_url, chat_id):
    response = edit_message(message_text, message_id, bot_url, chat_id)

    if not response["ok"]:
        response = send_message(message_text, bot_url, chat_id)
        return {"type": "created", "description": "The message did not exist so it was created.", "response": response}

    return {"type": "updated", "description": "Message was updated.", "response": response}

def delete_message(message_id, bot_url, chat_id):
    url = bot_url + "/deleteMessage"
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
    }
    description = "Deleted from chat and database"
    loc = ["chat", "database"]

    message = get_messages(chat_id, message_id)
    response = requests.post(url, data=data).json()
    if not response["ok"]:
        loc = ["database"]
        description = "Message is already deleted from chat, so deleted from database"

    if not message:
        return {"ok": True, "loc": [], "description": "Message is already deleted"}

    with open(DB, "r+") as f:
        db = json.load(f)
        db.remove(message[0])
        f.seek(0)
        f.truncate()
        f.seek(0)
        json.dump(db, f, indent=2)

    return {"ok": True, "loc": loc, "description": description}

def get_messages(chat_id, *message_ids):
    messages = []

    with open(DB, "r") as f:
        db = json.load(f)
        for i in range(len(db)):
            for message_id in message_ids:
                if int(db[i]["chat"]["id"]) != int(chat_id):
                    break

                if str(db[i]["message_id"]) == str(message_id):
                    messages.append(db[i])
                    break

    return messages


def get_all_chat_messages(chat_id):
    messages = []

    with open(DB, "r") as f:
        db = json.load(f)
        for i in range(len(db)):
            if db[i]["chat"]["id"] == int(chat_id):
                messages.append(db[i])

    return messages


def get_user(username, hashed_password):
    with open(USERS, "r") as f:
        users = json.load(f)

    for user in users:
        if user["username"] == username and user["hashed_password"] == hashed_password:
            return user

    return None
