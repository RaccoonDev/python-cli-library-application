# python-cli-library-application

Template for a Python library with an optional command-line interface, managed with [uv](https://docs.astral.sh/uv/).

## Layout

```
src/cli_template/
├── __init__.py     # public library API
├── core.py         # library logic, no CLI imports
├── py.typed        # ships type hints
├── __main__.py     # python -m cli_template
└── cli/
    ├── __init__.py # console-script entry point (imports Typer lazily)
    └── app.py      # Typer commands: parse input, call the library
tests/              # library and CLI tests
```

The library has no runtime dependencies. Typer lives in the `cli` extra:

```sh
pip install cli-template          # library only
pip install 'cli-template[cli]'   # library + cli-template command
```

## Development

```sh
uv sync                       # create .venv with dev tools
uv run cli-template hello Ada # run the CLI
uv run pytest                 # tests with coverage
uv run ruff check && uv run ruff format --check
uv run mypy
uv run pre-commit install     # run lint and type checks on commit
uv build                      # build sdist and wheel into dist/
```

## Testing the CLI with fakes

Commands get their services from a `Deps` object on Typer's context (`ctx.obj`), not from module-level imports. The root callback fills in the real `Deps()` when nothing was passed, so normal runs need no setup. Tests pass their own:

```python
from typer.testing import CliRunner
from cli_template.cli.app import Deps, app


def fake_greet(name: str, *, excited: bool = False) -> str:
    return "stubbed"


result = CliRunner().invoke(app, ["hello", "Ada"], obj=Deps(greet=fake_greet))
assert result.stdout.strip() == "stubbed"
```

When the CLI needs an HTTP client, a clock or config, add a field to `Deps` instead of patching. Keep library tests in `tests/test_core.py` free of the CLI, so fakes are only needed at the edges.

## Using this template

Rename `cli_template` / `cli-template` to your project's name in `pyproject.toml`, `src/`, `tests/`, and this README, then run `uv lock`.
