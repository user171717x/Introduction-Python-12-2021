import random


RUN_FLAG = True  # change it to True if you wanna run all parts of homework


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    1. Напишите программу, которая удаляет дубликаты элементов из списка.
    ''')

    LIST_SIZE = 30
    RANDOM_UPPER_BOUND = 20

    in_list = []    # list with duplicates
    out_list = []   # temp list without duplicates

    for _ in range(LIST_SIZE):  # creating new list with length LIST_SIZE and random ints from range
        in_list.append(random.randint(0, RANDOM_UPPER_BOUND))

    for x in in_list:
        flag = 0
        for y in out_list:
            if x == y:
                flag = 1    # if element added already to out list
        else:
            if flag == 0:
                out_list.append(x)
    print(f"List with duplicates: {in_list}")
    in_list = out_list
    print(f"List without duplicates: {in_list}")


if RUN_FLAG:
    print('''
    ========================================
    2. Напишите программу, которая копирует список.
    ''')

    LIST_SIZE = 10
    RANDOM_UPPER_BOUND = 20

    in_list = []  # start list
    out_list1 = []  # copy of start list
    out_list2 = []  # doubled start list

    for _ in range(LIST_SIZE):  # creating new list with length LIST_SIZE and random ints from range
        in_list.append(random.randint(0, RANDOM_UPPER_BOUND))

    out_list1 = in_list.copy()

    out_list2 = in_list.copy()
    for x in in_list:
        out_list2.append(x)

    out_list3 = list()
    for x in in_list:
        out_list3.append(x)

    print(f"Start list: {in_list}")
    print(f"Copy of start list: {out_list1}")
    print(f"Doubled start list: {out_list2}")
    print(f"Copy of start list (without using copy()): {out_list3}")


if RUN_FLAG:
    print('''
    ========================================
    3. Напишите программу, которая находит разницу между двумя списками и сохраняет ее в новый список.
    Вывести результат на экран.
    ''')

    LIST1_SIZE = 10
    LIST2_SIZE = 15
    RANDOM_UPPER_BOUND = 10

    first_list = []  # 1st list to compare
    second_list = []  # 2nd list to compare
    dif_list_temp = []
    dif_list = []  # difference between lists

    for _ in range(LIST1_SIZE):  # creating new list with length LIST1_SIZE and random ints from range
        first_list.append(random.randint(0, RANDOM_UPPER_BOUND))
    for _ in range(LIST2_SIZE):  # creating new list with length LIST2_SIZE and random ints from range
        second_list.append(random.randint(0, RANDOM_UPPER_BOUND))

    for x in first_list:
        flag = 0
        for y in second_list:
            if x == y:
                flag = 1
        else:
            if flag == 0:
                dif_list_temp.append(x)

    for x in second_list:
        flag = 0
        for y in first_list:
            if x == y:
                flag = 1
        else:
            if flag == 0:
                dif_list_temp.append(x)

    for x in dif_list_temp:
        flag = 0
        for y in dif_list:
            if x == y:
                flag = 1
        else:
            if flag == 0:
                dif_list.append(x)

    print(f"1st list to compare: {first_list}")
    print(f"2nd list to compare: {second_list}")
    print(f"Difference between lists: {dif_list}")
    print(f"Difference between lists (using sets): {list(set(first_list).symmetric_difference(set(second_list)))}")


if RUN_FLAG:
    print('''
    ========================================
    4. Напишите программу для объединения следующих словарей для создания нового
    Исходные словари :
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    Результат : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    ''')

    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    dic_total = {}

    for key in dic1:
        dic_total[key] = dic1[key]
    for key in dic2:
        dic_total[key] = dic2[key]
    for key in dic3:
        dic_total[key] = dic3[key]

    print(f"1st dictionary: {dic1}")
    print(f"2nd dictionary: {dic2}")
    print(f"3rd dictionary: {dic3}")
    print(f"Summary dictionary: {dic_total}")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    5. Напишите программу, которая выводит словарь, в котором ключи представляют собой числа от 1 до 15 (оба включены),
    а значения представляют собой квадраты ключей. Генерация ключей и значений должна быть выполнена через цикл.
    ''')

    dic = {}

    for key in range(1, 16):
        dic[key] = key * key

    print(f"Dictionary, where values equal squares of keys(1..15):\n {dic}")


