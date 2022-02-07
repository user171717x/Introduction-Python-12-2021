def checkio(values: list) -> list:
    return sorted(values, key=lambda x: int((x ** 2) ** 0.5))

print(checkio([-20, -5, 10, 15]))
