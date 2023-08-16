age = int(input())
if 25 <= age <= 50:
    print(f'Мне {age} лет')
elif age < 25:
    print('Мне меньше 25')
else:
    print('Я очень стар')

pin = 1234
pin_personal = int(input("Введите пароль : "))
if pin == pin_personal:
    print('Какую сумму вы хотите снять ?')
else:
    print('У вас осталось 2 попытки!')
    pin_personal = int(input("Введите пароль : "))
    if pin == pin_personal:
        print('Какую сумму вы хотите снять ?')
    else:
        print('У вас осталось 1 попытка!')
        pin_personal = int(input("Введите пароль : "))
        if pin == pin_personal:
            print('Какую сумму вы хотите снять ?')
        else:
            print('BLOCKED')
