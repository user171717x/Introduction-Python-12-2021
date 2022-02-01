
def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    return text.replace('.', ' ').replace(',', ' ').split()[0]


print(first_word("Hello world"))
print(first_word(" a word "))
print(first_word("don't touch it"))
print(first_word("greetings, friends"))
print(first_word("... and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))


"""
Best "Clear" Solution:

import re

def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)
"""


"""
def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] in ',. ':
        i += 1
    j = i
    while j < len(text) and text[j] not in ',. ':
        j += 1
    return text[i:j]
"""


"""

...?

"""