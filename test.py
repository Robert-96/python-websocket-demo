import random
import string

import pytest
import websockets


def random_word(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))


@pytest.mark.parametrize("message", [randon_word(10) for _ in range(10)])
def test_echo(message):
    with websockets.sync.client.connect("ws://127.0.0.1:7777") as websocket:
        websocket.send(message)
        response = await websocket.recv()

        response == message
