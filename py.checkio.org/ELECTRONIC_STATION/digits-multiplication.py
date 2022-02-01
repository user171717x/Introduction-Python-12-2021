import functools


def checkio(number: int) -> int:
    return functools.reduce(lambda x, y: x * y if x > 0 and y > 0 else x + y, [int(x) for x in [*str(number)]])


print(checkio(123405))
print(checkio(999))
print(checkio(1))

"""
Best "Speedy" Solution:

def checkio(number):
    total = 1
    for i in str(number).replace("0",""):
        total *= int(i)
    return total
"""


"""
functools.reduce - 

...???
"""