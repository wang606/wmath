import wmath
import random
import time


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


def get_random_float_list(n):
    molecule = [random.randint(-50, 50) for _i in range(n)]
    denominator = [random.randint(1, 100) for _k in range(n)]
    _float = [molecule[_n] / denominator[_n] for _n in range(n)]
    return _float


def get_random_float_list2d(m, n):
    molecule = [[random.randint(-50, 50) for _i in range(n)] for _j in range(m)]
    denominator = [[random.randint(1, 100) for _k in range(n)] for _l in range(m)]
    _float = [[molecule[_m][_n] / denominator[_m][_n] for _n in range(n)] for _m in range(m)]
    return _float


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
# let the columns of the matrix be linearly correlated intentionally
a = wmath.Matrix(get_random_float_list2d(10, 10))
a = wmath.Matrix(get_random_list2d(10, 10))
a = wmath.Matrix(get_random_complex_list2d(13, 10))
b = a.part(_rows=None, _cols=[0]).times(wmath.Meta.get_meta(a.kernel[-1][-1], 'ONE') * 4.9) + \
    a.part(_rows=None, _cols=[4]).times(wmath.Meta.get_meta(a.kernel[-1][-1], 'ONE') * -9.8)
a.fill(b, _rows=None, _cols=[1])

# qr decomposition
q, r = a.qr_schmidt_decomposition()
print(a.formula(), end='=')
print(q.formula(), '*', r.formula())
print('\n==========\n')

# verification
print(wmath.Meta.determine_meta(q * r - a, 'ZERO'))
print(wmath.Meta.determine_meta(q.transpose(_new=True).conjugate() * q, 'ONE'))
end_time = time.time()
print(end_time - start_time)
