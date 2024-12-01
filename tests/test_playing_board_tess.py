from playing_board import get_playing_board
import pytest

@pytest.mark.parametrize(["num","val"],[
    (
        5,
        " * * " "* * *" " * * " "* * *" " * * "
    ),
    (
        10,
        (
            " * * * * *"
            "* * * * * "
            " * * * * *"
            "* * * * * "
            " * * * * *"
            "* * * * * "
            " * * * * *"
            "* * * * * "
            " * * * * *"
            "* * * * * "
        )
    )
])
def test_playing_board(num, val):
    print(get_playing_board(num))
    assert ('').join(get_playing_board(num)) == val
