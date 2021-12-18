
import random


def get_random_int100():
    result = random.randint(1, 100)
    return result


def print_random_int100():
    result = random.randint(1, 100)
    print(result)


def print_rnd100_50bad_50good():
    if random.randint(1, 100) > 50:
        print("Good")
    else:
        print("Bad")


def print_uppercase(text):
    result = str(text).upper()
    print(result)


def convert_uppercase(text):
    return str(text).upper()


def convert_uppercase_strlist(str_list):
    result = list()
    for conv_str in str_list:
        result.append(conv_str.upper())
    return result


def get_int_range_list(upper_bound):
    range_list = [number for number in range(1, int(upper_bound) + 1)]
    return range_list


def get_square_range_list(upper_bound):
    range_list = [number ** 2 for number in range(1, int(upper_bound) + 1)]
    return range_list


"""
1. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и печатает его.
"""
print_random_int100()

"""
2. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и возвращает его.
"""
print(get_random_int100())

"""
3. Написать функцию, которая генерирует случайное число в диапазоне от 1 до 100 и печатает слово
"Хорошо", если это число больше 50 или слово "Плохо" в противоположном случае.
"""
print_rnd100_50bad_50good()

"""
4. Написать функцию, которая принимает в качестве параметра строку
 и печатает ее в верхнем регистре (UPPERCASE).
"""
print_uppercase("dfds4343FDFfdsf")

"""
5. Написать функцию, которая принимает в качестве параметра строку
 и возвращает ее в верхнем регистре (UPPERCASE).
"""
print(convert_uppercase("dfds4343FDFfdsf"))

"""
6. Написать функцию, которая принимает в качестве параметра список строк
 и возвращает их в виде списка строк в верхнем регистре (UPPERCASE).
"""
my_list = ["fdshj", "TYTds", "dgh676d", "GHJYD6", "43fdfdf"]
print(convert_uppercase_strlist(my_list))

"""
7. Написать функцию, которая принимает в качестве параметра число
 и возвращает список чисел от 1 до заданного числа.
"""
print(get_int_range_list(10))

"""
8. Написать функцию, которая принимает в качестве параметра число
 и возвращает список квадратов чисел от 1 до заданного числа.
"""
print(get_square_range_list(7))
