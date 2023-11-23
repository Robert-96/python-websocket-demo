#!/usr/bin/env python

import asyncio

import websockets


async def echo(websocket):
    print(">>> Connected")
    async for message in websocket:
        print(f">>> Received: {message}")
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, "127.0.0.1", 7777):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
