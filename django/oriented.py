class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4

    def start(self):
        print(self.color)
        print(self.doors)
        print("I start")


# 파이썬은 method를 호출할 때 그 method의 instance를 첫번째 argumet로 사용한다.
bmw = Car()
bmw.color = "Red Sexy Red"
bmw.start()
# bmw.start() = bmw.start(bmw)
# Red Sexy Red / I start 출련된다. start method의 첫 번째 print의 argument는 자기 자신(self, 여기선 bmw)의 color이다.


porche = Car()
porche.color = "Red"
print(porche.windows)
# 4
print(porche.color)
# Red

ferrari = Car()
ferrari.color = 'Yellow'
print(ferrari.color)
# Yellow

print(dir(Car))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'doors', 'seats', 'start', 'wheels', 'windows']


class Book():
    page = 4
    thick = 3
    writer = 10

    def __str__(self):
        return "lalalalal"


harry = Book()
print(harry)
# lalalal출력
print(harry.__str__())
# lalalal 출력

