def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    if text.count(symbol) > 1:
        idx = text.split(symbol)
        return len(idx[0]) + len(idx[1]) + 1
    else:
        return None


# second_index("sims", "s")
# print(second_index("find the river", "e"))
# print(second_index("hi", " "))
print(second_index("hi mayor", " "))



"""
Best "Clear" Solution:


def second_index(text: str, symbol: str):
    try:
        return text.index(symbol, text.index(symbol) + 1)
    except ValueError:
        return None
"""



"""
Best "Speedy" Solution:

def second_index(text: str, symbol: str) -> [int, None]:
    first = text.find(symbol)
    second = text.find(symbol, first+1)
    
    return second if second != -1 else None
"""