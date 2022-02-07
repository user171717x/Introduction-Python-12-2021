import unicodedata


def checkio(in_string):
    """remove accents"""
    return ''.join(c for c in unicodedata.normalize('NFD', in_string)
                   if unicodedata.category(c) != 'Mn')


print(checkio(u"préfèrent"))
print(checkio(u"loài trăn lớn"))
print(checkio("loài trăn lớn"))
print(checkio("àèìǹòùẁỳÀÈÌǸÒÙẀỲ"))
print(checkio("ằẰ"))

"""
https://www.compart.com/en/unicode/category/Mn
https://docs-python.ru/standart-library/modul-unicodedata-python/
"""

"""
... ???
"""