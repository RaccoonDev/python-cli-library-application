"""Typer application. Commands here should only parse input and call the library."""

from dataclasses import dataclass
from typing import Annotated, Protocol

import typer

from cli_template import __version__, greet

app = typer.Typer(no_args_is_help=True, help="Example CLI built on the cli_template library.")


class Greeter(Protocol):
    def __call__(self, name: str, *, excited: bool = ...) -> str: ...


@dataclass(frozen=True)
class Deps:
    """Services the commands depend on.

    The real ones are used by default. Tests hand in fakes with
    ``CliRunner().invoke(app, [...], obj=Deps(greet=fake))``. Add HTTP clients,
    clocks, config and similar here as the CLI grows.
    """

    greet: Greeter = greet


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit


@app.callback()
def root(
    ctx: typer.Context,
    version: Annotated[
        bool,
        typer.Option(
            "--version", callback=_version_callback, is_eager=True, help="Show version and exit."
        ),
    ] = False,
) -> None:
    """Example CLI built on the cli_template library."""
    if ctx.obj is None:
        ctx.obj = Deps()


@app.command()
def hello(
    ctx: typer.Context,
    name: Annotated[str, typer.Argument(help="Who to greet.")],
    excited: Annotated[bool, typer.Option("--excited", "-e", help="End with '!'.")] = False,
) -> None:
    """Print a greeting."""
    deps: Deps = ctx.obj
    try:
        typer.echo(deps.greet(name, excited=excited))
    except ValueError as exc:
        raise typer.BadParameter(str(exc), param_hint="NAME") from exc
