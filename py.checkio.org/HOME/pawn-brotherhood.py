def safe_pawns(pawns: set) -> int:
    summ = 0
    pawn_list = list(pawns)
    for pawn in pawns:
        for item in pawn_list:
            if has_def(pawn, item):
                summ += 1
                break
    return summ


def has_def(pawn, def_pawn):
    pawn_x = int(ord(pawn[0]))
    pawn_y = int(pawn[1])
    def_pawn_x = int(ord(def_pawn[0]))
    def_pawn_y = int(def_pawn[1])
    if pawn_y - 1 == def_pawn_y:
        if (pawn_x + 1 == def_pawn_x) or (pawn_x - 1 == def_pawn_x):
            return 1
    return 0


print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))


"""
Best "Clear" Solution:

def getdiags(pawn):
    c, r = map(ord, pawn)
    return chr(c - 1) + chr(r - 1), chr(c + 1) + chr(r - 1)

def safe_pawns(pawns):
    return len([p for p in pawns if any(d in pawns for d in getdiags(p))])

"""


"""
Best "Speedy" Solution:

def safe_pawns(pawns):
    return sum((any(chr(ord(l) + i) + str(int(d) - 1) in pawns for i in [-1, 1])) for l, d in pawns)

"""


"""
any()

...???
"""