from typer.testing import CliRunner

from cli_template import __version__
from cli_template.cli.app import Deps, app

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


def test_hello_with_injected_greeter() -> None:
    calls: list[tuple[str, bool]] = []

    def fake_greet(name: str, *, excited: bool = False) -> str:
        calls.append((name, excited))
        return "stubbed"

    result = runner.invoke(app, ["hello", "Ada", "-e"], obj=Deps(greet=fake_greet))
    assert result.exit_code == 0
    assert result.stdout.strip() == "stubbed"
    assert calls == [("Ada", True)]


def test_hello_reports_library_errors_as_bad_parameter() -> None:
    def failing_greet(name: str, *, excited: bool = False) -> str:
        raise ValueError("boom")

    result = runner.invoke(app, ["hello", "Ada"], obj=Deps(greet=failing_greet))
    assert result.exit_code == 2
    assert "boom" in result.output
