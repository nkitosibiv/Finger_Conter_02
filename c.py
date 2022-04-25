from turtle import color


class Vehicle:
    def __init__(self, price, type):
        self.color = color
        self.price = price
        self.type = type
    def drive(self):
        print(self.color, self.type,'poexal' )
    def brake(self):
        print(self.color, self.type, 'остановился')

car1 = Vehicle('белый' , 20000, 'автомобиль')
car2 = Vehicle('красный' , 30000, 'самолёт')
car1.drive()
car1.brake()