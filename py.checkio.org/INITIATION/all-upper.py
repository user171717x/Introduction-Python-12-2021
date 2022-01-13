def is_all_upper(text: str) -> bool:
    return text == text.upper()


print(is_all_upper('ALL UPPER'))
print(is_all_upper('     '))
print(is_all_upper('55 55 5'))
print(is_all_upper('mixed UPPER and lower'))
