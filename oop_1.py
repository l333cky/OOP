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
        self.is_power = False
        self.is_stopped = True

    # метод возвращающий информацию о машине
    def get_car_info(self):
        info = f"Машина {self.brand} {self.model} {self.color} {self.year} года"
        return info



    # метод объекта
    def start(self):
        car = self.get_car_info()
        if self.is_power :
            print(f"{car} уже заведена")
        else :
            self.is_power= True
            print(f"{car} завелась")

    def turn(self, direction):
        car = self.get_car_info()
        valid_direction = ("налево","направо")
        if direction.lower() in valid_direction:
            print(f"{car} повернула {direction}")
        else:
            print(f"Направление может быть одним из следующих:{valid_direction}")

    def power_off(self):
        car = self.get_car_info()
        if not self.is_power:
            print(f"{car} уже заглушена")
        else:
            if self.is_stopped:
                print(f"{car} заглушена")
                self.is_power=False
            else:
                print(f"Необходимо остановить машину{car} ")


    def go(self):
        car = self.get_car_info()
        if not self.is_power:
            print(f"необходимо завести машину {car}")
        else:
            print(f"{car} поехала прямо")
            self.is_stopped=False

    def __str__(self):
        return f"{self.brand}  {self.model}"

    def stop(self):
        car = self.get_car_info()
        if self.is_power:
            if self.is_stopped:
                print(f"{car} уже остановлена")
            else :
                self.is_stopped = True
                print(f"{car} остановилась")
        else:
            print(f"необходимо завести машину {car}")


    def __str__(self):
        return f"{self.brand} {self.model}"


# создание объекта(экземпляра) класса
car_1 = Car(color='Red', year=2020, brand='bmw', model='x5')
car_2 = Car(color='Black', year=2023, brand='audi', model='a5')

# получение доступа к атрибутам класса
# print(car_1.color) # через имя
# print(Car.color) # через класс

# print(car_2.color)

# вызов метода объекта
car_1.start()
# car_1.go()
# car_1.stop()
car_1.power_off()


#
# car_1.turn(direction="налево")
# car_1.turn(direction="прямо")
# car_2.turn(direction="направо")
#
#
# car_1.stop()
# car_2.power_off()
