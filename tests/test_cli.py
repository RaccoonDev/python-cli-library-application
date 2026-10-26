from typer.testing import CliRunner

from cli_template import __version__
from cli_template.cli.app import app

runner = CliRunner()


def test_version() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert result.stdout.strip() == __version__


def test_hello() -> None:
    result = runner.invoke(app, ["hello", "Ada", "--excited"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello, Ada!"


def test_hello_rejects_empty_name() -> None:
    result = runner.invoke(app, ["hello", " "])
    assert result.exit_code != 0
