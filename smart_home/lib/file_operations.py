import json
import inspect


def write_to_file(data, filepath):
    """
    Response Object or Dict and writes it to a specified filepath.

    Args:
      data: Str, Dict, or Response Object
      filepath: Str
    """

    with open(filepath, "w+") as f:
        if inspect.isclass(data):
            f.write(json.dumps(data.json()))
        elif isinstance(data, str):
            f.write(data)
