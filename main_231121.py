import datetime
import random
import string


run_flag = False  # change it to True if you wanna run all parts of homework


if run_flag:  # change it to True to run
    print('''
    ========================================
    0) (Пример) Пользователь вводит год рождения с клавы, вывести возраст человека.
    ''')
    born_year = int(input('Enter your birthday year pls:'))
    # TODO: Handle exception int from str
    current_year = datetime.date.today().year
    if -1 < born_year < current_year + 1:
        print("You are {} year(s) old".format(current_year - born_year))
    else:
        print('ERROR! The birthday year is wrong!')


if run_flag:
    print('''
    ========================================
    1) (Практика) В переменной month лежит какое-то число из интервала от 1 до 12.
        Определите в какую пору года попадает этот месяц (зима, лето, весна, осень).
    ''')
    random.seed()  # Initialize the random number generator
    month = random.randint(1, 12)  # random integer that 1 <= X <= 12, our month
    print(f"Month with number {month} is", end=' ')
    if month < 3:
        print('Winter month')
    elif 2 < month < 6:
        print('Spring month')
    elif 5 < month < 9:
        print('Summer month')
    elif 8 < month < 12:
        print('Autumn month')
    else:
        print('Winter month')


if run_flag:
    print('''
    ========================================
    2) (Практика) Дана строка, состоящая из символов, например, 'abcde'. Проверьте, что
        первым символом этой строки является буква 'а'. Если это так - выведите 'yes',
        в противном случае выведите 'no'.
    ''')
    random.seed()
    letters = string.ascii_lowercase  # all abc lowercase letters
    string_length = random.randint(1, 50)  # string have random length
    # creating string from letters using loop with our length
    test_string = ''.join(random.choice(letters) for i in range(string_length))
    print(f"Is string \"{test_string}\" starts with 'a'? - ", end='')
    if test_string[:1] == 'a':
        print('Yes')
    else:
        print('No')


if run_flag:
    print('''
    ========================================
    3) (Практика) Дана строка из 6-ти цифр. Проверьте, что сумма первых трёх цифр
        равняется сумме вторых трёх цифр. Если это так - выведите 'yes', в
        противном случае выведите 'no'.
    ''')
    int_str = input('Enter 6-digit number: ')
    print('Is summary of first 3 digits equal summary of past 3 digits? - ', end='')
    dif = int(int_str[0]) + int(int_str[1]) + int(int_str[2]) - int(int_str[3]) - int(int_str[4]) - int(int_str[5])
    if dif == 0:
        print('Yes')
    else:
        print('No')


if run_flag:
    print('''
    ========================================
    4) (ДЗ) За день машина проезжает n километров. Сколько дней нужно, что бы проехать
        маршрут m километров? Программа получает на вход числа n и m.
    ''')
    daily_trip = int(input('Enter daily car distance: '))
    total_trip = int(input('Enter total trip distance: '))
    days = total_trip // daily_trip
    hours = int(((total_trip % daily_trip) / daily_trip) * 24)
    if hours == 0:
        print(f"Driver needs {days} day(s) to finish trip")
    else:
        print(f"Driver needs {days} day(s) {hours} hour(s) to finish trip")


if run_flag:
    print('''
    ========================================
    5) (ДЗ) Пользователь вводит трёхзначное число. Найдите сумму его цифр
        (используйте %).
    ''')
    number = int(input('Enter 3-digits number: '))
    total = (number % 10) + ((number % 100 - number % 10) // 10) + ((number - number % 10) // 100)
    print(f"Sum of digits = {total}")


if run_flag:
    print('''
    ========================================
    6) (ДЗ) Найти максимальное число из трёх. Числа вводятся с клавиатуры.
    ''')
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))
    num3 = int(input('Enter 3rd number: '))
    if num1 > num2:
        if num1 > num3:
            print(num1, end='')
        else:
            print(num3, end='')
    else:
        if num2 > num3:
            print(num2, end='')
        else:
            print(num3, end='')
    print(' is biggest of them')


if run_flag:
    print('''
    ========================================
    7) (ДЗ) Определить високосный год или нет. Число вводится с клавиатуры.
    ''')
    if int(input('Enter year: ')) % 4 > 0:
        print('That isnt leap year')
    else:
        print('That\'s leap year')


if run_flag:
    print('''
    ========================================
    8) (ДЗ) Определить чётное или нечётное число. Число вводится с клавиатуры.
    ''')
    if int(input('Enter any number: ')) % 2 > 0:
        print('That isnt even number')
    else:
        print('That\'s even number')


if run_flag:
    print('''
    ========================================
    9) (ДЗ*) Найти корни квадратного уравнения и вывести их на экран, если они есть.
        Если корней нет, то вывести сообщение об этом. Конкретное квадратное уравнение
        определяется коэффициентами a, b, c, которые вводит пользователь.
    ''')
    '''
    if c = 0  >>  x = 0  and  x = - b/a
    if b = 0  >> 
                if -c/a > 0  >>  x = +sqrt(c/a)  and  x = -sqrt(c/a)
                if -c/a < 0  >>  The equation in the set of real number has no solutions
    if c = 0 and b = 0  >>  x = 0
    if allOk  >>  D = b^2 - 4ac
                D > 0  >>  x1 = (-b+sqrt(D))/2a     x2 = (-b-sqrt(D))/2a
                D = 0   >>  x = -b/2a
                D < 0   >> The equation has no solution
    '''
    print("Quadratic equation have view: (a * x^2) + (b * x) + (c) = 0, where a =/= 0")
    a = int(input('Enter a number: '))
    b = int(input('Enter b number: '))
    c = int(input('Enter c number: '))
    print(f"Quadratic equation: ({a} * x^2) + ({b} * x) + ({c}) = 0")
    if c == 0:
        if b == 0:
            print("Quadratic root for the equation: x = 0")
        else:
            print(f"Quadratic roots for the equation: x = 0, x = {-b/a}")
    elif b == 0:
        if -c/a > 0:
            if c < 0:
                c *= -1
            print(f"Quadratic roots for the equation: x = {(c/a)**(1/2)}, x = {-((c/a)**(1/2))}")
        else:
            print("The equation in the set of real number has no solutions")
    else:
        d = b * b - 4 * a * c
        if d > 0:
            print(f"Quadratic roots for the equation: x = {(-b+(d**(1/2)))/(2*a)}, x = {(-b-(d**(1/2)))/(2*a)}")
        elif d == 0:
            print(f"Quadratic root for the equation: x = {-b / (2*a)}")
        else:
            print("The equation has no solution")


if run_flag:
    print('''
    ========================================
    10) (ДЗ*) Дана следующая функция y = f(x):
        y = 2x - 10, если x > 0
        y = 0, если x = 0
        y = 2 * |x| - 1, если x < 0
        Найти значение функции по x, который вводится с клавиатуры.
    ''')
    print('''
    Function y = f(x):
        y = 2x - 10, if x > 0
        y = 0, if x = 0
        y = 2|x| - 1, if x < 0
    ''')
    x = int(input('Enter X to find solution of function: '))
    if x > 0:
        print(f"y = {2 * x - 10}")
    elif x == 0:
        print("y = 0")
    else:
        print(f"y = {-2 * x - 1}")





