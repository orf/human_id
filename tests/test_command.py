import pytest
from click.testing import CliRunner
from human_id.cli import main


@pytest.fixture()
def cli():
    runner = CliRunner()
    return lambda *args: runner.invoke(main, args)


def test_default(cli):
    result = cli()
    assert result.exit_code == 0


def test_sep(cli):
    result = cli("--sep=!")
    assert len(result.output.split("!")) == 4


def test_count(cli):
    result = cli("--count=4")
    assert len(result.output.split("\n")) == 5  # There's an extra newline.
