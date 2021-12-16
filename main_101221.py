
import random

RUN_FLAG = True  # change it to True if you wanna run all parts of homework


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    1. Напишите программу для преобразования списка в кортеж.
    ''')

    inputList = [1, 2.34, 'x', 4, 'hello', 6, 2.54]
    outputTuple = tuple(inputList)

    print(f"Data struct: {inputList} is {type(inputList)}")
    print(f"Data struct: {outputTuple} is {type(outputTuple)}")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    2. Напишите программу для замены последнего значения кортежей в списке

    Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

    Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
    ''')

    tuplesList = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    tempList = list()
    print(f"Input list: {tuplesList}")

    for i_tuple in tuplesList:
        tempList.append(tuple(list(i_tuple)[:-1] + [100]))
    tuplesList = tempList
    print(f"Output list: {tuplesList}")

    # """
    # An other case, works OK
    # """
    # for item in tuplesList:
    #     editList = list(item)
    #     editList.pop()
    #     editList.append(100)
    #     tempList.append(tuple(editList))
    # tuplesList = tempList
    # print(f"Output list: {tuplesList}")

    # """
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # This case makes task correct, but getting Warning:
    #     Class 'list' does not define 'getitem',
    # so the '[]' operator cannot be used on its instances
    # WHY ??? How to fix? Help me pls
    # """
    # for l_idx in range(0, len(tuplesList)):
    #     editList = list(tuplesList[l_idx])
    #     editList.pop()
    #     editList.append(100)
    #     tuplesList[l_idx] = tuple(editList)
    # print(f"Output list: {tuplesList}")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    3. Напишите программу для поэлементного вычисления суммы заданных кортежей.
     Результатом должен быть кортеж.
    Input
    (1, 2, 3, 4)
    (3, 5, 2, 1)
    (2, 2, 3, 1)
    Output
    (6, 9, 8, 6)
    ''')

    t1 = (1, 2, 3, 4)
    t2 = (3, 5, 2, 1)
    t3 = (2, 2, 3, 1)
    print(f"Tuple 1: {t1}\nTuple 2: {t2}\nTuple 3: {t3}")
    total = list()

    for i in range(0, len(t1)):
        total.append(t1[i] + t2[i] + t3[i])
    total = tuple(total)
    print(f"Summary tuple: {total}")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    4. Напишите программу, которая проверяет, присутствует ли А в наборе или нет.
    А вводится с клавиатуры.
    ''')

    SET_SIZE = 10
    RANDOM_UPPER_BOUND = 20

    data_set = set()
    for _ in range(SET_SIZE):  # creating new set with length SET_SIZE and random ints from range
        data_set.add(random.randint(0, RANDOM_UPPER_BOUND))
    print(f"Data Set: {data_set}")

    while True:
        a_find = input("Enter int value what you looking for at set(\'exit\' to finish): ")
        if a_find == 'exit':
            break
        if data_set.issuperset({int(a_find)}):
            print(f"{a_find} found success at set!")
        else:
            print(f"{a_find} NOT found at set!")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    5. Напишите программу, чтобы проверить, не имеют ли два заданных набора (set) общих элементов.
    ''')

    SET_SIZE = 4
    RANDOM_UPPER_BOUND = 20

    data_set1 = set()
    data_set2 = set()
    for _ in range(SET_SIZE):  # creating new set with length SET_SIZE and random ints from range
        data_set1.add(random.randint(0, RANDOM_UPPER_BOUND))
        data_set2.add(random.randint(0, RANDOM_UPPER_BOUND))
    print(f"Data Set 1: {data_set1}")
    print(f"Data Set 2: {data_set2}")

    if data_set1 & data_set2:
        print('Some elements at Set 1 same as at Set 2.')
    else:
        print('Sets totally different!')


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    6. Напишите программу для поиска элементов в данном наборе A (set), которых нет в другом наборе B.
    ''')

    SET_SIZE = 7
    RANDOM_UPPER_BOUND = 10

    data_setA = set()
    data_setB = set()
    for _ in range(SET_SIZE):  # creating new set with length SET_SIZE and random ints from range
        data_setA.add(random.randint(0, RANDOM_UPPER_BOUND))
        data_setB.add(random.randint(0, RANDOM_UPPER_BOUND))
    print(f"Data Set A: {data_setA}")
    print(f"Data Set B: {data_setB}")

    temp_set = data_setA.difference(data_setB)
    if len(temp_set) > 0:
        print(f"These elements at Set A not found at Set B: {temp_set}")
    else:
        print('All elements at Set A found at Set B!')


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    7. Напишите программу, которая удаляет пересечение 2-го набора из 1-го набора.
    ''')

    SET_SIZE = 7
    RANDOM_UPPER_BOUND = 10

    data_set1 = set()
    data_set2 = set()
    for _ in range(SET_SIZE):  # creating new set with length SET_SIZE and random ints from range
        data_set1.add(random.randint(0, RANDOM_UPPER_BOUND))
        data_set2.add(random.randint(0, RANDOM_UPPER_BOUND))
    print(f"Data Set 1: {data_set1}")
    print(f"Data Set 2: {data_set2}")

    result = data_set1.difference(data_set2)

    print(f"Edited Set 1, without crossing with Set 2 elements: {result}")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    8. Реализовать логику Union для двух списков (list), проверить работу алгоритма на set.union
    ''')

    list1 = [0, 1, 3, 4, 5, 7, 9, 12, 14, 20]
    list2 = [0, 2, 6, 7, 9, 11, 12, 13, 15, 19, 20]
    print(f"Data List 1: {list1}")
    print(f"Data List 2: {list2}")

    expected_result = list(set(list1).union(set(list2)))
    print(f"Expected result: {expected_result}")

    result = list1[:]
    for item in list2:
        if item not in result:
            result.append(item)
    result.sort()

    print(f"Union with lists: {result}\nSolved correct: {expected_result == result}")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    9. Реализовать логику Difference для двух списков (list), проверить работу алгоритма на set.difference
    ''')

    list1 = [0, 1, 3, 4, 5, 7, 9, 12, 14, 20]
    list2 = [0, 2, 6, 7, 9, 11, 12, 13, 15, 19, 20]
    print(f"Data List 1: {list1}")
    print(f"Data List 2: {list2}")

    expected_result = list(set(list1).difference(set(list2)))
    print(f"Expected result: {expected_result}")

    result = list1[:]
    for item in list2:
        if item in result:
            result.pop(result.index(item))
    result.sort()

    print(f"Difference with lists: {result}\nSolved correct: {expected_result == result}")
