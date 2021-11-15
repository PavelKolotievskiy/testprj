# Создать класс в конструктор которого передается одно число В этом классе дожен быть метод show, который распечатывает переданное число.
class myClass:
    def __init__(self, value):
        self.data = value

    def show(self):
        print(self.data)


f1 = myClass(1)
f1.show()


# Создать класс, который наследуется от предыдущего класса и в этот класс передается два числа. Данный класс реализует метод calc, который складывает эти два числа.
class myChild(myClass):
    def __init__(self, value, me):
        super().__init__(value)
        self.me = me
        self.value = value

    def calc(self):
        res = self.me + self.value
        super().show()


f2 = myChild(2, 2)
f2.calc()

# Создать блок try/except/finally Внутри блока try создать выражение, которое делит на 0. Перехватить эту ошибку и распечатать сообщение пользвоателю.
try:
    s1 = 12
    s2 = 0
    s3 = s1 / s2
    print(f"Result try {s3}")
except ZeroDivisionError:
    print("Нельзя делить на ноль")
else:
    print("Else")
finally:
    print("Finally")


# Создать декоратор, который перед запуском функции распечатывает все аргументы вызываемой функции.
def mydec(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return inner


@mydec
def func(x):
    return x


func = mydec(func)
func(3)


# Создать класс в котором применить декоартор @property для доступа к внутренней переменной.
class MyClass2:
    def __init__(self, value):
        self._data = value

    @property
    def data(self):
        return self._data + 1


f1 = MyClass2(2)
print(f1.data)


# Создать генератор который возвращается числа от 1 до 10
def MyGen():
    i = 1
    while i <= 10:
        yield i
        i += 1


for a in MyGen():
    print(a)

# С помощью стандартной функции collections.namedtuple создать объект для хранения точки в трехмерном пространстве.
import collections
Point = collections.namedtuple("point", ["x", "y", "z"])

p1 = Point(x=1, y=2, z=3)

# Создать пакет в котором будет функция для распечатки текущей даты (можно использовать пакет datetime). Для данного пакета подготовить setup.py для установки.
import sys
sys.path.append(r'mypackage/src')

import mypackage.src
from mypackage.src import mydate
mydate.curdate()