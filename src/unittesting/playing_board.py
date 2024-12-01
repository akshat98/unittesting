from typing import List

def call(val: int) -> int:
    return val;

def get_playing_board(n: int)-> list[str]:
    def get_char(ind : int)-> str: 
        return ' ' if ind%2 == 0 else '*'
    
    ind=0
    matrix = []
    for j in range(n):
        row = ""
        for i in range(n):
            row+= get_char(ind)
            ind+=1
        matrix.append(row)
    return matrix
        