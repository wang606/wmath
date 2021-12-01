"""
polynomial.py
this script is response for the related problems in polynomial.
"""
from wmath.meta import Meta
from wmath.number_theory import (greatest_common_divisor_in_list,
                                 least_common_multiple_in_list,
                                 prime_factor_without_exp,
                                 factor)
from wmath.paradigm import Paradigm
from wmath.fraction import Fraction
from copy import deepcopy


class Polynomial(Paradigm):
    """
    define the class of polynomial and related operations among them.
    """
    def __init__(self, coefficient: list):
        super().__init__()
        assert coefficient
        _type = type(coefficient[-1]).__name__
        _coefficient = []
        for _i in coefficient:
            assert type(_i).__name__ == _type
            _coefficient.append(_i)
        while len(_coefficient) > 1 and Meta.determine_meta(_coefficient[-1], 'ZERO'):
            _coefficient.pop()
        self.coefficient = _coefficient

    def __str__(self):
        _str = '('
        for _i in range(self.degree(), 0, -1):
            _str += str(self.coefficient[_i]) + ')x**' + str(_i) + '+('
        _str += str(self.coefficient[0]) + ')'
        return _str

    def __pos__(self):
        return deepcopy(self)

    def __neg__(self):
        _coefficient = []
        for _i in self.coefficient:
            _coefficient.append(-_i)
        return Polynomial(_coefficient)

    def __eq__(self, other):
        assert self.basic_data_type().__name__ == other.basic_data_type().__name__
        if self.coefficient == other.coefficient:
            return True
        if self.degree() != other.degree():
            return False
        for _i in range(self.degree() + 1):
            if self.coefficient[_i] != other.coefficient[_i]:
                return False
        return True

    def __add__(self, other):
        assert self.basic_data_type().__name__ == other.basic_data_type().__name__
        _degree = max(self.degree(), other.degree())
        _coefficient = [Meta.get_meta(self.coefficient[-1], 'ZERO') for _i in range(_degree + 1)]
        for _i in range(_degree + 1):
            if _i <= self.degree():
                _coefficient[_i] += self.coefficient[_i]
            if _i <= other.degree():
                _coefficient[_i] += other.coefficient[_i]
        return Polynomial(_coefficient)

    def __sub__(self, other):
        assert self.basic_data_type().__name__ == other.basic_data_type().__name__
        _degree = max(self.degree(), other.degree())
        _coefficient = [Meta.get_meta(self.coefficient[-1], 'ZERO') for _i in range(_degree + 1)]
        for _i in range(_degree + 1):
            if _i <= self.degree():
                _coefficient[_i] += self.coefficient[_i]
            if _i <= other.degree():
                _coefficient[_i] -= other.coefficient[_i]
        return Polynomial(_coefficient)

    def __mul__(self, other):
        assert self.basic_data_type().__name__ == other.basic_data_type().__name__
        _degree = self.degree() + other.degree()
        _coefficient = [Meta.get_meta(self.coefficient[-1], 'ZERO') for _i in range(_degree + 1)]
        for _i in range(self.degree() + 1):
            for _j in range(other.degree() + 1):
                _coefficient[_i + _j] += self.coefficient[_i] * other.coefficient[_j]
        return Polynomial(_coefficient)

    def __truediv__(self, other):
        assert self.basic_data_type().__name__ == other.basic_data_type().__name__
        _self = +self
        if _self.degree() < other.degree():
            return Polynomial([Meta.get_meta(self.coefficient[-1], 'ZERO')]), _self
        if other.degree() == 0:
            return _self.times(Meta.get_meta(self.coefficient[-1], 'ONE') / other.coefficient[0]), \
                   Polynomial([Meta.get_meta(self.coefficient[-1], 'ZERO')])
        _degree = _self.degree() - other.degree()
        _coefficient = [Meta.get_meta(self.coefficient[-1], 'ZERO') for _i in range(_degree + 1)]
        while _self.degree() >= other.degree():
            _degree = _self.degree()
            _coefficient[_self.degree() - other.degree()] = _self.coefficient[-1] / other.coefficient[-1]
            _self -= other.times(_coefficient[_self.degree() - other.degree()], _self.degree() - other.degree(), True)
            if _self.degree() == _degree:
                _self.coefficient.pop()
        return Polynomial(_coefficient), _self

    def __floordiv__(self, other):
        return (self / other)[0]

    def __mod__(self, other):
        return (self / other)[1]

    def __pow__(self, power: int, modulo=None):
        _self = +self
        _pow = Polynomial([Meta.get_meta(self.coefficient[-1], 'ONE')])
        while power:
            if modulo:
                if power & 1:
                    _pow = _pow * _self % modulo
                _self = _self * _self % modulo
            else:
                if power & 1:
                    _pow *= _self
                _self *= _self
            power >>= 1
        return _pow

    def basic_data_type(self):
        """
        basic data type of this Polynomial.
        :return: (type)
        """
        return type(self.coefficient[-1])

    def degree(self):
        """
        degree of this polynomial.
        :return: (int)
        """
        return len(self.coefficient) - 1

    def value(self, x):
        """
        calc the value of the corresponding polynomial function where x is designated.
        :param x: (self.basic_data_type()) independent variable
        :return: (self.basic_data_type()) value
        """
        _value = Meta.get_meta(self.coefficient[-1], 'ZERO')
        for _i in range(self.degree() + 1):
            _value += self.coefficient[_i] * x ** _i
        return _value

    def monic(self, _new: bool = False):
        """
        return a monic polynomial with a same coefficient ratios of {self}.
        _new decides whether to return a new polynomial or applying change on {self}.
        :param _new: (bool)
        :return: (Polynomial) as above
        """
        if _new:
            _self = +self
        else:
            _self = self
        if Meta.determine_meta(_self.coefficient[-1], 'ONE') or \
                _self.degree() == 0 and Meta.determine_meta(_self.coefficient[0], 'ZERO'):
            return _self
        else:
            for _i in range(_self.degree()):
                _self.coefficient[_i] /= _self.coefficient[-1]
            _self.coefficient[-1] = Meta.get_meta(self.coefficient[-1], 'ONE')
            return self

    def primitive(self, _new: bool = False):
        """
        *** this function is valid only when self.basic_data_type() is Fraction ! ***
        return a primitive polynomial with a same coefficient ratios of {self}.
        _new decides whether to return a new polynomial or applying change on {self}.
        :param _new: (bool)
        :return: (Polynomial) as above
        """
        assert self.basic_data_type().__name__ == 'Fraction'
        if _new:
            _self = +self
        else:
            _self = self
        _molecule_list = []
        _denominator_list = []
        for _i in _self.coefficient:
            _molecule_list.append(_i.molecule)
            _denominator_list.append(_i.denominator)
        _molecule = least_common_multiple_in_list(_denominator_list)
        _denominator = greatest_common_divisor_in_list(_molecule_list)
        _times = Fraction([_molecule, _denominator])
        for _i in range(_self.degree() + 1):
            _self.coefficient[_i] *= _times
        return _self

    def times(self, n, degree: int = 0, _new: bool = False):
        """
        a new polynomial whose value is self * (n)x**(degree)
        _new decides whether to return the new polynomial or applying change on {self}.
        :param n: (self.basic_data_type())
        :param degree: (int)
        :param _new: (bool)
        :return: (Polynomial) the new polynomial
        """
        assert degree >= 0
        _coefficient = [Meta.get_meta(self.coefficient[-1], 'ZERO') for _i in range(degree)]
        for _i in self.coefficient:
            _coefficient.append(_i * n)
        if _new:
            return Polynomial(_coefficient)
        else:
            self.coefficient = _coefficient
            return self

    def rational_roots(self):
        """
        *** this function is valid only when self.basic_data_type() is Fraction ! ***
        calc all rational roots in the corresponding polynomial function.
        :return: (list of Fraction) all rational roots
        """
        _self = (+self).primitive()
        if _self.degree() == 0:
            return []
        if _self.degree() == 1:
            return [-_self.coefficient[0] / _self.coefficient[1]]
        _molecule_list = factor(_self.coefficient[0].molecule)
        _denominator_list = factor(_self.coefficient[-1].molecule)
        _rational_roots = []
        for _molecule in _molecule_list:
            for _denominator in _denominator_list:
                _fraction = Fraction([_molecule, _denominator])
                if _self.value(_fraction).molecule == 0:
                    _rational_roots.append(_fraction)
                if _self.value(-_fraction).molecule == 0:
                    _rational_roots.append(-_fraction)
        return _rational_roots

    def formula(self):
        """
        :return: (string) the formula form string of the polynomial
        """
        _str = ''
        if hasattr(self.basic_data_type(), 'formula'):
            for _i in range(self.degree(), 0, -1):
                _str += self.coefficient[_i].formula() + 'x^' + str(_i) + '+'
            _str += self.coefficient[0].formula()
        else:
            for _i in range(self.degree(), 0, -1):
                _str += str(self.coefficient[_i]) + 'x^' + str(_i) + '+'
            _str += str(self.coefficient[0])
        return _str

    def is_irreducible_according_eisenstein(self):
        """
        *** this function is valid only when self.basic_data_type() is Fraction ! ***
        judge weather the polynomial is irreducible according eisenstein discriminant method.
        :return: (bool) True for irreducible, and False for unclear rather than reducible
        """
        _self = (+self).primitive()
        _part_coefficient_list = [_i.molecule for _i in _self.coefficient][:-1]
        _prime_list = prime_factor_without_exp(greatest_common_divisor_in_list(_part_coefficient_list))
        if _prime_list:
            for _prime in _prime_list:
                if _self.coefficient[-1].molecule % _prime and _self.coefficient[0].molecule % _prime ** 2:
                    return True
        return False


def greatest_common_divisor_in_polynomial(a: Polynomial, b: Polynomial):
    """
    this function can figure out the greatest common divisor between a and b.
    the result polynomial is monic.
    (this function wouldn't influence the origin value of a or b although it looks like dangerous!
    this characteristic is decided by python, i have no idea. ^_^)
    :param a: (Polynomial)
    :param b: (Polynomial)
    :return: (Polynomial)
    """
    assert a.basic_data_type().__name__ == b.basic_data_type().__name__
    while (a % b).degree():
        _mid = b
        b = a % b
        a = _mid
    return b.monic()


def greatest_common_divisor_with_coefficient_in_polynomial(a: Polynomial, b: Polynomial):
    """
    calc the greatest common divisor between a and b, and find two polynomials x, y to fit formula:
    a * x + b * y = the greatest common divisor.
    :param a: (Polynomial)
    :param b: (Polynomial)
    :return: (tuple) the greatest common divisor, x, y
    """
    assert a.basic_data_type().__name__ == b.basic_data_type().__name__
    if (a % b).degree() == 0:
        _y = Polynomial([Meta.get_meta(b.coefficient[-1], 'ONE') / b.coefficient[-1]])
        return b.monic(), Polynomial([Meta.get_meta(b.coefficient[-1], 'ZERO')]), _y
    else:
        __greatest_common_divisor, __x, __y = greatest_common_divisor_with_coefficient_in_polynomial(b, a % b)
        _x = __y
        _y = __x - (a // b) * _x
        return __greatest_common_divisor, _x, _y
