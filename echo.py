#!/usr/bin/env python

import asyncio
import http
import os
import signal

import websockets


async def echo(websocket):
    print(">>> Connected")
    async for message in websocket:
        print(f">>> Received: {message}")
        await websocket.send(message)


async def health_check(path, request_headers):
    if path == "/healthz":
        return http.HTTPStatus.OK, [], b"OK\n"


async def main():
    host = os.environ.get("WS_HOST", "127.0.0.1").strip()
    port = os.environ.get("WS_PORT", 7777)

    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)
    
    async with websockets.serve(echo, host, port, process_request=health_check):
        await stop


if __name__ == "__main__":
    asyncio.run(main())
