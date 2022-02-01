def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    if text.count(begin) and text.count(end) and text.index(begin) > text.index(end):
        return ''
    result = text.split(begin)[1] if text.count(begin) else text
    result = result.split(end)[0] if text.count(end) else result
    return result


print(between_markers('No <hi>', '>', '<'))

assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
assert between_markers("<head><title>My new site</title></head>",
                       "<title>", "</title>") == "My new site", "HTML"
assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'


"""
Best "Speedy" Solution:

between_markers = lambda text, begin, end: text[text.index(begin)+len(begin) if begin in text else 0: text.index(end) if end in text else len(text)]
"""

"""
Best "Clear" Solution:

def between_markers(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]
"""

"""
lambda -

...???
"""