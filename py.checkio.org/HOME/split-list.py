def split_list(items: list) -> list:
    return [items[:len(items) // 2 + 1 if len(items) % 2 else len(items) // 2],
            items[len(items) // 2 + 1 if len(items) % 2 else len(items) // 2:]]


print(split_list([1, 2, 3, 4, 5]))
print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1]))
print(split_list([]))


"""
Best "Clear" Solution

def split_list(items: list) -> list:
    return [items[:(split_index := (len(items) + 1) // 2)], items[split_index:]]

"""


"""
Best "Speedy" Solution

def split_list(items: list) -> list:
    s = (len(items)+1) // 2
    return [items[:s],items[s:]]
"""

"""
:=

... ???

"""