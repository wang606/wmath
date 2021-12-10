# __all__ = ['Meta', 'number_theory', 'paradigm', 'fraction', 'polynomial', 'matrix']
from wmath.meta import *
from wmath.number_theory import *
from wmath.fraction import *
from wmath.paradigm import *
from wmath.polynomial import *
from wmath.matrix import *
from wmath.cross import *


# Meta.GET.ONE
Meta.GET.ONE.int = lambda x: 1
Meta.GET.ONE.float = lambda x: 1.0
Meta.GET.ONE.complex = lambda x: 1 + 0j
Meta.GET.ONE.Fraction = lambda x: Fraction(1)
Meta.GET.ONE.Polynomial = lambda x: Polynomial([Meta.get_meta(x.coefficient[-1], 'ONE')]) \
        if type(x).__name__ == 'Polynomial' else Polynomial([Meta.get_meta(x, 'ONE')])
Meta.GET.ONE.Matrix = lambda x: matrix_one(x.size()[0], x.size()[1], Meta.get_meta(x.kernel[-1][-1], 'ONE')) \
        if type(x).__name__ == 'Matrix' else matrix_one(1, 1, Meta.get_meta(x, 'ONE'))
# Meta.GET.ZERO
Meta.GET.ZERO.int = lambda x: 0
Meta.GET.ZERO.float = lambda x: 0.0
Meta.GET.ZERO.complex = lambda x: 0 + 0j
Meta.GET.ZERO.Fraction = lambda x: Fraction(0)
Meta.GET.ZERO.Polynomial = lambda x: Polynomial([Meta.get_meta(x.coefficient[-1], 'ZERO')]) \
        if type(x).__name__ == 'Polynomial' else Polynomial([Meta.get_meta(x, 'ZERO')])
Meta.GET.ZERO.Matrix = lambda x: matrix_zero(x.size()[0], x.size()[1], Meta.get_meta(x.kernel[-1][-1], 'ZERO')) \
        if type(x).__name__ == 'Matrix' else matrix_zero(1, 1, Meta.get_meta(x, 'ZERO'))
# Meta.DETERMINE
Meta.DETERMINE.ZERO.float = lambda x: True if abs(x) < 1e-8 else False
Meta.DETERMINE.ONE.float = lambda x: True if abs(x - 1.0) < 1e-8 else False
Meta.DETERMINE.ZERO.Fraction = lambda x: True if abs(float(x)) < 1e-8 else False
Meta.DETERMINE.ONE.Fraction = lambda x: True if abs(float(x) - 1.0) < 1e-8 else False
Meta.DETERMINE.ZERO.complex = lambda x: True if abs(x) < 1e-8 else False
Meta.DETERMINE.ONE.complex = lambda x: True if abs(x - 1.0) < 1e-8 else False


def _determine_zero_polynomial(x):
    if type(x).__name__ == 'Polynomial':
        for _i in x.coefficient:
            if not Meta.determine_meta(_i, 'ZERO'):
                return False
        return True
    else:
        return False  # Meta.determine_meta(x, 'ZERO')


def _determine_one_polynomial(x):
    if type(x).__name__ == 'Polynomial':
        for _i in x.coefficient[1:]:
            if not Meta.determine_meta(_i, 'ZERO'):
                return False
        if not Meta.determine_meta(x.coefficient[0], 'ONE'):
            return False
        return True
    else:
        return False  # Meta.determine_meta(x, 'ONE')


Meta.DETERMINE.ZERO.Polynomial = _determine_zero_polynomial
Meta.DETERMINE.ONE.Polynomial = _determine_one_polynomial


def _determine_zero_matrix(x):
    if type(x).__name__ == 'Matrix':
        for _i in x.kernel:
            for _j in _i:
                if not Meta.determine_meta(_j, 'ZERO'):
                    return False
        return True
    else:
        return False  # Meta.determine_meta(x, 'ZERO')


def _determine_one_matrix(x):
    if type(x).__name__ == 'Matrix':
        for _i in range(x.size()[0]):
            for _j in range(x.size()[1]):
                if _i == _j:
                    if not Meta.determine_meta(x.kernel[_i][_j], 'ONE'):
                        return False
                if _i != _j:
                    if not Meta.determine_meta(x.kernel[_i][_j], 'ZERO'):
                        return False
        return True
    else:
        return False  # Meta.determine_meta(x, 'ONE')


Meta.DETERMINE.ZERO.Matrix = _determine_zero_matrix
Meta.DETERMINE.ONE.Matrix = _determine_one_matrix
