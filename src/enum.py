from enum import Enum
from typing import NoReturn


class Color(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"  # I just added this


def handle_color(color: Color) -> None:
    if color is Color.RED:
        ...
    elif color is Color.GREEN:
        ...
    # elif color is Color.BLUE:
    #     ...
    else:
        assert_never(color) 
        #passing ENUM Blue but function expecting NoReturn 
        #mypy gives error


def assert_never(value: NoReturn) -> NoReturn:
    assert False, f"Unknown value: {value}"
