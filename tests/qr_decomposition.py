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
# a = wmath.Matrix(get_random_complex_list2d(5, 5))
a = wmath.Matrix(get_random_float_list2d(5, 5))
# a += a.transpose().conjugate()
b = a.part(_rows=None, _cols=[0]).times(wmath.Meta.get_meta(a.kernel[-1][-1], 'ONE') * 4.9) + \
    a.part(_rows=None, _cols=[4]).times(wmath.Meta.get_meta(a.kernel[-1][-1], 'ONE') * -9.8)
a.fill(b, _rows=None, _cols=[1])
t0 = time.time()

# schmidt unitary
q, r = a.qr_schmidt_decomposition()
print(q.formula(), r.formula())
# verification
print(wmath.Meta.determine_meta(q * r - a, 'ZERO'))
print(wmath.Meta.determine_meta(q.transpose().conjugate() * q, 'ONE'))
t1 = time.time()

# householder unitary
q1, r1 = a.qr_householder_decomposition(_unitary_need=True)
print(q1.formula(), r1.formula())
# verification
print(wmath.Meta.determine_meta(q1 * r1 - a, 'ZERO'))
print(wmath.Meta.determine_meta(q1.transpose().conjugate() * q1, 'ONE'))
t2 = time.time()

# givens unitary
q2, r2 = a.qr_givens_decomposition()
print(q2.formula(), r2.formula())
# verification
print(wmath.Meta.determine_meta(q2 * r2 - a, 'ZERO'))
print(wmath.Meta.determine_meta(q2.transpose().conjugate() * q2, 'ONE'))
t3 = time.time()

# upper hessenberg
b, c = a.upper_hessenberg(_unitary_need=True)
print(b.formula(), c.formula())
# verification
print(wmath.Meta.determine_meta(c * a * c.transpose().conjugate() - b, 'ZERO'))
print(wmath.Meta.determine_meta(c * c.transpose().conjugate(), 'ONE'))
t4 = time.time()

print(t1 - t0, t2 - t1, t3 - t2, t4 - t3)
end_time = time.time()
print(end_time - start_time)
