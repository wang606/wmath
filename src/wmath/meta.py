"""
Meta.py
this script is responsible for introducing Meta values.
"""


class Constant:
    """
    define a constant class.
    you can create your own constant container by just instantiate this class.
    for example: `a = Constant()`
    then you can add constants under it, such as `a.NAME = 'a'`
    after that, you can't change the value of a.NAME.
    """
    def __setattr__(self, key, value):
        if key in self.__dict__:
            _error = key + ' has been defined ! '
            raise PermissionError(_error)
        self.__dict__[key] = value

    def value_of(self, key: str):
        """
        designed for class, such as INT, FLOAT, COMPLEX and so on.
        you can define your own class's constant of course.
        :param key: (str)
        :return: self.__dict__[key]
        """
        return self.__dict__[key]

    def in_type(self, class_type: type):
        """
        designed for terms, such as ONE, ZERO and so on.
        you can define your own term's constant of course.
        :param class_type: (type)
        :return: self.__dict__[class_type.__name__]
        """
        return self.__dict__[class_type.__name__]


class Meta:
    """
    define Meta information in math.

    *** it's strongly discouraged to instantiate this class. Meta information is expected to be uniform. ***

    if you want to add constants under Meat,

    if you want to add another terms or classes under Meta, please use the Constant() instantiation.

    for example, if you want to add a MAX as a term, you should use the following statement:
    `Meta.MAX = Constant()`
    and then add its value in different class, such as:
    *** make sure the class name is correct ! ***
    `Meta.MAX.int = 999999999` (of course, it's just an example >_<)
    then you can use `Meta.MAX.in_type(int)` or just `Meta.MAX.int` to access this value.

    alternatively, you can also add your own class under the Meta class, such as:
    `Meta.YOUR_CLASS_NAME = Constant()`
    and then add its various values of different terms, such as:
    *** keep case consistent before and after ***
    `Meta.YOUR_CLASS_NAME.ZERO = YOUR_CLASS_NAME(0)`
    then you can use `Meta.YOUR_CLASS_NAME.value_of('ZERO')` or just `Meta.YOUR_CLASS_NAME.ZERO` to access this value.

    be careful !!!
    once the special value under your term or class is defined, it couldn't be modified,
    unless you instantiate a Constant() again.
    for example, you couldn't use `Meta.MAX.int = 100000000` after you had stated `Meta.MAX.int = 999999999`.
    but you could use `Meta.MAX = Constant()` to redefine the Meta.MAX, that would clear up all values of the old one.
    it's designed to protect the Meta information.
    """
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    CONST = Constant()
    CONST.PI = 3.141592653589793
    CONST.E = 2.718281828459045

    """
        classification by terms. 
    """
    ONE = Constant()
    ONE.int = 1
    ONE.float = 1.0
    ONE.complex = 1 + 0j

    ZERO = Constant()
    ZERO.int = 0
    ZERO.float = 0.0
    ZERO.complex = 0 + 0j

    """
        classification by class. 
    """
    int = Constant()
    int.ONE = 1
    int.ZERO = 0
    
    float = Constant()
    float.ONE = 1.0
    float.ZERO = 0.0
    
    complex = Constant()
    complex.ONE = 1 + 0j
    complex.ZERO = 0 + 0j


def discriminate(item, _term: str, _class: type = None):
    """
    if _class is not None:
        discriminate {item} is whether the '{_term}' in class {_class}.
    else:
        discriminate {item} is whether the '{_term}' in class {item} belongs to.
    *** pay attention! this function would check terms first. ***
    for example: Meta.ONE.int = 2 while Meta.int.ONE = 1 and item = 1,  _term = 'ONE', _class = int or None,
        then the result would be False, since Meta.ONE.int exists and is not equal to item.
    :param item: (any)
    :param _term: (str) specific term in some class, such as ONE, ZERO, MAX, so on
    :param _class: (type) if you want to specify a specific class, use this parameter
    :return: (bool) True for yes, False for no
    """
    if _class is not None:
        _class = _class.__name__
    else:
        _class = type(item).__name__
    if _term in Meta.__dict__ and _class in Meta.__dict__[_term].__dict__:
        if item == Meta.__dict__[_term].__dict__[_class]:
            return True
        else:
            return False
    if _class in Meta.__dict__ and _term in Meta.__dict__[_class].__dict__:
        if item == Meta.__dict__[_class].__dict__[_term]:
            return True
        else:
            return False
    _error = 'you had not define Meta.' + _term + '.' + type(item).__name__ \
             + ' or Meta.' + type(item).__name__ + '.' + _term + ' yet ! '
    raise KeyError(_error)
