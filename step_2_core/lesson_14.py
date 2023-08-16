word = str(input("Введите слово для теста : "))

if word[:]==word[::-1]:
    print(f'Слово {word} является полиндромом')
else:
    print(f'Слово {word} не палиндром')


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(number) #выводми список
print(number[:5]) # C 0 по 4
print(number[5:]) # C 5 до конца
print(number[5:10]) # C 5 до 9
print(number[::5]) # Шаг 5
print(number[1::3]) # C начиная с 1 и шагом 3
print(number[:-4]) # Все кроме 4 последних
print(number[1:-1]) # Без первого и последнего
print(number[::-1]) # Реверс списка
print(number[::-2]) # Реверс с шагом 2
print(number[-2::-2]) #Реверс с 2 с конца и щагом 2
print(number[10::-15])