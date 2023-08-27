class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def discription_person(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет ."
              f"Мой рост = {self.height} см, вес = {self.weight} кг.")

    def weight_x2(self):
        print(f'Вес х2 = {self.weight * 2}')

    def update_age(self, let):
        self.age = let


man1 = Person('Axiles', 30, 210, 187)
man2 = Person('Oleg', 40, 166, 144)
man3 = Person('Dupl', 19, 144, 133)

man1.weight_x2()
man1.update_age(99)
man1.discription_person()
