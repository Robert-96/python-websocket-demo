import random
import string

import pytest
from websockets.sync.client import connect


def random_word(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))


@pytest.mark.parametrize("message", [random_word(10) for _ in range(10)])
def test_echo(message):
    with connect("ws://127.0.0.1:7777") as websocket:
        websocket.send(message)
        response = websocket.recv()

        response == message
