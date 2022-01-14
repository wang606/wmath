import wmath
import random
import time


def get_random_float_list2d(m, n):
    molecule = [[random.randint(-50, 50) for _i in range(n)] for _j in range(m)]
    denominator = [[random.randint(1, 100) for _k in range(n)] for _l in range(m)]
    _float = [[molecule[_m][_n] / denominator[_m][_n] for _n in range(n)] for _m in range(m)]
    return _float


def get_random_float_list(n):
    molecule = [random.randint(-50, 50) for _i in range(n)]
    denominator = [random.randint(1, 100) for _k in range(n)]
    _float = [molecule[_n] / denominator[_n] for _n in range(n)]
    return _float


def get_random_complex_list(n):
    real = [random.randint(-50, 50) for _i in range(n)]
    imag = [random.randint(-50, 50) for _i in range(n)]
    _kernel = []
    for _j in range(n):
        _kernel.append(complex(real[_j], imag[_j]))
    return _kernel


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
n = 150
c = get_random_float_list(n)
print(c[::-1])
a = wmath.Polynomial(wmath.list2complex(c))
b = wmath.polynomial_roots(a)
for _i in b:
    print(_i, a.value(_i))
end_time = time.time()
print(end_time - start_time)
