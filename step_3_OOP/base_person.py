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

    def get_weight(self):
        print(f'Мой вес = {self.weight}')

    def update_age(self, let):
        self.age = let


man = Person("alex", 20, 30, 50)
man.discription_person()
man.get_weight()
man.weight_x2()
