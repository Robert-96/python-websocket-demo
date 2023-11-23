import random
import string

from websockets.sync.client import connect


def random_word(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))


def test_echo():
    with connect("ws://127.0.0.1:7777") as websocket:
        for message in (random_word(10) for _ in range(10)):
            websocket.send(message)
            response = websocket.recv()

            response == message
