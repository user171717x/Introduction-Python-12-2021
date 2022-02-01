def sum_numbers(text: str) -> int:
    elements = text.split()
    summ = 0
    for element in elements:
        if element.isdigit():
            summ += int(element)
    return summ


"""
Best "Speedy" Solution:

return sum(map(int, filter(str.isdigit, text.split())))
"""

"""
sum() - Sum of numbers in the list

https://python-course.eu/advanced-python/lambda-filter-reduce-map.php
https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function-ru

...???
"""