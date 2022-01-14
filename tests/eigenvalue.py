import wmath
import random
import time


def get_random_float_list2d(m, n):
    molecule = [[random.randint(-50, 50) for _i in range(n)] for _j in range(m)]
    denominator = [[random.randint(1, 100) for _k in range(n)] for _l in range(m)]
    _float = [[molecule[_m][_n] / denominator[_m][_n] for _n in range(n)] for _m in range(m)]
    return _float


def get_random_list2d(m, n):
    molecule = [[random.randint(-50, 50) for _i in range(n)] for _j in range(m)]
    denominator = [[random.randint(1, 100) for _k in range(n)] for _l in range(m)]
    fraction = [[wmath.Fraction([molecule[_m][_n], denominator[_m][_n]]) for _n in range(n)] for _m in range(m)]
    return fraction


def get_random_complex_list2d(m, n):
    real = [[random.randint(-50, 50) for _i in range(n)] for _j in range(m)]
    imag = [[random.randint(-50, 50) for _i in range(n)] for _j in range(m)]
    _kernel = []
    for _i in range(m):
        _kernel.append([])
        for _j in range(n):
            _kernel[_i].append(complex(real[_i][_j], imag[_i][_j]))
    return _kernel


start_time = time.time()
# a = wmath.Matrix(get_random_complex_list2d(50, 50))
a = wmath.Matrix(wmath.list2complex(get_random_float_list2d(50, 50)))
# a = wmath.Matrix(get_random_float_list2d(10, 10))
# a += a.transpose().conjugate()
b = a.eigenvalue()
for _i in b:
    print(_i)
end_time = time.time()
print(end_time - start_time)
