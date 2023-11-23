import random
import string

import pytest
import websockets


def random_word(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))


@pytest.mark.parametrize("message", [randon_word(10) for _ in range(10)])
def test_echo(message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()

        assert response == message
