def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    freq_dict = {element: data.count(element) for element in data}
    max_value = int()
    max_key = str()

    for key, value in freq_dict.items():
        if not max_value:
            max_value = value
            max_key = key
        elif max_value < value:
            max_value = value
            max_key = key
        else:
            pass

    return max_key


most_frequent(["a", "b", "c", "a", "b", "a"])
most_frequent(["a", "a", "bi", "bi", "bi"])


"""
Best "Speedy" Solution:

def most_frequent(data):
    return max(set(data), key=data.count)
    
"""

"""
max() - 

...???
"""