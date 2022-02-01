
def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    data.sort(reverse=True, key=sort_by_price)

    return data[:limit]


def sort_by_price(item):
    return item['price']


print(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))


"""
Best "Clear" Solution:

def bigger_price(limit, data):
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]
"""


"""
Best "Speedy" Solution:

def bigger_price(limit: int, data: list) -> list:
    data.sort(key=lambda x: x["price"], reverse=True)
    return data[:limit]
"""


"""
key=lambda x: x['price'], reverse=True

... ???
"""