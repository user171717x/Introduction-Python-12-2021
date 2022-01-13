def nearest_value(values: set, one: int) -> int:
    dif_list_abs = [abs(one - number) for number in values]
    diff = min(dif_list_abs)
    diff_count = dif_list_abs.count(diff)
    result = one + diff if ((diff + one) in values) and diff_count == 1 else one - diff
    return result


print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
print(nearest_value({4, 7, 10, 11, 12, 17}, 8))
print(nearest_value({4, 8, 10, 11, 12, 17}, 9))
print(nearest_value({4, 9, 10, 11, 12, 17}, 9))
print(nearest_value({4, 7, 10, 11, 12, 17}, 0))
print(nearest_value({4, 7, 10, 11, 12, 17}, 100))
print(nearest_value({5, 10, 8, 12, 89, 100}, 7))
print(nearest_value({5}, 5))
print(nearest_value({5}, 7))


"""
Best "Creative" Solution:

def nearest_value(values: set, one: int) -> int:
    return min(sorted(values), key = lambda i: abs(i - one)) 

"""

"""
Best "Speedy" Solution:

from functools import cmp_to_key
def nearest_value(values: set, one: int) -> int:    
    return sorted(values, key = cmp_to_key(lambda a,b: abs(a - one) - abs(b - one) or (a-b)))[0]
"""


"""

lambda

cmp_to_key

...???
"""