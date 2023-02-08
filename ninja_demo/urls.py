# ninja_demo / urls.py
# Created by azat at 8.02.2023
from ninja import NinjaAPI
from ninja_demo.routers import sync_endpoints, async_endpoints

api = NinjaAPI()
api.add_router("", sync_endpoints.router, tags=['sync'])
api.add_router("", async_endpoints.router, tags=['async'])


@api.post("/")
def ping(request, msg: str):
    if msg == "ping":
        return {"ping": "pong"}
    else:
        return {"error": "Invalid message"}
