import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        x = await websocket.send({"action": "auth", "params": "api_key"})
        y = await websocket.recv()
        print(y)
        await websocket.send({"action": "subscribe", "params": "data_to_subscribe_to"})

asyncio.get_event_loop().run_until_complete(
    hello('wss://'))