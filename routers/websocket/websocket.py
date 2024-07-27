from fastapi import APIRouter, FastAPI, WebSocket, WebSocketDisconnect
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
import asyncio

from websockets import ConnectionClosed

from data.usecases.product.find_all import FindAllUseCase

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try: 
        while True:
            await asyncio.sleep(1)
            payload =  FindAllUseCase().find_all()
            await websocket.send_json(jsonable_encoder(payload))
    except (WebSocketDisconnect, ConnectionClosed):
        print("Client disconnected")
    finally:
        websocket.close()