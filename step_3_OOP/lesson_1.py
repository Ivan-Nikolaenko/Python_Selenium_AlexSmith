class Person():
    # Модель человека

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Человек создан.")

    def sing(self):
        print(self.name + " поёт.")

    def smoke(self):
        print(self.name + " курит.")

    def dance(self):
        print(self.name + " танцует.")


man = Person('Sting', 30)
woman = Person('Dasha',25)

print(man.name)
man.smoke()
man.dance()
woman.dance()
