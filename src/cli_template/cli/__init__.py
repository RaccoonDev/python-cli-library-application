"""Command-line entry point.

Typer is imported lazily so the library stays usable without the ``cli`` extra.
"""


def main() -> None:
    try:
        from cli_template.cli.app import app
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on installed extras
        if exc.name != "typer":
            raise
        raise SystemExit(
            "The command-line interface needs extra dependencies: pip install 'cli-template[cli]'"
        ) from exc
    app()
