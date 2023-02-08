# ninja_demo / urls.py
# Created by azat at 8.02.2023
from ninja import NinjaAPI

api = NinjaAPI()


@api.post("/")
def ping(request, msg: str):
    if msg == "ping":
        return {"ping": "pong"}
    else:
        return {"error": "Invalid message"}
