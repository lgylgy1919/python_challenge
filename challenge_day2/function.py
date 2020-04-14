def say_hello():
    print("hello")
    print("bye")


say_hello()


def say_hi(who):
    print("hello", who)


say_hi("Nico")


def say_bye(name="anonymous"):
    print("bye", name)


say_bye()


def plus(a, b):
    print(a+b)


plus(2, 5)


def minus(a, b=0):
    print(a-b)


minus(7, 3)
minus(3)
