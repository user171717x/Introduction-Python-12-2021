
import random
import string

RUN_FLAG = True  # change it to True if you wanna run all parts of homework

if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    1. Дано целое число (int). Определить сколько нулей в этом числе.
    ''')

    RANDOM_UPPER_BOUND = 10000000000000000000000

    x_int = random.randint(0, RANDOM_UPPER_BOUND)
    result = len(str(x_int)) - len(str(x_int).replace('0', ''))
    print(f"In integer {x_int} there are {result} zero digits.")
    # result = number.count("0")    better case to solve that

if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
    ''')

    x_int = 10030030000
    result = len(str(x_int)) - len(str(int(str(x_int)[::-1])))
    print(f"In integer {x_int} there are {result} zero digits at the right side.")
    # result = len(number) - len(number.rstrip("0"))        better case

if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    3. Дан список строк my_list. Создать новый список в который поместить
    элементы из my_list по следующему правилу:
    Если строка стоит на нечетном месте в my_list, то ее заменить на
    перевернутую строку. "qwe" на "ewq".
    Если на четном - оставить без изменения.
    ''')

    my_list = ['123456', '123456', '123456', '123456', '123456']
    res_list = list()
    flag = False    # count elements as 1,2,3 etc, not as 0,1,2,3 etc
    for i_str in my_list:
        if flag:
            res_list.append(i_str)
            flag = False
        else:
            res_list.append(i_str[::-1])
            flag = True
    print(f"Start list: {my_list}\nEdited list: {res_list}")

    # better
    # for c in range(len(my_list)):
    #   if c % 2 !=0:
    #       result_list.append(my_list[::-1])
    #   else:
    #       result_list.append(my_list[c])
    #
    # much Better
    # for idx in range(len(my_list)):
    #     new_value = my_list[idx][::-1] if idx % 2 else my_list[idx]
    #     my_list.append(my_list[idx])

if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
    стоит на последнем месте в new_list. Если my_list [1,2,3,4], то new_list [2,3,4,1]
    ''')

    LIST_SIZE = 10
    RANDOM_UPPER_BOUND = 20

    my_list = list()

    for _ in range(LIST_SIZE):  # creating new list with length LIST_SIZE and random ints from range
        my_list.append(random.randint(0, RANDOM_UPPER_BOUND))

    new_list = my_list[1:]
    new_list.append(my_list[0])
    print(f"Start list: {my_list}\nEdited list: {new_list}")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
    [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
    ''')

    LIST_SIZE = 10
    RANDOM_UPPER_BOUND = 20

    my_list = list()

    for _ in range(LIST_SIZE):  # creating new list with length LIST_SIZE and random ints from range
        my_list.append(random.randint(0, RANDOM_UPPER_BOUND))

    print(f"Start list: {my_list}")
    temp = my_list.pop(0)
    my_list.append(temp)
    print(f"Edited list: {my_list}")

    # better
    # my_list.append(my_list.pop(0))

if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    6. Дана строка в которой есть числа (разделяются пробелами).
    Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
    Для данного примера ответ - 133. (используйте split и проверку isdigit)
    ''')

    my_str = '43 больше чем 34 но меньше чем 56'
    result = 0
    for item in my_str.split(' '):      # split() - lychshe razdelyaet po probelam berya vse probeli idyshie ryadom
        if item.isdigit():
            result += int(item)
    print(f"Text with numbers: {my_str}\nTotal sum of all numbers at text: {result}")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
    которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
    В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
    my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
    ''')

    my_str = 'My long string'
    l_limit = 'o'
    r_limit = 'g'
    temp_str = my_str[:my_str.index(l_limit):-1]
    sub_str = temp_str[:temp_str.index(r_limit):-1]
    print(f"Start string: {my_str}\nBiggest substring from {l_limit} to {r_limit}: {sub_str}")

    #better
    # l = my_str.find(l_limit)
    # r = my_str.rindex(r_limit)
    # s = my_str[l+1 : r]

if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
    Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
    быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
    (используйте срезы длинны 2)
    ''')

    random.seed()
    letters = string.ascii_lowercase  # all abc lowercase letters
    string_length = random.randint(5, 20)  # string have random length
    # creating string from letters using loop with our length
    my_str = ''.join(random.choice(letters) for _ in range(string_length))

    res_list = list()

    if len(my_str) % 2 > 0:     # if len(my_str) % 2:    better case
        temp = my_str + '_'
    else:
        temp = my_str

    for idx in range(0, len(temp), 2):
        res_list.append(temp[idx:idx + 2])

    print(f"Start string: {my_str}\nString split to list : {res_list}")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    9. Дан список чисел. Определите, сколько в этом списке элементов,
    которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
    Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
    Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
    ''')

    LIST_SIZE = 10
    RANDOM_UPPER_BOUND = 9

    my_list = list()

    for _ in range(LIST_SIZE):  # creating new list with length LIST_SIZE and random ints from range
        my_list.append(random.randint(0, RANDOM_UPPER_BOUND))

    result = 0
    for item in range(1, len(my_list) - 1):
        if my_list[item - 1] + my_list[item + 1] < my_list[item]:
            result += 1

    print(f"Numbers list: {my_list}\nThere are {result} number(s) greater than the sum of neighbors")


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    10. Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
    а) Определить возраст самого молодого человека и поместить в новый список имена всех людей,
    чей возраст совпадает с этим минимальным возрастом.
    б) Определить самое длинное имя и поместить в новый список имена всех людей,
    чье имя по длине совпадает с этой длиной.
    в) Посчитать среднее количество лет всех людей из списка.
    ''')

    persons = [
        {"name": "John", "age": 15},
        {"name": "Nicholas", "age": 24},
        {"name": "Comodo", "age": 15},
        {"name": "Izen", "age": 39},
        {"name": "Bonny", "age": 45},
        {"name": "Donald", "age": 50},
        {"name": "Harry", "age": 50},
        {"name": "Brian", "age": 31},
        {"name": "Jack", "age": 18}
    ]

    max_name_len, min_age, aver_age = 0, 999, 0
    min_age_names, max_len_names = list(), list()

    print('List of persons:')

    for person in persons:
        print(f"{person['name']}, age {person['age']}")
        min_age = person['age'] if person['age'] < min_age else min_age
        max_name_len = len(person['name']) if len(person['name']) > max_name_len else max_name_len
        aver_age += person['age']
    aver_age //= len(persons)   # average age calculating

    for person in persons:
        if person['age'] == min_age:
            min_age_names.append(person['name'])
        if len(person['name']) == max_name_len:
            max_len_names.append(person['name'])

    print(f"\nMinimal age at list: {min_age} age\nList of names with that age: {min_age_names}")
    print(f"\nMaximum name length at list: {max_name_len} symbols\nList of names with that length: {max_len_names}")
    print(f"\nAverage age at list: {aver_age}")

    # better
    # ages = []   all ages
    # names_lens = []     all names length
    # for person_dict in persons:
    #     ages.append(person_dict["age"])
    #     names_lens.append(len(person_dict["name"]))
    # min_age = min(ages)
    # max_name_len = max(names_lens)
    # aver_age = sum(ages) / len(ages)
    # for person_dict in persons:
    #     if len(person_dict["name"]) == max_len_name:
    #         print(person_dict["name"])
    # for person_dict in persons:
    #     if person_dict["age"] == min_age
    #         print(person_dict["name"])