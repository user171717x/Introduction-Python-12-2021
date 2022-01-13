from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    if border in items and (idx := items.index(border)):
        items = items[idx:]
    return items


print(list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)))
print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
print(list(remove_all_before([1, 2, 3, 4, 5], 6)))
print(list(remove_all_before([], 5)))


"""
Best "Clear" Solution:

def remove_all_before(items, border):
    try:
        return items[items.index(border):]
    except ValueError:
        return items
"""


"""
Best "Speedy" Solution:

def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    
    return items[items.index(border):] if border in items else items
"""