import json


def pretty_dict_str(python_dictionary: dict) -> str:
    """Returns a string representation of a dictionary with sorted keys and indentation."""
    return json.dumps(python_dictionary, sort_keys=True, indent=4)
