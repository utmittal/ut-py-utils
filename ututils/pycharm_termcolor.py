from typing import Iterable, Any

import termcolor
from termcolor._types import Color, Highlight, Attribute


# Copied all the type hints from the termcolor implementation because I couldn't figure out a better way to get them.
# This is not great because it breaks the moment termcolor changes.
def colored(text: object,
            color: Color | None = None,
            on_color: Highlight | None = None,
            attrs: Iterable[Attribute] | None = None) -> str:
    """Sets the `force_color=True` argument on termcolor.colored() to ensure it works in pycharm console.

    Passes all other arguments as is. Doesn't support the `no_color` argument."""

    return termcolor.colored(text=text, color=color, on_color=on_color, attrs=attrs, force_color=True)


# Copied all the type hints from the termcolor implementation because I couldn't figure out a better way to get them.
# This is not great because it breaks the moment termcolor changes.
def cprint(text: object,
           color: Color | None = None,
           on_color: Highlight | None = None,
           attrs: Iterable[Attribute] | None = None, **kwargs: Any) -> None:
    """Sets the `force_color=True` argument on termcolor.cprint() to ensure it works in pycharm console.

    Passes all other arguments as is. Doesn't support the `no_color` argument."""
    return termcolor.cprint(text=text, color=color, on_color=on_color, attrs=attrs, force_color=True, **kwargs)
