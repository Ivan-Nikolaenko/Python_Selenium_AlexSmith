class Car:
    def __init__(self, model, year, v_engine, price, mileage):
        self.model = model
        self.year = year
        self.v_engine = v_engine
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def discription_car(self):
        print(f"Марка машины : {self.model}, год выпуска {self.year},"
              f" обьем двигателя = {self.v_engine}, цена = {self.price}$,пробег = {self.mileage}, "
              f"кол-во колёс = {self.wheels}")


betmobile = Car("BMW", 2023, "v12", 204442, 1000)
betmobile.discription_car()


class Truck(Car):

    def __init__(self, model, year, v_engine, price, mileage):
        super().__init__(model, year, v_engine, price, mileage)
        self.wheels = 8

    def discription_car(self):
        print(f"Марка Грузовика : {self.model}, год выпуска {self.year},"
              f" обьем двигателя = {self.v_engine}, цена = {self.price}$,пробег = {self.mileage}, "
              f"кол-во колёс = {self.wheels}")


super_truck = Truck("Kamaz", 1999, "v8", 10000, 2888888)
super_truck.discription_car()
