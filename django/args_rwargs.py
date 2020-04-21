def plus(a, b, *args, **kwargs):
    print(args, kwargs)
    print(args)
    print(kwargs)
    return a + b
# 무한으로 position argument가 무한, keyword argument가 무한


plus(1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, hello=True,
     aa=True, dfa=True, fda=True, fdagfa=True)


def add(*args):
    result = 0
    for number in args:
        result += number
    return result


what = add(1, 2, 3, 4, 3, 4, 3, 4, 3, 5, 2, 35, 13, 5, 3, 5, 3, 5, 3)
print(what)
