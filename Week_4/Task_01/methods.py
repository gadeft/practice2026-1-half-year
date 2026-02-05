import requests

from Week_4.Task_01.constants import *


def send_message(message_text, bot_url, chat_id):
    url = bot_url + "/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message_text
    }

    response = requests.post(url, data=data)
    return response.json()

def edit_message(new_message_text, message_id, bot_url, chat_id):
    url = bot_url + "/editMessageText"
    data = {
        "chat_id": chat_id,
        "text": new_message_text,
        "message_id": message_id,
    }

    response = requests.post(url, data=data)
    return response.json()

def delete_message(message_id, bot_url, chat_id):
    url = bot_url + "/deleteMessage"
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
    }

    response = requests.post(url, data=data)
    return response.json()
