# coding=utf-8
from fastapi import FastAPI
import requests
from pydantic import BaseSettings

class Settings(BaseSettings):
    access_token: str
    dev_id: str

settings = Settings()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/cmd")
def notify_cmd(err: int = None):
    if err == 0:
        body = "Succeeded ✨"
    else:
        body = "Failed 💀"

    url = 'https://api.pushbullet.com/v2/pushes'
    headers = {'Content-Type': 'application/json',
               'Access-Token': settings.access_token}

    payload = {'body': body, 'title': 'Command Finished',
               'type': 'note', 'device_iden': settings.dev_id}

    r = requests.post(url, headers=headers, json=payload)
    if(r.status_code == 200):
        return "Sent Notification"
    else:
        return r.text