"""
Создание классов и их экземпляров (объектов) имеющих определенные свойства(атрибуты) и методы (функции)

Основные понятие ООП:
Абстрагирование
Инкапсуляция
Наследование
Полиморфизм

"""

class Car:
    # атрибуты класса (общие для всех объектов
    color = 'Black'
    year = 2020

    def __init__(self, color, year, brand, model):
        self.color = color
        self.year = year
        self.brand = brand
        self.model = model


    # метод объекта
    def start(self):
        print(f"Машина {self.brand} {self.model} завелась")


# создание объекта(экземпляра) класса
car_1 = Car(color='Red', year=2020, brand='bmw', model='x5')
car_2 = Car(color='Black', year=2023, brand='audi', model='a5')

# получение доступа к атрибутам класса
print(car_1.color) # через имя
print(Car.color) # через класс

print(car_2.color)

# вызов метода объекта
car_1.start()
car_2.start()

print(car_1.color)
print(car_2.brand)
print(car_2.year)