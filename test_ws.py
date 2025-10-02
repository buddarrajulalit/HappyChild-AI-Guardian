import asyncio
import websockets
import json

async def test_ws():
    uri = "ws://127.0.0.1:8000/alerts/"
    async with websockets.connect(uri) as websocket:
        # Receive connection message
        message = await websocket.recv()
        print("Server:", message)

        # Send a test alert message
        await websocket.send("This is a test alert from client")
        response = await websocket.recv()
        print("Server:", response)

asyncio.run(test_ws())

