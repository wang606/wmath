# __all__ = ['Meta', 'number_theory', 'fraction', 'polynomial', 'matrix']
from meta import *
from number_theory import *
from fraction import *
from polynomial import *
from matrix import *


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
# Meta.GET.ANY
class ANY:
    def __str__(self):
        return 'any({0})'.format(type(self).__name__)
    def formula(self):
        return 'any({0})'.format(type(self).__name__)
    def __eq__(self, other):
        if type(self).__name__ == type(other).__name__ and str(self) == str(other):
            return True
        else:
            return False
Meta.GET.ANY.int = lambda x: type('int', (ANY, ), {})()
Meta.GET.ANY.float = lambda x: type('float', (ANY, ), {})()
Meta.GET.ANY.complex = lambda x: type('complex', (ANY, ), {})()
Meta.GET.ANY.Fraction = lambda x: type('Fraction', (ANY, ), {})()
Meta.GET.ANY.Polynomial = lambda x: type('Polynomial', (ANY, ), {})()
Meta.GET.ANY.Matrix = lambda x: type('Matrix', (ANY, ), {})()
