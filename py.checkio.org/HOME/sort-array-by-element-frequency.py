def frequency_sort(items):
    freq_dict = {key: items.count(key) for key in items}
    items_freq = [[item, freq_dict[item]] for item in items]

    idx_dict = {key: items.index(key) for key in items}
    items_idx = [[item, idx_dict[item]] for item in items]

    item_f = list()
    for freq in set(freq_dict.values()):
        temp_list = [items_idx[item] for item in range(len(items_idx)) if items_freq[item][1] == freq]
        item_f.append(sorted(temp_list, key=lambda x: x[1]))

    result = list()
    for item in item_f[::-1]:
        for item2 in item:
            result.append(item2[0])

    return result


print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))



"""
Best "Clear" Solution:


def frequency_sort(items):
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))
"""

"""
Best "Speedy" Solution:


from collections import Counter

def frequency_sort(items):
	groups = Counter(items)
	sort = sorted(groups.items(), key=lambda e: e[1], reverse=True)
	for key, value in sort:
		yield from [key]*value
"""

"""
from collections import Counter

...???
"""