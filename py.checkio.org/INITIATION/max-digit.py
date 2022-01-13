def max_digit(number: int) -> int:
    return max([int(digit) for digit in str(number)])


print(max_digit(52))


"""
Best "Speedy" Solution:

def max_digit(number: int) -> int:
    return max(map(int, str(number)))
"""

"""
Best "Clear" Solution:

max_digit = lambda number: int(max(str(number)))
"""

"""
max() - 

map() - 

...???
"""