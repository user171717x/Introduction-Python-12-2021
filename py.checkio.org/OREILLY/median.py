"""
raise
The raise keyword is used to raise an exception.

Try the following missions with raise:
Absolute SortingAbsolute Sorting
MedianMedian
The Hidden WordThe Hidden Word
"""

from typing import List


def checkio(data: List[int]) -> [int, float]:
    try:
        data = sorted(data)
        if data[0] is str:
            raise Exception(TypeError)
        else:
            return data[len(data) // 2] if len(data) % 2 else (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
    except TypeError as e:
        return 0


print(checkio(['a', 2, 3, 4, 5]))
print(checkio([1, 2, 3, 4, 5]))
print(checkio([3, 1, 2, 5, 3]))
print(checkio([1, 300, 2, 200, 1]))
print(checkio([3, 6, 20, 99, 10, 15]))
print(checkio(list(range(1000000))))


"""
Best "Clear" Solution

def checkio(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2
"""


"""
Best "Creative" Solution

checkio=lambda d:(lambda t,n:t[n]+t[-n-1])(sorted(d),len(d)//2)/2
"""


"""
Best "Speedy" Solution

# Find the k'th-smallest value in a, worst case O(n)
# Skip the first d elements and consider only the next n
def select(a, d, n, k):
    if n <= 5:
        return sorted(a[d:d+n])[k]

    # Find median of medians of 5
    medians = [sorted(a[i:i+5])[2] for i in range(d, d+n-4, 5)]
    m = len(medians)
    median = select(medians, 0, m, m // 2)

    # Partition around the median.
    # a[d:i]     <= median
    # a[j+1:d+n] >= median
    i, j = d, d+n-1
    while i <= j:
        while a[i] < median: i += 1
        while a[j] > median: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if d+k < i: return select(a, d, i-d, k)
    else:       return select(a, i, n+d-i, k+d-i)

def checkio(data):
    n = len(data)
    if n % 2 == 1:
        return select(data, 0, n, n//2)
    else:
        return 0.5 * (select(data, 0, n, n//2-1) + select(data, 0, n, n//2))
"""


"""

data[~half]

... ???
"""