
def popular_words(text: str, words: list) -> dict:
    return {key: text.lower().split().count(key) for key in words}


print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

print(popular_words("\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n", ["one", "two", "three"]))


"""
Best "Clear" Solution:

def popular_words(text, words):
    lower_count = text.lower().split().count
    return {word: lower_count(word) for word in words}
"""


"""
Best "Speedy" Solution:

def popular_words(text, words):
    counter = {word: 0 for word in words}
    for word in text.lower().split():
        if word in counter:
            counter[word] += 1
    return counter
"""