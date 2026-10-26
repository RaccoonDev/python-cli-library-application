import pytest

from cli_template import greet


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada."


def test_greet_excited() -> None:
    assert greet(" Ada ", excited=True) == "Hello, Ada!"


def test_greet_rejects_empty_name() -> None:
    with pytest.raises(ValueError, match="empty"):
        greet("   ")
