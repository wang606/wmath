"""
fraction.py
this script is response for the operation in fraction.
"""
from wmath.number_theory import greatest_common_divisor


class Fraction:
    """
    define the class of fraction in math and operation among them.
    """
    def __init__(self, molecule: int, denominator: int):
        self.__dict__['__inited'] = False
        assert type(molecule) == int and type(denominator) == int
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
        return Fraction(self.denominator, self.molecule)

    def __pos__(self):
        return Fraction(self.molecule, self.denominator)

    def __neg__(self):
        return Fraction(-self.molecule, self.denominator)

    def __abs__(self):
        return Fraction(abs(self.molecule), abs(self.denominator))

    def __add__(self, other):
        _denominator = self.denominator * other.denominator
        _molecule = self.molecule * other.denominator + other.molecule * self.denominator
        return Fraction(_molecule, _denominator)

    def __sub__(self, other):
        _denominator = self.denominator * other.denominator
        _molecule = self.molecule * other.denominator - other.molecule * self.denominator
        return Fraction(_molecule, _denominator)

    def __mul__(self, other):
        _denominator = self.denominator * other.denominator
        _molecule = self.molecule * other.molecule
        return Fraction(_molecule, _denominator)

    def __truediv__(self, other):
        _denominator = self.denominator * other.molecule
        _molecule = self.molecule * other.denominator
        return Fraction(_molecule, _denominator)

    def __pow__(self, power: int, modulo=None):
        _denominator = pow(self.denominator, power)
        _molecule = 0
        if modulo:
            _molecule = pow(self.molecule, power, modulo * _denominator)
        else:
            _molecule = pow(self.molecule, power)
        return Fraction(_molecule, _denominator)

    def formula(self):
        """
        :return: (string) the formula form string of the fraction
        """
        if self.denominator == 1:
            return str(self.molecule)
        else:
            return '\\frac{' + str(self.molecule) + '}{' + str(self.denominator) + '}'


def number2fraction(x):
    """
    convert real number into fraction.
    :param x: (bool | int | float)
    :return: (Fraction) the fraction form of x
    """
    if type(x) == bool:
        if x:
            return Fraction(1, 1)
        else:
            return Fraction(0, 1)
    if type(x) == int:
        return Fraction(x, 1)
    else:
        assert type(x) == float
    _str = str(x)
    _molecule = 1
    _denominator = 1
    if 'e' in _str:
        _exp = int(_str.split('e')[-1])
        if _exp < 0:
            _denominator *= pow(10, -_exp)
        else:
            _molecule *= pow(10, _exp)
        _str = _str.split('e')[0]
    if '.' in _str:
        _molecule *= int(_str.split('.')[0] + _str.split('.')[-1])
        _denominator *= pow(10, len(_str.split('.')[-1]))
    return Fraction(int(_molecule), int(_denominator))


def str2fraction(x: str):
    """
    convert string like '2/3' or '3.3' or '4' into a fraction.
    :param x: (str)
    :return: (fraction)
    """
    if '/' in x:
        _str = x.split('/')
        _molecule = int(_str[0])
        _denominator = int(_str[1])
        return Fraction(_molecule, _denominator)
    else:
        return number2fraction(float(x))


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
        if type(_i) == list:
            _list.append(list2fraction(_i))
        elif type(_i) == Fraction:
            _list.append(_i)
        elif type(_i) == str:
            _list.append(str2fraction(_i))
        else:
            _list.append(number2fraction(_i))
    return _list


def list2str(x: list):
    """
    covert all items into strings in an any dimension list.
    it's very useful when you want to print a n dimension list while some items in it is pointers.
    :param x: (list)
    :return: (list of only strings)
    """
    _list = []
    for _i in x:
        if type(_i) == list:
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
        if type(_i) == list:
            _list.append(list2float(_i))
        elif type(_i) == Fraction:
            _list.append(float(_i))
        elif type(_i) == str:
            _list.append(float(str2fraction(_i)))
        else:
            _list.append(_i)
    return _list
