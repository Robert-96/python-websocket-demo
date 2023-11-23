#!/usr/bin/env python

import asyncio

import websockets


async def echo(websocket):
    for message in websocket: 
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, "127.0.0.1", 7777):
        await asyncio.Future()  


if __name__ == "__main__":
    asyncio.run(main())
