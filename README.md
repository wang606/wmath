# [TODO]
# introduce
'wmath' is a simple mathematical package designed by a bored undergraduate who wants to review math and python at the same time.
## features:
- <font color=#ff0000>wmath use a class called '**Meta**' to manage the global meta information, which is not allowed to be instantiated</font>
- <font color=#ff0000>wmath use class **Fraction** as one of its basic data types, since wmath mainly focus on rational operation</font> 
- <font color=#ff0000>param '**_new**' is a bool data, included in many methods in wmath, that decides whether to return a brand-new data or apply change on {self}</font>
## modules
wmath contains the following modules: 
- meta.py ------ manage the global meta information
- number_theory.py ------ handling number theory problems in math
- fraction.py ------ the operation in fraction
- polynomial.py ------ the related problems in polynomial
- matrix.py ------ the problems related to matrix in the rational number field
# reference
## meta.py
### Constant
```markdown
(class)
define a constant class.
you can create your own constant container by just instantiate this class.
for example: `a = Constant()`
then you can add constants under it, such as `a.NAME = 'a'`
after that, you can't change the value of a.NAME. 
    __setattr__(self, key, value)
```
- value_of(self, key: str)
```markdown
designed for class, such as int, float, complex and so on.
you can define your own class's constant of course.
    :param key: (str)
    :return: self.__dict__[key]
```
- in_type(self, class_type: type)
```markdown
designed for terms, such as ONE, ZERO and so on.
you can define your own term's constant of course.
    :param class_type: (type)
    :return: self.__dict__[class_type.__name__]
```
### <font color=#ff0000>Meta</font>
<font color=#ff0000>this part is very important !</font>
```markdown
(class)
define meta information in math.

    *** it's strongly discouraged to instantiate this class. meta information is expected to be uniform. ***

    if you want to add another terms or class under Meta, please use the Constant() instantiation.
    *** classification by terms is encouraged ! ***

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
    it's designed to protect the meta information.
        
    __setattr__(self, key, value)
```
- CONST
  - CONST.PI = 3.141592653589793
  - CONST.E = 2.718281828459045
- ONE
  - ONE.int = 1
  - ONE.float = 1.0
  - ONE.complex = 1 + 0j
- ZERO
  - ZERO.int = 0
  - ZERO.float = 0.0
  - ZERO.complex = 0 + 0j
### determine(item, _term: str, _class: type = None)
```markdown
if _class is not None:
    determine if {item} is the '{_term}' in class {_class}.
else:
    determine if {item} is the '{_term}' in class {item} belongs to.
*** pay attention! this function would check terms first. ***
for example: Meta.ONE.int = 2 while Meta.int.ONE = 1 and item = 1,  _term = 'ONE', _class = int or None,
then the result would be False, since Meta.ONE.int exists and is not equal to item.
    :param item: (any)
    :param _term: (str) specific term in some class, such as ONE, ZERO, MAX, so on
    :param _class: (type) if you want to specify a specific class, use this parameter
    :return: (bool) True for yes, False for no
```
## number_theory.py
### is_prime(x: int)
```markdown
(function)
judge weather x is a prime.
if x <= 1, then return False. 
    :param x: (int)
    :return: (bool) True if x is a prime, while False if not
```
### find_prime_until(x: int)
```markdown
(function)
return all prime less than int x.
    :param x: (int) x > 1
    :return: (list) all prime less than int x
```
### prime_factor_without_exp(x: int)
```markdown
(function)
calc all prime factors of int x.
if x is zero or one, then return [].
if x < 0, then return the result of -x.
    :param x: (int)
    :return: (list) all prime factors of int x
```
### prime_factor_with_exp(x: int)
```markdown
(function)
calc all prime factors and each exp of int x.
if x is zero or one, then return {}.
if x < 0, then return the result of -x. 
    :param x: (int) x > 0
    :return: (dict) all prime factors as keys with each exp as value of int x
```
### factor(x: int)
```markdown
calc all factors of int x.
if x is zero, then return [].
if x < 0, then return the result of -x.
    :param x: (int)
    :return: (list) all factors of int x
```
### greatest_common_divisor(a: int, b: int)
```markdown
(function)
calc the greatest common divisor between a and b.
    :param a: (int)
    :param b: (int)
    :return: (int) the greatest common divisor between a and b
```
### greatest_common_divisor_in_list(a: list)
```markdown
calc the greatest common divisor among items in a.
    :param a: (list) integer
    :return: (int) the greatest common divisor
```
### least_common_multiple(a: int, b: int)
```markdown
calc the least common multiple between a and b.
    :param a: (int)
    :param b: (int)
    :return: (int) the least common multiple between a and b
```
### least_common_multiple_in_list(a: list)
```markdown
calc the least common multiple among items in a.
    :param a: (list) integer
    :return: (int) the least common multiple
```
### greatest_common_divisor_with_coefficient(a: int, b: int)
```markdown
(function)
calc the greatest common divisor between a and b, and find two numbers x, y to fit formula:
a * x + b * y = the greatest common divisor.
    :param a: (int)
    :param b: (int)
    :return: (tuple) the greatest common divisor, x, y
```
### inverse(a: int, n: int)
```markdown
calc the inverse of a in the case of module n, where a and n must be mutually prime.
a * x = 1 (mod n)
    :param a: (int)
    :param n: (int)
    :return: (int) x
```
## fraction.py
### <font color=#ff0000>Fraction</font>
<font color=#ff0000>the basic data type of wmath. </font>
```markdown
(class)
define the class of fraction in math and operation among them.
    __init__(self, molecule: int, denominator: int)
    __getattr__(self, item)
    __setattr__(self, key, value)
    __str__(self)
    __float__(self)
    __eq__(self, other)
    __lt__(self, other)
    __le__(self, other)
    __invert__(self)
    __pos__(self)
    __neg__(self)
    __abs__(self)
    __add__(self, other)
    __sub__(self, other)
    __mul__(self, other)
    __truediv__(self, other)
    __pow__(self, power: int, modulo=None)
```
- formula(self)
```markdown
    :return: (string) the formula form string of the fraction 
```
### number2fraction(x)
```markdown
(function)
convert real number into fraction.
    :param x: (bool | int | float)
    :return: (Fraction) the fraction form of x
```
### str2fraction(x: str)
```markdown
(function)
convert string like '2/3' or '3.3' or '4' into a fraction.
    :param x: (str)
    :return: (fraction)
```
### list2fraction(x: list)
```markdown
(function)
convert list of real numbers or number strings into list of fractions.
it's allowed that list includes some fractions already.
such as: [1, '1/2', Fraction(2, 3), 4]
it's also allowed that list contains of child lists.
such as: [1, '1/2', Fraction(2, 3), [4, 5, 6.3], -0.9]
    :param x: (list of numbers or number strings or fractions or child lists)
    :return: (list of fractions)
```
### list2str(x: list)
```markdown
(function)
covert all items into strings in an any dimension list.
it's very useful when you want to print a n dimension list while some items in it is pointers.
    :param x: (list)
    :return: (list of only strings)
```
### list2float(x: list)
```markdown
covert all items into float in an any dimension list.
it's very useful when you want to convert fractions into float in a multiple dimension list.
    :param x: (list)
    :return: (list of only float)
```
## polynomial.py
### Polynomial
```markdown
(class)
define the class of polynomial and related operations among them.
    __init__(self, coefficient: list)
    __getattr__(self, item)
    __setattr__(self, key, value)
    __str__(self)
    __pos__(self)
    __neg__(self)
    __eq__(self)
    __add__(self, other)
    __sub__(self, other)
    __mul__(self, other)
    __truediv__(self, other)
    __floordiv__(self, other)
    __mod__(self, other)
    __pow__(self, power: int, modulo=None)
```
- value(self, x: Fraction)
```markdown
calc the value of the corresponding polynomial function where x is designated.
    :param x: (Fraction) independent variable
    :return: (Fraction) value
```
- adjust(self)
```markdown
manually adjust the polynomial after you changed the value 'in' the coefficient, 
while didn't fire the __setattr__() function since the coefficient is a pointer.
    :return: (Polynomial) self after adjust
```
- monic(self)
```markdown
return a monic polynomial with a same coefficient ratios of {self}. 
    :return: (Polynomial) as above
```
- primitive(self)
```markdown
return a primitive polynomial with a same coefficient ratios of {self}. 
    :return: (Polynomial) as above
```
- times(self, n: Fraction, degree: int = 0)
```markdown
a new polynomial whose value is self * (n)x**(degree)
    :param n: (Fraction)
    :param degree: (int)
    :return: (Polynomial) the new polynomial
```
- rational_roots(self)
```markdown
calc all rational roots in the corresponding polynomial function.
    :return: (list of Fraction) all rational roots
```
- formula(self)
```markdown
    :return: (string) the formula form string of the fraction
```
- is_irreducible_according_eisenstein(self):
```markdown
judge whether the polynomial is irreducible according eisenstein discriminant method.
    :return: (bool) True for irreducible, and False for unclear rather than reducible
```
### greatest_common_divisor_in_polynomial(a: Polynomial, b: Polynomial)
```markdown
this function can figure out the greatest common divisor between a and b.
the result polynomial is monic.
(this function wouldn't influence the origin value of a or b although it looks like dangerous!
this characteristic is decided by python, i have no idea. ^_^)
    :param a: (Polynomial)
    :param b: (Polynomial)
    :return: (Polynomial)
```
### greatest_common_divisor_with_coefficient_in_polynomial(a: Polynomial, b: Polynomial)
```markdown
calc the greatest common divisor between a and b, and find two polynomials x, y to fit formula:
a * x + b * y = the greatest common divisor.
    :param a: (Polynomial)
    :param b: (Polynomial)
    :return: (tuple) the greatest common divisor, x, y
```
## matrix.py
### Matrix
```markdown
(class)
define the class of matrix in the rational number field and related operations among them.
    __init__(self, kernel: list)
    __str__(self)
    __eq__(self, other)
    __pos__(self)
    __neg__(self)
    __add__(self)
    __sub__(self)
    __mul__(self)
```
- size(self)
```markdown
total number of rows and columns.
    :return: (tuple)
```
- part(self, rows, cols):
```markdown
return a new Matrix with values deep-copied from {self}, specified by {rows} and {cols}.
if rows(cols) is a tuple like (a1, a2), that means from row(col) a1 to row(col) a2, with a2 not included.
if rows(cols) is a list like [a1, a2, ...], that means row(col) a1, a2, ..., with everyone included.
    :param rows: (tuple or list of int)
    :param cols: (tuple or list of int)
    :return: (Matrix)
```
- determinant(self)
```markdown
calc determinant of a square matrix.
    :return: (Fraction) determinant
```
### 
determinant_upper_triangle(x: list)
```markdown
calc determinant of x as a 2d Matrix by upper-triangle method.
    :param x: (list2d of Fraction)
    :return: (Fraction) determinant
```
