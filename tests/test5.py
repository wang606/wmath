import copy
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
a = wmath.Matrix(get_random_complex_list2d(10, 10))
# a = wmath.Matrix(get_random_float_list2d(10, 10))
# a += a.transpose().conjugate()
# upper hessenberg
b, c = a.upper_hessenberg(_unitary_need=True)
print(b.formula(), c.formula())
# verification
print(wmath.Meta.determine_meta(c * a * c.transpose().conjugate() - b, 'ZERO'))
print(wmath.Meta.determine_meta(c * c.transpose().conjugate(), 'ONE'))
# schmidt unitary
q, r = a.qr_schmidt_decomposition(_column_linearly_independent=True)
print(q.formula(), r.formula())
# verification
print(wmath.Meta.determine_meta(q * r - a, 'ZERO'))
print(wmath.Meta.determine_meta(q.transpose().conjugate() * q, 'ONE'))
end_time = time.time()
print(end_time - start_time)
