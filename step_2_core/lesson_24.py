try:
    a = int(input("Введите первое значение : "))
    b = int(input("Введите второе значение : "))

    result = a / b
except ZeroDivisionError:
    result = 0
    print("Вы разделили на 0.")
except ValueError:
    result = 'Error!!!'
    "Вы ввели значение отличное от цифры"
print(f'Результат деления : {result}')
#ZeroDivisionError
#ValueError
