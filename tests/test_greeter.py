import pytest
from src.greeter import greet


def test_default_greeting():
    assert greet("Pepe") == "Hola, Pepe!"


def test_morning():
    assert greet("Pepe", 8) == "Buenos días, Pepe!"


def test_afternoon():
    assert greet("Pepe", 15) == "Buenas tardes, Pepe!"


def test_night():
    assert greet("Pepe", 22) == "Buenas noches, Pepe!"


def test_invalid_hour():
    with pytest.raises(ValueError):
        greet("Pepe", 25)


def test_empty_name():
    with pytest.raises(ValueError):
        greet("")
