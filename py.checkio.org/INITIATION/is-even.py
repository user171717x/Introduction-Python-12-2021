def is_even(num: int) -> bool:
    return num % 2 == 0


"""
Best "Speedy" Solution:

def is_even(num: int) -> bool:
    return not(num & 1)
"""

"""
Best "Clear" Solution:

def is_even(num: int) -> bool:
    return num & 1 == 0
"""