#Your optional code here
#You can import some modules or create additional functions


def checkio(data: list) -> list:
    fixed_data = [item for item in data if data.count(item) > 1]
    return fixed_data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


print(list(checkio([1, 2, 3, 1, 3])))

assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"


"""
Best "Clear" Solution:

checkio=lambda d:[x for x in d if d.count(x)>1]
"""

"""
Best "Speedy" Solution:

def checkio(data):
from collections import Counter
count = Counter(data)
return [n for n in data if count[n] > 1]
"""

"""
lambda - 

... ???
"""