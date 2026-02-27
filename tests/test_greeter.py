import pytest
from src.greeter import greet

def test_greet_ok():
    assert greet("Pepe") == "Hola, Pepe!"

def test_greet_empty_name_raises():
    with pytest.raises(ValueError):
        greet("")
