import runpy

import pytest

from cli_template import __version__
from cli_template.cli import main


def test_console_script(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("sys.argv", ["cli-template", "--version"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0
    assert capsys.readouterr().out.strip() == __version__


def test_python_m(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr("sys.argv", ["cli_template", "hello", "Ada"])
    with pytest.raises(SystemExit) as exc_info:
        runpy.run_module("cli_template", run_name="__main__")
    assert exc_info.value.code == 0
    assert capsys.readouterr().out.strip() == "Hello, Ada."
