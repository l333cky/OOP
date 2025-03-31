# Родительский (базовый) класс для класса Student
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def hello(self):
        print(f"Привет, меня зовут {self.name} {self.lastname}")

    def bye(self):
        pass

# Дочерний (производный) класс от класса Person
class Student(Person):
    # Конструктор дочернего должен иметь атрибуты родительского класса и атрибуты дочернего
    def __init__(self, name, lastname, age, group, ticket, form_study):
        super().__init__(name, lastname, age)
        self.group = group
        self.ticket = ticket
        self.form_study = form_study
        print (f"Покеда)")


person_1 = Person (name="Dima", lastname="Ivanov", age=24)
person_1.hello()
person_1.bye()
