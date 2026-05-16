from src.main import main


def test_main_returns_zero(capsys):
    assert main() == 0
    captured = capsys.readouterr()
    assert "Hermes Core running" in captured.out
