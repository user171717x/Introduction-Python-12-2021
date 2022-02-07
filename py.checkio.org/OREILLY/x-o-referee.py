from typing import List


def checkio(game_result: List[str]) -> str:
    set_1 = {game_result[0][0], game_result[0][1], game_result[0][2]}
    set_2 = {game_result[1][0], game_result[1][1], game_result[1][2]}
    set_3 = {game_result[2][0], game_result[2][1], game_result[2][2]}
    set_4 = {game_result[0][0], game_result[1][0], game_result[2][0]}
    set_5 = {game_result[0][1], game_result[1][1], game_result[2][1]}
    set_6 = {game_result[0][2], game_result[1][2], game_result[2][2]}
    set_7 = {game_result[0][0], game_result[1][1], game_result[2][2]}
    set_8 = {game_result[0][2], game_result[1][1], game_result[2][0]}

    sets = [set_1, set_2, set_3, set_4, set_5, set_6, set_7, set_8]
    for line in sets:
        if len(line) == 1:
            if line.issubset('.'):
                continue
            return line.pop()
    return "D"


# print(checkio(["X.O", "XX.", "XOO"]))
# print(checkio(["OO.", "XOX", "XOX"]))
# print(checkio(["OOX", "XXO", "OXX"]))
# print(checkio(["O.X", "XX.", "XOO"]))
# print(checkio(["...","XXX","OO."]))
print(checkio(["OOX", "XXO", "OXX"]))


"""
Best "Clear" Solution

def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

"""


"""
Best "Speedy" Solution


# migrated from python 2.7
def checkio(game_result):
    for i in range(3):
        if (game_result[i][0] in ['O', 'X']) and (game_result[i][0] == game_result[i][1] == game_result[i][2]):
            return game_result[i][0]
        if (game_result[0][i] in ['O', 'X']) and (game_result[0][i] == game_result[1][i] == game_result[2][i]):
            return game_result[0][i]
    if (game_result[1][1] in ['O', 'X']) and ((game_result[0][0] == game_result[1][1] == game_result[2][2]) or (game_result[0][2] == game_result[1][1] == game_result[2][0])):
        return game_result[1][1]
    return "D"
"""

"""
HOW ?

... ???
"""