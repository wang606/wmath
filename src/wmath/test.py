import wmath
import random
import copy
import time


n = 50
a = [[random.randint(1, 100) for _i in range(n)] for _j in range(n)]
a = wmath.list2fraction(a)
_list = [i for i in range(n)]
t0 = time.time()
print(wmath.determinant_upper_triangle(a))
t1 = time.time()
a = wmath.Matrix(a)
print(a)
print(t1 - t0)
