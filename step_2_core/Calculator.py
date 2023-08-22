try:
    a = int(input("Введите первое значение : "))
    b = int(input("Введите второе значение : "))
    arif = str(input("Введите знак арифметический  операции (Один из : + , - , / , *) : "))
except ValueError:
    print('Ошибка!Введите число!')
try:
    if arif == '+':
        print('Результат сложения = ' + str(a + b))
    elif arif == '-':
        print('Результат вычетания = ' + str(a - b))
    elif arif == '/':
        print('Результат деления = ' + str(a / b))
    elif arif == '/':
        print('Результат умножения = ' + str(a * b))
    else:
        print('Эхх я больше нечего не умею . . .')
except ZeroDivisionError:
    print('Вы разделили на 0.')
