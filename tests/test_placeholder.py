from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_main():
    main_path = Path(__file__).resolve().parents[1] / "src" / "main.py"
    spec = spec_from_file_location("project_main", main_path)
    module = module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module.main


def test_main_prints_initialized_message(capsys):
    main = load_main()
    main()
    captured = capsys.readouterr()
    assert captured.out == "Paperclip project initialized\n"
