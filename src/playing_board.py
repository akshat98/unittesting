from typing import List

def call(val: int) -> int:
    return val;

def get_playing_board(n: int)-> list[str]:
    def get_char(ind : int)-> str: 
        return '*' if ind%2 == 0 else ' '
    
    toggle = False
    matrix = []
    for j in range(n):
        row = ""
        for i in range(n):
            row+= "*" if toggle else " "
            toggle = not toggle
        toggle = not toggle if(n%2==0) else toggle
        matrix.append(row)
    return matrix
        