import pytest

from src.main import greet


def test_greet() -> None:
    assert greet("world") == "Hello, world."


def test_greet_raises_type_error_for_non_string_name() -> None:
    with pytest.raises(TypeError):
        greet(123)  # type: ignore[arg-type]
