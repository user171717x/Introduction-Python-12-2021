def count_digits(text: str) -> int:
    summ = 0
    for symbol in text:
        if symbol.isdigit():
            summ += 1

    # case2: # summ = len([symbol for symbol in text if symbol.isdigit()])

    return summ


print(count_digits('Petersen between 1845 and 1910 year'))


"""
Best "Clear" Solution:

def count_digits(text: str) -> int:
    return sum(c.isdigit() for c in text)

"""


"""
Best "Creative" Solution:

def count_digits(text: str) -> int:
    return sum(text.count(digit) for digit in '1234567890')
"""

"""
Best "Speedy" Solution:

def count_digits(text: str) -> int:
    return sum(map(str.isdigit, text))
"""


"""
map() - 


sum(c.isdigit() for c in text) -

...???

"""