import wmath
import random
import time


def get_random_list2d(n):
    molecule = [[random.randint(-50, 50) for _i in range(n)] for _j in range(n)]
    denominator = [[random.randint(1, 100) for _k in range(n)] for _l in range(n)]
    fraction = [[wmath.Fraction([molecule[_m][_n], denominator[_m][_n]]) for _m in range(n)] for _n in range(n)]
    return fraction


def get_random_list(n):
    molecule = [random.randint(-50, 50) for _i in range(n)]
    denominator = [random.randint(1, 100) for _k in range(n)]
    fraction = [wmath.Fraction([molecule[_n], denominator[_n]]) for _n in range(n)]
    return fraction


start_time = time.time()
m, n = 10, 5
a = [wmath.Matrix(get_random_list2d(n)) for _i in range(m)]
a = wmath.Polynomial(a)
print(a.formula())
b = [[wmath.Polynomial(get_random_list(n)) for _j in range(m)] for _k in range(m)]
b = wmath.Matrix(b)
print(b.formula())
end_time = time.time()
print(end_time - start_time)
