def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))


print(beginning_zeros('001001'))
print(beginning_zeros('100'))
print(beginning_zeros('0000'))


"""
Best "Clear" Solution, Best "Speedy" Solution:

def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))
"""