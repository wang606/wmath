# __all__ = ['Meta', 'number_theory', 'fraction', 'polynomial', 'matrix']
from meta import *
from number_theory import *
from fraction import *
from polynomial import *
from matrix import *
# define 'ONE' and 'ZERO' in the field Fraction.
if not hasattr(Meta.GET.ONE, 'Fraction'):
    Meta.GET.ONE.Fraction = lambda x: Fraction(1)
if not hasattr(Meta.GET.ZERO, 'Fraction'):
    Meta.GET.ZERO.Fraction = lambda x: Fraction(0)
# define 'ONE' and 'ZERO' in the Polynomial field.
if not hasattr(Meta.GET.ONE, 'Polynomial'):
    Meta.GET.ONE.Polynomial = lambda x: Polynomial([Meta.get_meta(x.coefficient[-1], 'ONE')]) \
        if type(x).__name__ == 'Polynomial' else Polynomial([Meta.get_meta(x, 'ONE')])
if not hasattr(Meta.GET.ZERO, 'Polynomial'):
    Meta.GET.ZERO.Polynomial = lambda x: Polynomial([Meta.get_meta(x.coefficient[-1], 'ZERO')]) \
        if type(x).__name__ == 'Polynomial' else Polynomial([Meta.get_meta(x, 'ZERO')])
# define 'ONE' and 'ZERO' in the Matrix field.
if not hasattr(Meta.GET.ONE, 'Matrix'):
    Meta.GET.ONE.Matrix = lambda x: matrix_one(x.size()[0], x.size()[1], Meta.get_meta(x.kernel[-1][-1], 'ONE')) \
        if type(x).__name__ == 'Matrix' else matrix_one(1, 1, Meta.get_meta(x, 'ONE'))
if not hasattr(Meta.GET.ZERO, 'Matrix'):
    Meta.GET.ZERO.Matrix = lambda x: matrix_zero(x.size()[0], x.size()[1], Meta.get_meta(x.kernel[-1][-1], 'ZERO')) \
        if type(x).__name__ == 'Matrix' else matrix_zero(1, 1, Meta.get_meta(x, 'ZERO'))
