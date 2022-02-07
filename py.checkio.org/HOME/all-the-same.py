from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) < 2


print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 1]))
print(all_the_same(['a', 'a', 'a']))
print(all_the_same([]))

"""
Best "Clear" Solution

def all_the_same(elements):
   return elements[1:] == elements[:-1]
"""


"""
Best "Creative" Solution

all_the_same = lambda e: e[1:] == e[:-1]
"""