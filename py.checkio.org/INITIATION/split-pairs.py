def split_pairs(a):
    if len(a) % 2 == 1:
        a = f"{a}_"
    result = list()
    for idx in range(0, len(a)):
        if idx % 2 == 0:
            result.append(a[idx: idx + 2])
    return result


print(list(split_pairs('abcd')))
print(list(split_pairs('a')))
print(list(split_pairs('abcdf')))


"""
Best "Speedy" Solution:

def split_pairs(a):
    a += '_' if len(a) % 2 else ''
    return [a[i:i + 2] for i in range(0, len(a), 2)]
"""


"""
Best "Clear" Solution:

def split_pairs(a):
    return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]

"""

"""
zip() - 

...???
"""