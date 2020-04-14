def plus(a, b):
    return a-b


# keyword arguments(순서가 상관없다)
result = plus(b=30, a=1)
print(result)


# 인자로 str,int 모두 가능하다.
def say_hello(name, age):
    return f"hello {name} you are {age} years old"


hello = say_hello("nico", 12)
print(hello)

# keyword arguments(순서가 상관없다)
hi = say_hello(age="12", name="nico")
print(hi)


# 이 경우엔 str타입만 인자로 넣을 수 있다.
def say_bye(name, age):
    return "hello " + name + " you are " + age + " years old"


bye = say_bye("nico", "12")
print(bye)
