def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    return text[text.index(begin) + 1: text.index(end)]


print(between_markers('What is >apple<', '>', '<'))
print(between_markers('What is [apple]', '[', ']'))
print(between_markers('What is ><', '>', '<'))
print(between_markers('>apple<', '>', '<'))


"""
Best "Speedy" Solution:

def between_markers(text, begin, end):
    i = text.find(begin) + 1
    j = text.find(end, i)
    return text[i:j]
"""