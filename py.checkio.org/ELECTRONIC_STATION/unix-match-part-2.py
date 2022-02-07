import re


def unix_match(filename: str, pattern: str) -> bool:
    braket_part = re.findall(r'\[.*]', pattern)
    before_part, after_part = pattern.split(braket_part[0])
    print(braket_part[0], before_part, after_part)

    temp = braket_part[0][1:-1]
    temp = temp.replace('[', '\[').replace(']', '\]')
    full_pattern = before_part + '[' + temp + ']' + after_part
    print(full_pattern)

    # match = re.fullmatch(pattern.
    #                              replace('.', '\.').
    #                              replace('[!]', '\[\!\]').
    #                              replace('*', '\*').
    #                              replace('[]', ' ').
    #                              replace('[!', '[^'), filename)
    match = None
    return False if match is None else True


print(unix_match("checkio", "[c[]heckio"))
# print(unix_match("[!]check.txt", "[!]check.txt"))
# print(unix_match("[!]check.txt", "[!]check.txt"))
# print(unix_match("nametxt","name[]txt"))
# print(unix_match("name.txt","name[]txt"))
# print(unix_match('somefile.txt', '*'))
# print(unix_match('somefile.txt', 'somefile.txt'))
# print(unix_match('log1.txt', 'log[1234567890].txt'))
# print(unix_match('log1.txt', 'log[!0].txt'))
# print(unix_match('log1.txt', 'log[1234567890].txt'))
# print(unix_match('log1.txt', 'log[!1].txt'))
