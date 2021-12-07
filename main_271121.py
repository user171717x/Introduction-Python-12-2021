RUN_FLAG = True  # change it to True if you wanna run all parts of homework

'''
1. Посмотреть видео и создать проект на github
https://www.youtube.com/watch?v=IH0W5bm4orc
'''


if RUN_FLAG:  # change it to True to run
    print('''
    ========================================
    2. Напишите программу Python, которая принимает слово от пользователя и переворачивает его
    Пример:
    input - Hello Worlds
    output - sdlroW olleH
    ''')
    while True:
        in_text = input('\n\nEnter input word(\'exit\' to finish): ')
        if in_text == 'exit':
            break
        print('Output (reversed) text: ', end='')
        in_length = len(in_text)
        while in_length > 0:
            in_length -= 1
            print(f"{in_text[in_length]}", end='')


if RUN_FLAG:
    print('''
    ========================================
    3. Напишите программу Python для построения следующего шаблона, используя вложенный цикл for.
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
    ''')
    h = int(input('Enter height of triangle (in range: from 1 to 100): '))  # preferable value is 5, max 100
    if 0 < h < 100:
        print('\n1st implementation:')  # 1st implementation
        for x in range(1, h + 1):
            for y in range(1, x + 1):
                print('* ', end='')
            print('')
        for x in range(1, h):
            for y in range(1, h + 1 - x):
                print('* ', end='')
            print('')
        print('\n2nd implementation:')  # 2nd implementation
        for x in range(1, h + 1):
            for y in range(1, x + 1):
                print('* ', end='')
            print('')
        for x in range(1, h):
            print('* ' * (h - x))
    else:
        print('Triangle height incorrect')


if RUN_FLAG:
    print('''
    ========================================
    3*. Напишите программу Python для построения следующего шаблона, используя вложенный цикл for.
        *
       *** 
      ***** 
     ******* 
    *********
    ''')
    h = int(input('Enter height of triangle (in range: from 1 to 100): '))  # preferable value is 5, max 100
    if 0 < h < 100:
        for x in range(0, h + 1):
            for y in range(0, h - x):
                print(' ', end='')
            print('*' * (2 * x - 1))
    else:
        print('Triangle height incorrect')


if RUN_FLAG:
    print('''
    ========================================
    4. Даны два целых числа A и В. Выведите все числа от A до B включительно, 
    в порядке возрастания, если A < B, или в порядке убывания если A > B
    ''')
    a = int(input('Enter A: '))
    b = int(input('Enter B: '))
    print('Range from A to B: ', end='')
    if a < b:
        for x in range(a, b + 1):
            print(x, end=' ')
    else:
        for x in range(0, a - b + 1):
            print(a - x, end=' ')


if RUN_FLAG:
    print('''
    ========================================
    5. Даны два целых числа A и B (при этом A < B). Выведите все числа от A до B включительно.
    ''')
    a = int(input('Enter A: '))
    b = int(input('Enter B (B > A): '))
    print('Range from A to B: ', end='')
    if a < b:
        for x in range(a, b + 1):
            print(x, end=' ')
