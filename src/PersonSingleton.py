from dataclasses import dataclass


# @dataclass
# class PersonSingleton():
#     pass


from typing import Union
from typing import TypeVar

U = Union[int, str]
T  = TypeVar('T',int,str)

def max_1(var1: T, var2: T) -> T:
    return max(var1, var2)


max_1("foo", "bar")
print(max_1(1, 2))

