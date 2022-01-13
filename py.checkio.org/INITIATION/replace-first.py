from typing import Iterable


def replace_first(items: list) -> Iterable:
    return items[1:] + items[0:1]


print(list(replace_first([1, 2, 3, 4])))
print(list(replace_first([1])))
print(list(replace_first([])))

"""
Best "Clear" Solution:

def replace_first(items: list) -> list:
    return items[1:] + items[:1]
    
    
def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items
"""