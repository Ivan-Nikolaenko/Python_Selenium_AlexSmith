from lesson_2 import Person


class Employee(Person):
    """Наследуемся от супер класса"""

    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)
        self.rage = 100

    def get_rage(self):
        print(f"Ярость нашего персонажа = {self.rage}")

    def weight_x2(self):
        print(f'Его вес равен !!!!---> х2 = {self.weight * 2}')


rab = Employee("Povar", 31, 922, 200)
man = Person("Alex", 22, 12, 21)
man.weight_x2()
rab.weight_x2()

