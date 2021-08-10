from smart_home.lib.file_operations import write_to_file
from pathlib import Path


def test_write_to_file_with_string():
    string = '{"test_key": "test_value"}'
    filepath = Path("tests/test_lib/test_file.json")
    write_to_file(string, filepath)
    assert filepath.is_file()
    with open(filepath, "r") as f:
        assert '{"test_key": "test_value"}' in f
