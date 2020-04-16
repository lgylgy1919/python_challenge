# 다른 파이썬 파일에서 함수를 가져올 수 있다.
from calculator import plus, minus
# 필요한 부분만 import하는게 좋다.
from math import ceil as sexy_ceil, fsum, fabs

# 함수 이름을 바꾸는 것도 가능하다.(ceil -> sexy_ceil)
print(sexy_ceil(1.2))
print(fabs(-1.2))
print(fsum([1, 2, 3, 4, 5, 6, 7]))


print(plus(2, 3),  minus(6, 1))
