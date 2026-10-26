"""Core library logic. Keep this module free of CLI concerns."""


def greet(name: str, *, excited: bool = False) -> str:
    """Return a greeting for ``name``.

    >>> greet("Ada")
    'Hello, Ada.'
    """
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}{'!' if excited else '.'}"
