def checkio(words: str) -> bool:
    count = 0
    for word in words.split():
        if word.isnumeric():
            count = 0
        else:
            if count == 2:
                return True
            else:
                count += 1
    return False


assert checkio("Hello World hello") == True, "Hello"
assert checkio("He is 123 man") == False, "123 man"
assert checkio("1 2 3 4") == False, "Digits"
assert checkio("bla bla bla bla") == True, "Bla Bla"
assert checkio("Hi") == False, "Hi"


"""
Best "Speedy" Solution:


import re

def checkio(words):
    return True if re.search('\D+\s\D+\s\D+', words) else False

"""


"""
Best "Clear" Solution:

def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False
"""


"""

import re

word.isalpha()

...???

"""