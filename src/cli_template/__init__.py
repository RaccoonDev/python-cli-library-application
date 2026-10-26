"""cli_template: a reusable library with an optional command-line interface."""

from importlib.metadata import PackageNotFoundError, version

from cli_template.core import greet

try:
    __version__ = version("cli-template")
except PackageNotFoundError:  # pragma: no cover - running from an uninstalled checkout
    __version__ = "0.0.0"

__all__ = ["__version__", "greet"]
