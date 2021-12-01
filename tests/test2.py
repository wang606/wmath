import wmath
import random
import time
import copy


def get_random_list2d(m, n):
    molecule = [[random.randint(-50, 50) for _i in range(n)] for _j in range(m)]
    denominator = [[random.randint(1, 100) for _k in range(n)] for _l in range(m)]
    fraction = [[wmath.Fraction([molecule[_m][_n], denominator[_m][_n]]) for _n in range(n)] for _m in range(m)]
    return fraction


def get_random_list(n):
    molecule = [random.randint(-50, 50) for _i in range(n)]
    denominator = [random.randint(1, 100) for _k in range(n)]
    fraction = [wmath.Fraction([molecule[_n], denominator[_n]]) for _n in range(n)]
    return fraction


def get_random_float_list2d(m, n):
    molecule = [[random.randint(-50, 50) for _i in range(n)] for _j in range(m)]
    denominator = [[random.randint(1, 100) for _k in range(n)] for _l in range(m)]
    _float = [[molecule[_m][_n] / denominator[_m][_n] for _n in range(n)] for _m in range(m)]
    return _float


start_time = time.time()
a = wmath.Matrix(wmath.list2fraction([[1, 1, -3, -1], [3, -1, -3, 4], [1, 5, -9, -8]]))
b = wmath.Matrix(wmath.list2fraction([[1], [4], [0]]))
c = wmath.non_homogeneous_linear_equations(a, b)
for i in c[0]:
    print(i.formula(), end=', ')
print(c[1][0].formula())
end_time = time.time()
print(end_time - start_time)
