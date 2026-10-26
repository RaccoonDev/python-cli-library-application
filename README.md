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

## Using this template

Rename `cli_template` / `cli-template` to your project's name in `pyproject.toml`, `src/`, `tests/`, and this README, then run `uv lock`.
