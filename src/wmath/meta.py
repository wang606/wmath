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


class Meta:
    """
    define Meta information in math.

    *** it's strongly discouraged to instantiate this class. Meta information is expected to be uniform. ***

    # basic information
    Meta use class Constant() as its middle nodes' type,
    and Meta's end node is usually a constant data or a lambda expression or a small function.
    the general structure of Meta usually looks like this:
    Meta:
        |- CONST:
            |- PI: (float) 3.141592653589793
            |- E: (float) 2.718281828459045
            |- ...
        |- GET:
            |- ONE:
                |- int: (lambda) x: 1
                |- float: (lambda) x: 1.0
                |- complex: (lambda) x: 1 + 0j
                |- ...
            |- ZERO:
                |- int: (lambda) x: 0
                |- float: (lambda) x: 0.0
                |- complex: (lambda) x: 0 + 0j
                |- ...
            |- ANY:
                |- ...
            |- ...
        |- DETERMINE:
            |- {introduced as below}

    as above, Meta has three basic elements: CONST, GET, DETERMINE.
    CONST is used to store consistent constant in math, such as PI, E.
    GET is used to define terms in different class/type/field, such as ONE, ZERO.
    DETERMINE is used to determine if a variant is the specific value/term in specific class/type/field
    *** it's discouraged to add another basic elements unless you know well. ***

    # CONST
    if you want to add your own consistent constants, use CONST please. the statement looks like this:
    `Meta.CONST.YOUR_CONSTANT_NAME = 348236` (348236 is just a example <_<)

    # GET
    if you want to add another terms or classes under Meta.GET, please use the Constant() instantiation.
    *** classification by terms is encouraged ! ***

        for example, if you want to add a MAX as a term, you should use the following statement:
        `Meta.GET.MAX = Constant()`
        and then add its value in different class/type/field, such as:
        *** make sure the class name is correct ! ***
        `Meta.GET.MAX.int = lambda x: 999999999` (of course, it's just an example >_<)
        then you can use function `get_meta(item, _term: str, _class: type = None)` to access this value.

        alternatively, you can classify things by class/type/field, though it's not encouraged, such as:
        `Meta.YOUR_CLASS_NAME = Constant()`
        and then add its various values of different terms, such as:
        *** keep case consistent before and after ***
        `Meta.GET.YOUR_CLASS_NAME.ZERO = lambda x: YOUR_CLASS_NAME(0, x)`

    # DETERMINE
    usually, this node is not your concern.
    but if you want to specify the behavior of function `determine_meta(item, _term: str, _class: type = None)`,
    where the param {_class} or the type of param {item} is your interest class/type/field,
    you can define the value of `Meta.DETERMINE.{{term}}.{{class/type/field}}` or
    `Meta.DETERMINE.{{class/type/field}}.{{term}}`, which is usually a small function.
    by default, the function `determine_meta(item, _term: str, _class: type = None)` would return whether {item}
    is equal to `get_meta(item, _term: str, _class: type = None)`.

        for example, in class Fraction, where Meta.GET.ONE.Fraction = lambda x: Fraction(1), determine_meta(
        Fraction(2), 'ONE') is False while determine_meta(Fraction(1), 'ONE') is True.

    be careful !!!
    once the special value under your term or class is defined, it couldn't be modified,
    unless you instantiate a Constant() again.
    for example, you couldn't use `Meta.GET.MAX.int = lambda x: 100000000` after
    you had stated `Meta.GET.MAX.int = lambda x: 999999999`.
    but you could use `Meta.GET.MAX = Constant()` to redefine the Meta.GET.MAX,
    that would clear up all values of the old one.

    it's designed to protect the Meta information.
    """
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    # the three basic elements
    CONST = Constant()
    GET = Constant()
    DETERMINE = Constant()

    # CONST
    CONST.PI = 3.141592653589793
    CONST.E = 2.718281828459045

    """
        classification by terms. more encouraged. 
    """
    # GET
    GET.ONE = Constant()
    GET.ZERO = Constant()
    GET.ANY = Constant()

    # DETERMINE
    DETERMINE.ONE = Constant()
    DETERMINE.ZERO = Constant()

    """
        classification by class. discouraged. 
    """
    '''
    GET.int = Constant()
    GET.int.ONE = 1
    GET.int.ZERO = 0
    
    GET.float = Constant()
    GET.float.ONE = 1.0
    GET.float.ZERO = 0.0
    
    GET.complex = Constant()
    GET.complex.ONE = 1 + 0j
    GET.complex.ZERO = 0 + 0j
    '''

    def get_meta(item: object, _term: str, _class: type = None):
        """
        get the meta information of {{_term}} in {{_class}} or type(item) if {{_class}} is None.
        *** pay attention! this function would check terms first. ***
        :param item: (any) parameter which would specify the class/type/field when _class is None
        :param _term: (str) specify the term
        :param _class: (type) specify the class/type/field
        :return: Meta.GET.{{_term}}.{{_class}}(item) or Meta.GET.{{_class}}.{{_term}}(item)
        """
        # _class
        if _class is not None:
            _class = _class.__name__
        else:
            _class = type(item).__name__
        # _term first
        if _term in Meta.GET.__dict__ and _class in Meta.GET.__dict__[_term].__dict__:
            return Meta.GET.__dict__[_term].__dict__[_class](item)
        # then _class
        if _class in Meta.GET.__dict__ and _term in Meta.GET.__dict__[_class].__dict__:
            return Meta.GET.__dict__[_class].__dict__[_term](item)
        _error = 'you have not defined Meta.GET.' + _term + '.' + _class + \
                 ' or Meta.GET.' + _class + '.' + _term + ' yet !'
        raise KeyError(_error)

    def determine_meta(item: object, _term: str, _class: type = None):
        """
        if _class is not None:
            determine if {item} is the '{_term}' in class {_class}.
        else:
            determine if {item} is the '{_term}' in class {item} belongs to.
        *** pay attention! this function would check terms first. ***
        for example: when Meta.GET.ONE.int(x) = 2 and Meta.GET.int.ONE(x) = 1, if the parameters is
            (item = 1,  _term = 'ONE', _class = int or None), the result would be False,
            since Meta.ONE.int() exists and is not equal to item.
        :param item: (any)
        :param _term: (str) specific term in class/type/field, such as ONE, ZERO, MAX, so on
        :param _class: (type) if you want to specify a specific class/type/field, use this parameter
        :return: (bool) True for yes, False for no
        """
        # _class
        if _class is not None:
            _class = _class.__name__
        else:
            _class = type(item).__name__
        # check specific DETERMINE method
        # _term first
        if _term in Meta.DETERMINE.__dict__ and _class in Meta.DETERMINE.__dict__[_term].__dict__:
            return Meta.DETERMINE.__dict__[_term].__dict__[_class](item)
        # then _class
        if _class in Meta.DETERMINE.__dict__ and _term in Meta.DETERMINE.__dict__[_class].__dict__:
            return Meta.DETERMINE.__dict__[_class].__dict__[_term](item)
        # try default method
        try:
            # _term first
            if _term in Meta.GET.__dict__ and _class in Meta.GET.__dict__[_term].__dict__:
                if item == Meta.GET.__dict__[_term].__dict__[_class](item):
                    return True
                else:
                    return False
            # then _class
            if _class in Meta.GET.__dict__ and _term in Meta.GET.__dict__[_class].__dict__:
                if item == Meta.GET.__dict__[_class].__dict__[_term](item):
                    return True
                else:
                    return False
            # if no Meta.GET.{{_term}}.{{_class}} or Meta.GET.{{_class}}.{{_term}} found
            _error = 'you have not defined Meta.GET.' + _term + '.' + _class \
                     + ' or Meta.GET.' + _class + '.' + _term + ' yet ! '
            raise KeyError(_error)
        # if Meta.GET.XXX exists, but can't be used to determine
        except ValueError:
            _error = 'the default determination method is invalid ! please define Meta.DETERMINE.' + _term + '.' + \
                     _class + ' or Meta.DETERMINE.' + _class + '.' + _term + ' specifically ! '
            raise ValueError(_error)
