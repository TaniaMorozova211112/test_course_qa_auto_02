# Створіть клас Employee, який має атрибути name та salary.

class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary


# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department,
# а клас Developer - атрибут programming_language.

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, programming_language=None, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language



# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім('я, зарплата, відділ), '
# а також атрибут team_size, який вказує на кількість розробників у команді,
# якою керує керівник.)

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )
        self.team_size = team_size






# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"Perimeter is {self.perimeter():.2f}. Area is {self.area():.2f}."

# Наслідуйте від нього декілька (> 2) інших фігур,
# та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
# та ініціалізуватись через конструктор.
class Rhomb(Figure):
    def __init__(self, side_length, height_to_this_side):
        self.__side_length = side_length
        self.__height_to_this_side = height_to_this_side

    def perimeter(self):
        return 4 * self.__side_length

    def area(self):
        return self.__side_length * self.__height_to_this_side

    def __str__(self):
        return super().__str__() + " This is Rhomb!"



class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def area(self):
        return self.__length * self.__width

    def __str__(self):
        return super().__str__() + " This is Rectangle!"


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return 2 * pi * self.__radius

    def area(self):
        return pi * (self.__radius ** 2)

    def __str__(self):
        return super().__str__() + " This is Circle!"


# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте
# та виведіть в консоль площу та периметр кожної.
rhomb = Rhomb(4, 6)
rectangle = Rectangle(5, 10)
circle = Circle(7)

list_figure = [rhomb, rectangle, circle]

for figure in list_figure:
    print(figure)





