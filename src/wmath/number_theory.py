"""
number_theory.py
this script is response for handling number theory problems in math.
"""
import math
import warnings


def is_prime(x: int):
    """
    judge weather x is a prime.
    if x <= 1, then return False.
    :param x: (int)
    :return: (bool) True if x is a prime, while False if not
    """
    if x == 2:
        return True
    if x & 1 == 0 or x <= 1:
        return False
    _is_prime = True
    _sqrt = int(math.sqrt(x)) + 1
    _i = 3
    while _i <= _sqrt:
        if x % _i == 0:
            _is_prime = False
            break
        _i += 2
    return _is_prime


def find_prime_until(x: int):
    """
    return all prime less than int x.
    :param x: (int)
    :return: (list) all prime less than int x
    """
    if x < 2:
        return []
    _prime = [2]
    _i = 3
    while _i <= x:
        _is_prime = True
        _sqrt = math.sqrt(_i)
        for _j in _prime:
            if _j > _sqrt:
                break
            if _i % _j == 0:
                _is_prime = False
                break
        if _is_prime:
            _prime.append(_i)
        _i += 2
    return _prime


def prime_factor_without_exp(x: int):
    """
    calc all prime factors of int x.
    if x is zero or one, then return [].
    if x < 0, then return the result of -x.
    :param x: (int)
    :return: (list) all prime factors of int x
    """
    x = abs(x)
    if x == 0 or x == 1:
        return []
    _list = []
    _prime = find_prime_until(int(math.sqrt(x)) + 1)
    for _i in _prime:
        if x % _i == 0:
            _list.append(_i)
            while x % _i == 0:
                x //= _i
    if x != 1:
        _list.append(x)
    return _list


def prime_factor_with_exp(x: int):
    """
    calc all prime factors and each exp of int x.
    if x is zero or one, then return {}.
    if x < 0, then return the result of -x.
    :param x: (int)
    :return: (dict) all prime factors as keys with each exp as value of int x
    """
    x = abs(x)
    if x == 0 or x == 1:
        return {}
    _dict = {}
    _sqrt = int(math.sqrt(x)) + 1
    _prime = find_prime_until(_sqrt)
    for _i in _prime:
        if x % _i == 0:
            _dict[_i] = 0
            while x % _i == 0:
                _dict[_i] += 1
                x //= _i
    if x != 1:
        _dict[x] = 1
    return _dict


def factor(x: int):
    """
    calc all factors of int x.
    if x is zero, then return [].
    if x < 0, then return the result of -x.
    :param x: (int)
    :return: (list) all factors of int x
    """
    x = abs(x)
    if x == 0:
        warnings.warn('the factors of 0 is unclear, return [] instead. ', UserWarning)
        return []
    if x == 1:
        return [1]

    def list_multiple(a: list, b: list):
        _list = []
        for _i in b:
            for _j in a:
                _list.append(_i * _j)
        return _list

    _prime_factor_with_exp = prime_factor_with_exp(x)
    _list2d = []
    for _prime in _prime_factor_with_exp:
        _list2d.append([_prime ** _i for _i in range(_prime_factor_with_exp[_prime] + 1)])
    while len(_list2d) != 1:
        _list2d[-2] = list_multiple(_list2d[-2], _list2d[-1])
        _list2d.pop()
    return _list2d[0]


def greatest_common_divisor(a: int, b: int):
    """
    calc the greatest common divisor between a and b.
    :param a: (int)
    :param b: (int)
    :return: (int) the greatest common divisor between a and b
    """
    if a == 0 and b == 0:
        warnings.warn('the greatest common divisor of 0 and 0 is unclear, return 0 instead. ', UserWarning)
        return 0
    if b == 0:
        return a
    while a % b != 0:
        _mid = b
        b = a % b
        a = _mid
    return b


def greatest_common_divisor_in_list(a: list):
    """
    calc the greatest common divisor among items in a.
    :param a: (list) integer
    :return: (int) the greatest common divisor
    """
    assert a
    if 1 in a:
        return 1
    while 0 in a:
        a.remove(0)
    if len(a) == 0:
        warnings.warn('the greatest common divisor of 0 and 0 is unclear, return 0 instead. ', UserWarning)
        return 0
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return greatest_common_divisor(a[0], a[1])
    _list = []
    for _i in range(len(a) // 2):
        _list.append(greatest_common_divisor(a[2 * _i], a[2 * _i + 1]))
    if len(a) % 2:
        _list.append(a[-1])
    return greatest_common_divisor_in_list(_list)


def least_common_multiple(a: int, b: int):
    """
    calc the least common multiple between a and b.
    :param a: (int)
    :param b: (int)
    :return: (int) the least common multiple between a and b
    """
    return a * b // greatest_common_divisor(a, b)


def least_common_multiple_in_list(a: list):
    """
    calc the least common multiple among items in a.
    :param a: (list) integer
    :return: (int) the least common multiple
    """
    assert a
    while 1 in a:
        a.remove(1)
    if len(a) == 0:
        return 1
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return least_common_multiple(a[0], a[1])
    _list = []
    for _i in range(len(a) // 2):
        _list.append(least_common_multiple(a[2 * _i], a[2 * _i + 1]))
    if len(a) % 2:
        _list.append(a[-1])
    return least_common_multiple_in_list(_list)


def greatest_common_divisor_with_coefficient(a: int, b: int):
    """
    calc the greatest common divisor between a and b, and find two numbers x, y to fit formula:
    a * x + b * y = the greatest common divisor.
    :param a: (int)
    :param b: (int)
    :return: (tuple) the greatest common divisor, x, y
    """
    if b == 0:
        return a, 1, 0
    else:
        __greatest_common_divisor, __x, __y = greatest_common_divisor_with_coefficient(b, a % b)
        _x = __y
        _y = __x - (a // b) * __y
        return __greatest_common_divisor, _x, _y


def inverse(a: int, n: int):
    """
    calc the inverse of a in the case of module n, where a and n must be mutually prime.
    a * x = 1 (mod n)
    :param a: (int)
    :param n: (int)
    :return: (int) x
    """
    assert greatest_common_divisor(a, n) == 1
    return greatest_common_divisor_with_coefficient(a, n)[1] % n
