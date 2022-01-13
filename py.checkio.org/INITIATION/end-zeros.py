def end_zeros(num: int) -> int:
    number = len(str(num)) - len(str(num).rstrip('0'))
    return number


print(end_zeros(0))

"""
:= - assigns values to variables as part of a larger expression
Example:
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
"""

"""
Best "Clear" Solution:

def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))
"""

"""
Best "Speedy" Solution:

def end_zeros(num: int) -> int:
    # your code here
    if num == 0:
        return 1
    
    zeros = 0
    while num % 10 == 0:
        num //= 10
        zeros += 1
    return zeros
"""