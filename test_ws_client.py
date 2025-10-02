import asyncio
import websockets

async def listen():
    uri = "ws://127.0.0.1:8000/alerts/"
    async with websockets.connect(uri) as websocket:
        print("✅ Connected to WebSocket server. Waiting for alerts...")
        while True:
            msg = await websocket.recv()
            print(f"📩 Alert received: {msg}")

if __name__ == "__main__":
    asyncio.run(listen())
