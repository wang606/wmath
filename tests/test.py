import wmath
import random
import time
import copy


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


def root(_poly: wmath.Polynomial, _start: float, y_precision: float = 1e-12, _step: float = 1e-5):
    _y = _poly.value(_start)
    while abs(_y) > y_precision:
        _y1 = _poly.value(_start + _step)
        _y2 = _poly.value(_start + _step * 1j)
        if abs(_y1 - _y) > abs(_y2 - _y):
            _start -= _y / (_y1 - _y) * _step
        else:
            _start -= (_y / (_y2 - _y)) * _step * 1j
        _y = _poly.value(_start)
    return _start


def root1(_poly: wmath.Polynomial, _start: float, y_precision: float = 1e-12, _step: float = 1, x_precision: float = 1e-12):
    _y = _poly.value(_start)
    while abs(_y) > y_precision:
        if _step < x_precision:
            return None
        _next = _start
        _next_abs_y = abs(_y)
        for _i in [-_step, _step]:
            for _j in [-_step, _step]:
                _abs_y = abs(_poly.value(_start + _i + _j * 1j))
                if _abs_y < _next_abs_y:
                    _next = _start + _i + _j * 1j
                    _next_abs_y = _abs_y
        if _next == _start:
            _step /= 2
        else:
            _start = _next
        _y = _poly.value(_start)
    return _start


start_time = time.time()
n = 15
a = wmath.Polynomial(get_random_complex_list(n))
b = wmath.polynomial_roots(a)
for _i in b:
    print(_i, a.value(_i))
end_time = time.time()
print(end_time - start_time)
