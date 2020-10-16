import os
from src.main.sample import say_hello
import time


os.listdir()
time.time()


def test_say_hello():
    assert say_hello() == "hello"
