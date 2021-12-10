"""
cross.py
this script is response for some cross function.
"""
from wmath.meta import Meta
from wmath.polynomial import Polynomial
from wmath.matrix import Matrix, matrix_vertical_stack


def polynomial_roots(_poly: Polynomial):
    __poly = _poly.monic(_new=True)
    _one = Meta.get_meta(__poly.coefficient[-1], 'ONE')
    _zero = Meta.get_meta(__poly.coefficient[-1], 'ZERO')
    _kernel = [[]]
    for _i in range(__poly.degree() - 1, -1, -1):
        _kernel[0].append(-__poly.coefficient[_i])
    for _i in range(__poly.degree() - 1):
        _kernel.append([])
        for _j in range(__poly.degree()):
            if _i == _j:
                _kernel[_i + 1].append(_one)
            else:
                _kernel[_i + 1].append(_zero)
    _matrix = Matrix(_kernel)
    _roots = _matrix.eigenvalue()
    return _roots
