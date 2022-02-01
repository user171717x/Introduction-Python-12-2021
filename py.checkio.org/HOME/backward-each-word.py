def backward_string_by_word(text: str) -> str:
    return " ".join([word[::-1] for word in text.split(' ')])


print(backward_string_by_word('welcome to a game'))
print(backward_string_by_word('hello   world')) # 'olleh   dlrow'