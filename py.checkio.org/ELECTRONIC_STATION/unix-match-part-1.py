def unix_match(filename: str, pattern: str) -> bool:
    """
    * match any count any symbols
    ? match 1 any symbol
    """

    return filename == pattern


print(unix_match('somefile.txt', '*'))
print(unix_match('log1.txt', 'log?.txt'))
