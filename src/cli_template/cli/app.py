"""Typer application. Commands here should only parse input and call the library."""

from typing import Annotated

import typer

from cli_template import __version__, greet

app = typer.Typer(no_args_is_help=True, help="Example CLI built on the cli_template library.")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit


@app.callback()
def root(
    version: Annotated[
        bool,
        typer.Option(
            "--version", callback=_version_callback, is_eager=True, help="Show version and exit."
        ),
    ] = False,
) -> None:
    """Example CLI built on the cli_template library."""


@app.command()
def hello(
    name: Annotated[str, typer.Argument(help="Who to greet.")],
    excited: Annotated[bool, typer.Option("--excited", "-e", help="End with '!'.")] = False,
) -> None:
    """Print a greeting."""
    try:
        typer.echo(greet(name, excited=excited))
    except ValueError as exc:
        raise typer.BadParameter(str(exc), param_hint="NAME") from exc
