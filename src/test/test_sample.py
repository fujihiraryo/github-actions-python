from src.main.sample import say_hello, plus


def test_say_hello():
    assert say_hello() == "hello"


def test_plus():
    assert plus(1, 1) == 0
