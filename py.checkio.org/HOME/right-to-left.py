def left_join(phrases: tuple) -> str:
    """
    Join strings and replace "right" to "left"
    """
    return "left".join(",".join(phrases).split('right'))


assert (left_join(("left", "right", "left", "stop")) == "left,left,left,stop"), "All to left"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"


"""
Best "Speedy" Solution:

def left_join(phrases):
    return ",".join(phrases).replace("right", "left")
"""


"""
Best "Clear" Solution:

def left_join(phrases):
    return (",".join(phrases)).replace("right","left")
"""