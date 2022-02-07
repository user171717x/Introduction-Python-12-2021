import re


def unix_match(filename: str, pattern: str) -> bool:
    """
    * match any count any symbols
    ? match 1 any symbol
    """
    full_pattern = r''
    for symbol in pattern:
        if symbol == '*':
            full_pattern += '[A-Za-z0-9.]*'
        elif symbol == '?':
            full_pattern += '[A-Za-z0-9.]{1}'
        elif symbol == '.':
            full_pattern += '\.'
        else:
            full_pattern += symbol
    match = re.fullmatch(full_pattern, filename)
    if match is None:
        result = False
        # print(f"{filename} <> {pattern} <> {full_pattern} = False")
    else:
        result = True
        # print(f"{filename} <> {pattern} <> {full_pattern} = {match.string} <> True")

    return result


# unix_match('somefile.txt', '*')
# unix_match('other.exe', '*')
# unix_match('my.exe', '*.txt')
# unix_match('log1.txt', 'log?.txt')
# unix_match('log12.txt', 'log?.txt')
# unix_match('log12.txt', 'log??.txt')
unix_match("12apache1", "*.*")


"""
Best "Clear" Solution:


from re import search


def unix_match(filename: str, pattern: str) -> bool:
    return (
        search(
            pattern.replace(".", r"\.").replace("*", ".*").replace("?", "."), filename
        )
        is not None
    )
"""


"""
Best "Speedy" Solution:

unix_match = lambda f, p: __import__('re').match(p.replace('.', r'\.').replace('*', '.*').replace('?', r'.{1}'), f) is not None

"""