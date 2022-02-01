def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    if not len(array):
        return 0
    else:
        return sum([array[idx] for idx in range(0, len(array)) if not (idx & 1)]) * array[-1]


"""
Best "Clear" Solution:

def checkio(array):
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]
"""


"""
Best "Speedy" Solution:

def checkio(array):
    return sum(array[0::2])*array[-1] if 0 < len(array) else 0

"""