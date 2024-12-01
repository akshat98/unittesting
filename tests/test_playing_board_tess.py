from unittesting.playing_board import get_playing_board

def test_playing_board():

    board_of_5 = " * * " "* * *" " * * " "* * *" " * * "

    board_of_10 = (
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

    print("hello" ,type(board_of_10))
    print(get_playing_board(50))


    assert get_playing_board(5).join(',') == board_of_5
    assert get_playing_board(10).joint(',') == board_of_10

