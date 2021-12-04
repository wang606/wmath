"""
fraction.py
this script is response for the operation in fraction.
"""
from wmath.number_theory import greatest_common_divisor


class Fraction:
    """
    define the class of fraction in math and operation among them.
    """
    def __init__(self, x):
        """
        {x} accept bool, int, float, str and Fraction self type.
        for example : (True)=>1/1, (3)=>3/1, (9.3)=>93/10, ('2.0/3.6')=>5/9, (Fraction(2, 3))=>2/3
        when there are two params in {x}, which is a list or tuple,
        the first would be considered as molecule, and second as denominator.
        for example : (2, 3)=>2/3, [3.4, '3/2']=>17/75, ('4', True)=>4/1
        *** denominator can't be zero ! ***
        :param x: (bool | int | float | str | Fraction | tuple | list)
        """
        self.__dict__['__inited'] = False

        def _convert_to_fraction(_x):
            if type(_x).__name__ == 'Fraction':
                return _x.molecule, _x.denominator
            if type(_x).__name__ == 'int' or type(_x).__name__ == 'bool':
                return int(_x), 1
            _x = str(_x)
            if '/' in _x:
                _x = _x.split('/')
                _molecule_1, _denominator_1 = _convert_to_fraction(_x[0])
                _molecule_2, _denominator_2 = _convert_to_fraction(_x[1])
                _molecule, _denominator = _molecule_1 * _denominator_2, _molecule_2 * _denominator_1
                return _molecule, _denominator
            _molecule, _denominator = 1, 1
            if 'e' in _x:
                _exp = int(_x.split('e')[-1])
                if _exp < 0:
                    _denominator *= pow(10, -_exp)
                else:
                    _molecule *= pow(10, _exp)
                _x = _x.split('e')[0]
            if '.' in _x:
                _molecule *= int(_x.split('.')[0] + _x.split('.')[-1])
                _denominator *= pow(10, len(_x.split('.')[-1]))
            else:
                _molecule *= int(_x)
            return _molecule, _denominator

        _type = type(x).__name__
        if _type == 'tuple' or _type == 'list':
            molecule_1, denominator_1 = _convert_to_fraction(x[0])
            molecule_2, denominator_2 = _convert_to_fraction(x[1])
            molecule, denominator = molecule_1 * denominator_2, molecule_2 * denominator_1
        elif _type == 'bool' or _type == 'int' or _type == 'float' or _type == 'str' or _type == 'Fraction':
            molecule, denominator = _convert_to_fraction(x)
        else:
            _error = 'Fraction only accepts bool | int | float | str | Fraction | tuple | list type. '
            raise ValueError(_error)

        assert type(molecule).__name__ == 'int' and type(denominator).__name__ == 'int'
        assert denominator != 0

        _greatest_common_divisor = greatest_common_divisor(molecule, denominator)
        self.molecule = molecule // _greatest_common_divisor
        self.denominator = denominator // _greatest_common_divisor
        self.__dict__['__inited'] = True

    def __getattr__(self, item):
        raise AttributeError

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if self.__dict__['__inited']:
            # dynamically adjust the fraction
            _greatest_common_divisor = greatest_common_divisor(
                self.__dict__['molecule'],
                self.__dict__['denominator'])
            self.__dict__['molecule'] = self.__dict__['molecule'] // _greatest_common_divisor
            self.__dict__['denominator'] = self.__dict__['denominator'] // _greatest_common_divisor

    def __str__(self):
        if self.denominator == 1:
            return str(self.molecule)
        else:
            return str(self.molecule) + '/' + str(self.denominator)

    def __int__(self):
        if self.denominator == 1:
            return self.molecule // self.denominator
        else:
            _error = 'can\'t convert ' + str(self) + ' to an int type. '
            raise ValueError(_error)

    def __float__(self):
        return self.molecule / self.denominator

    def __eq__(self, other):
        return self.molecule == other.molecule and self.denominator == other.denominator

    def __lt__(self, other):
        return (self - other).molecule < 0

    def __le__(self, other):
        return self == other or self < other

    def __invert__(self):
        if self.molecule == 0:
            raise ZeroDivisionError
        return Fraction([self.denominator, self.molecule])

    def __pos__(self):
        return Fraction([self.molecule, self.denominator])

    def __neg__(self):
        return Fraction([-self.molecule, self.denominator])

    def __abs__(self):
        return Fraction([abs(self.molecule), abs(self.denominator)])

    def __add__(self, other):
        _denominator = self.denominator * other.denominator
        _molecule = self.molecule * other.denominator + other.molecule * self.denominator
        return Fraction([_molecule, _denominator])

    def __sub__(self, other):
        _denominator = self.denominator * other.denominator
        _molecule = self.molecule * other.denominator - other.molecule * self.denominator
        return Fraction([_molecule, _denominator])

    def __mul__(self, other):
        if type(other).__name__ != 'Fraction':
            other = Fraction(other)
        _denominator = self.denominator * other.denominator
        _molecule = self.molecule * other.molecule
        return Fraction([_molecule, _denominator])

    def __truediv__(self, other):
        if type(other).__name__ != 'Fraction':
            other = Fraction(other)
        _denominator = self.denominator * other.molecule
        _molecule = self.molecule * other.denominator
        return Fraction([_molecule, _denominator])

    def __pow__(self, power: int or float, modulo=None):
        _denominator = pow(self.denominator, power)
        _molecule = 0
        if modulo:
            _molecule = pow(self.molecule, power, modulo * _denominator)
        else:
            _molecule = pow(self.molecule, power)
        return Fraction([_molecule, _denominator])

    def conjugate(self):
        return +self

    def formula(self):
        """
        :return: (string) the formula form string of the fraction
        """
        if self.denominator == 1:
            return str(self.molecule)
        else:
            return '\\frac{' + str(self.molecule) + '}{' + str(self.denominator) + '}'


def list2fraction(x: list):
    """
    convert list of real numbers or number strings into list of fractions.
    it's allowed that list includes some fractions already.
    such as: [1, '1/2', Fraction(2, 3), 4]
    it's also allowed that list contains of child lists.
    such as: [1, '1/2', Fraction(2, 3), [4, 5, 6.3], -0.9]
    :param x: (list of numbers or number strings or fractions or child lists)
    :return: (list of fractions)
    """
    _list = []
    for _i in x:
        if type(_i).__name__ == 'list':
            _list.append(list2fraction(_i))
        else:
            _list.append(Fraction(_i))
    return _list


def list2str(x: list):
    """
    covert all items into strings in an any dimension list.
    it's very useful when you want to print an n dimension list while some items in it is pointers.
    :param x: (list)
    :return: (list of only strings)
    """
    _list = []
    for _i in x:
        if type(_i).__name__ == 'list':
            _list.append(list2str(_i))
        else:
            _list.append(str(_i))
    return _list


def list2float(x: list):
    """
    covert all items into float in an any dimension list.
    it's very useful when you want to convert fractions into float in a multiple dimension list.
    :param x: (list)
    :return: (list of only float)
    """
    _list = []
    for _i in x:
        if type(_i).__name__ == 'list':
            _list.append(list2float(_i))
        elif type(_i).__name__ == 'Fraction':
            _list.append(float(_i))
        elif type(_i).__name__ == 'str':
            _list.append(float(Fraction(_i)))
        else:
            _list.append(float(_i))
    return _list
