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
### Meta
```markdown
(class)
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
        
    __setattr__(self, key, value)
```
- CONST
  - CONST.PI = 3.141592653589793
  - CONST.E = 2.718281828459045
- GET
  - GET.ONE = Constant()
  - GET.ZERO = Constant()
  - GET.ANY = Constant()
- DETERMINE
- get_meta(item: object, _term: str, _class: type = None)
```markdown
(function)
get the meta information of {{_term}} in {{_class}} or type(item) if {{_class}} is None.
*** pay attention! this function would check terms first. ***
    :param item: (any) parameter which would specify the class/type/field when _class is None
    :param _term: (str) specify the term
    :param _class: (type) specify the class/type/field
    :return: Meta.GET.{{_term}}.{{_class}}(item) or Meta.GET.{{_class}}.{{_term}}(item)
```
- determine(item, _term: str, _class: type = None)
```markdown
(function)
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
(function)
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
(function)
calc the greatest common divisor among items in a.
    :param a: (list) integer
    :return: (int) the greatest common divisor
```
### least_common_multiple(a: int, b: int)
```markdown
(function)
calc the least common multiple between a and b.
    :param a: (int)
    :param b: (int)
    :return: (int) the least common multiple between a and b
```
### least_common_multiple_in_list(a: list)
```markdown
(function)
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
(function)
calc the inverse of a in the case of module n, where a and n must be mutually prime.
a * x = 1 (mod n)
    :param a: (int)
    :param n: (int)
    :return: (int) x
```
## fraction.py
### Fraction
```markdown
(class)
define the class of fraction in math and operation among them.
    __init__(self, molecule: int, denominator: int)
        {x} accept bool, int, float, str and Fraction self type.
        for example : (True)=>1/1, (3)=>3/1, (9.3)=>93/10, ('2.0/3.6')=>5/9, (Fraction(2, 3))=>2/3
        when there are two params in {x}, which is a list or tuple,
        the first would be considered as molecule, and second as denominator.
        for example : (2, 3)=>2/3, [3.4, '3/2']=>17/75, ('4', True)=>4/1
        *** denominator can't be zero ! ***
        :param x: (bool | int | float | str | Fraction | tuple | list)
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
- conjugate(self)
```markdown
(function)
    :return +self
```
- formula(self)
```markdown
(function)
    :return: (string) the formula form string of the fraction 
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
(function)
covert all items into float in an any dimension list.
it's very useful when you want to convert fractions into float in a multiple dimension list.
    :param x: (list)
    :return: (list of only float)
```
### list2complex(x: list)
```markdown
(function)
covert list of float into complex in an any dimension list.
it's very useful when you want to convert float into complex in eigenvalue algorithm.
    :param x: (list of float)
    :return: (list of only complex)
```
## paradigm.py
### Paradigm
```markdown
(class)
it's base for many class related to math.
    __init__(self)
```
- basic_data_type(self)
```markdown
(function)
```
- formula(self)
```markdown
(function)
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
- basic_data_type(self)
```markdown
(function)
basic data type of this Polynomial.
    :return: (type)
```
- degree(self)
```markdown
(function)
degree of this polynomial. 
    :return: (int)
```
- value(self, x)
```markdown
(function)
calc the value of the corresponding polynomial function where x is designated.
    :param x: (self.basic_data_type()) independent variable
    :return: (self.basic_data_type()) value
```
- conjugate(self, _new: bool = True)
```markdown
(function)
conjugate
    :param _new: (bool)
    :return: (Polynomial)
```
- derived(self, _new: bool = False)
```markdown
(function)
this function is valid only when self.basic_data_type support number multiplication.
derived polynomial of self.
    :param _new: (bool)
    :return: (Polynomial)
```
- integral(self, _new: bool = False)
```markdown
(function)
this function is valid only when self.basic_data_type support number multiplication.
integral of polynomial function, with zero as its constant coefficient.
    :param _new: (bool)
    :return: (Polynomial)
```
- monic(self, _new: bool = False)
```markdown
(function)
return a monic polynomial with a same coefficient ratios of {self}. 
_new decides whether to return a new polynomial or applying change on {self}.
    :param _new: (bool)
    :return: (Polynomial) as above
```
- primitive(self, _new: bool = False)
```markdown
(function)
*** this function is valid only when self.basic_data_type() is Fraction ! ***
return a primitive polynomial with a same coefficient ratios of {self}.
_new decides whether to return a new polynomial or applying change on {self}.
    :param _new: (bool)
    :return: (Polynomial) as above
```
- times(self, n, degree: int = 0, _new: bool = False)
```markdown
(function)
a new polynomial whose value is self * (n)x**(degree)
_new decides whether to return the new polynomial or applying change on {self}.
    :param n: (self.basic_data_type())
    :param degree: (int)
    :param _new: (bool)
    :return: (Polynomial) the new polynomial
```
- rational_roots(self)
```markdown
(function)
*** this function is valid only when self.basic_data_type() is Fraction ! ***
calc all rational roots in the corresponding polynomial function.
    :return: (list of Fraction) all rational roots
```
- real_roots(self, x_precision=1e-12, y_precision=None)
```markdown
(function)
this function is valid only when self.basic_data_type is float.
return all real roots.
    :param x_precision: (float)
    :param y_precision: (float)
    :return: (list of real number) real roots, with bigger further ahead
```
- formula(self)
```markdown
(function)
    :return: (string) the formula form string of the fraction
```
- is_irreducible_according_eisenstein(self):
```markdown
(function)
*** this function is valid only when self.basic_data_type() is Fraction ! ***
judge whether the polynomial is irreducible according eisenstein discriminant method.
    :return: (bool) True for irreducible, and False for unclear rather than reducible
```
### greatest_common_divisor_in_polynomial(a: Polynomial, b: Polynomial)
```markdown
(function)
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
(function)
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
define the class of matrix and related operations among them.
    __init__(self, kernel: list)
    __str__(self)
    __invert__(self)
    __eq__(self, other)
    __pos__(self)
    __neg__(self)
    __add__(self)
    __sub__(self)
    __mul__(self)
    __truediv__(self, other)
```
- basic_data_type(self)
```markdown
(function)
basic data type of this matrix. 
    :return: (type)
```
- formula(self)
```markdown
(function)
    :return: (string) the formula form string of the matrix
```
- size(self)
```markdown
(function)
total number of rows and columns.
    :return: (tuple)
```
- horizontal_split(self)
```markdown
(function)
return a list of Matrix which is horizontally split from self. 
    :return: (list of Matrix)
```
- vertical_spilt(self)
```markdown
(function)
return a list of Matrix which is vertically split from self. 
    :return: (list of Matrix)
```
- part(self, rows, cols):
```markdown
(function)
return a new Matrix with values deep-copied from {self}, specified by {rows} and {cols}.
_rows(_cols) accept range (_from, _to, _step) or list [a1, a2, ...] type.
    :param rows: (tuple or list of int)
    :param cols: (tuple or list of int)
    :return: (Matrix)
```
- fill(self, _rows, _cols, other, _new=False)
```markdown
(function)
fill specific part of {self} with corresponding values in {other}.
the part is specified by {_rows} and {_cols}.
the size of {other} must be bigger than or equal to (len(_rows), len(_cols)).
    :param _rows: (range or list of int)
    :param _cols:(range or list of int)
    :param _new: (bool) (bool) True for a new matrix, False for no
    :param other: (Matrix or list2d or tuple with the same basic_data_type of self)
    :return: (Matrix) if _new: a new matrix, else: self after filling
```
- times(self, _times, _new: bool = False, _rows=None, _cols=None)
```markdown
(function)
multiply each fraction in {self} by _times.
if _rows(_cols) is not None, it would only multiply the specific rows(cols).
_rows(_cols) accept range (_from, _to, _step) or list [a1, a2, ...] type.
_new decides whether to return a new matrix or applying change on {self}.
    :param _times: (self.basic_data_type()) times
    :param _new: (bool) True for a new matrix, False for no
    :param _rows: (range or list of int) keep None if you want to change all rows
    :param _cols: (range or list of int) keep None if you want to change all cols
    :return: (Matrix) if _new: a new matrix, else: self after multiplication
```
- transpose(self, _new: bool = False)
```markdown
(function)
transpose
_new decides whether to return a new matrix or applying change on {self}.
    :param _new: (bool)
    :return: (Matrix) if _new: a new matrix, else: self after transpose
```
- conjugate(self, _new: bool = True)
```markdown
(function)
conjugate
    :param _new: (bool)
    :return: (Matrix) if _new: a new matrix, else: self after conjugate
```
- stepped(self, standardized: bool = False, simplified: bool = False, _new: bool = False, _neg_needed: bool = False, _independent_cols_needed: bool = False)
```markdown
(function)
turn any matrix into stepped or standardized stepped or simplified stepped matrix.
    :param simplified: (bool)
    :param standardized: (bool)
    :param _new: (bool)
    :param _neg_needed: (bool)
    :param _independent_cols_needed: (bool)
    :return: (Matrix) if _new: a new matrix, else: self after stepped or standardized stepped or simplified stepped.
            (multi) Matrix as above, [_neg: (bool) if _neg_needed], [_independent_cols: (list) if _independent_cols_needed]
```
- trace(self)
```markdown
(function)
trace of matrix.
    :return: (self.basic_data_type())
```
- rank(self)
```markdown
(function)
rank of matrix.
    :return: (int) rank
```
- determinant_upper_triangle(self)
```markdown
(function)
calc determinant of a square matrix with upper triangle method.
    :return: (Fraction) determinant
```
- determinant_definition(self)
```markdown
(function)
calc determinant of a square matrix according to the definition of determinant.
it runs much slower than determinant_upper_triangle(). but it's very useful when upper triangle is invalid, such
as Matrix(Polynomial) since Polynomial's truediv return two arguments rather than one.
    :return: (Fraction) determinant
```
- inverse(self, _new: bool = False)
```markdown
(function)
inverse
_new decides whether to return a new matrix or applying change on {self}.
    :param _new: (bool)
    :return: (Matrix) if _new: a new matrix, else: self after inverse
```
- accompany(self)
```markdown
(function)
accompany matrix
    :return: (Matrix) if _new: a new matrix, else: self after turning to its accompany matrix
```
- qr_schmidt_decomposition(self, _column_linearly_independent: bool = False)
```markdown
(function)
QR decomposition of matrix.
    :return: (Matrix, Matrix) Q, R
```
- qr_householder_decomposition(self, _unitary_need: bool = False)
```markdown
(function)
qr decomposition of matrix using householder method.
matrix must be square.
    :param _unitary_need: (bool)
    :return: ([Matrix, ]Matrix) [Q, ]R
```
- qr_givens_decomposition(self, _unitary_need: bool = True)
```markdown
(function)
qr decomposition of matrix using givens method.
matrix must be square.
    :param _unitary_need: (bool)
    :return: ([Matrix, ]Matrix) [Q, ]R
```
- upper_hessenburg(self, _new: bool = False, _unitary_need: bool = False)
```markdown
(function)
make the matrix upper hessenburg.
unitary * self * (unitary^T.conjugate()) is a hessenburg matrix.
    :param _new: (bool)
    :param _unitary_need: (bool)
    :return: (Matrix or Matrix, Matrix)
```
- eigenvalue(self)
```markdown
(function)
eigenvalue of self with double shifts method.
the basic data type of self must be complex unless all eigenvalue is real numbers.
    :return: (list) eigenvalues
```
### matrix_zero(_row: int, _col: int, _filled)
```markdown
(function)
return a matrix filled with {_filled}, with a size (_row, _col).
    :param _row: (int)
    :param _col: (int)
    :param _filled: (any)
    :return: (Matrix)
```
### matrix_one(_row: int, _col: int, _value)
```markdown
(function)
return a 'E' matrix with {_value} on the diagonal, with a size (_row, _col).
    :param _row: (int)
    :param _col: (int)
    :param _value: (any)
    :return: (Matrix)
```
### matrix_horizontal_stack(a: Matrix, b: Matrix)
```markdown
(function)
stack two matrices horizontally. 
    :param a: (Matrix)
    :param b: (Matrix)
    :return: (Matrix)
```
### matrix_vertical_stack(a: Matrix, b:  Matrix)
```markdown
(function)
stacking two matrices vertically. 
    :param a: (Matrix)
    :param b: (Matrix)
    :return: (Matrix)
```
### homogeneous_linear_equations(a: Matrix)
```markdown
(function)
figure out the fundamental system of solutions of homogeneous linear equations: a * X = Matrix(zero).
    :param a: (Matrix) as above
    :return: (list of Matrix) fundamental system of solutions
```
### non_homogeneous_linear_equations(a: Matrix, b: Matrix)
```markdown
(function)
figure out the fundamental system of solutions and one special solution of non homogeneous linear equations:
a * X = b.
good news ! argument {b} could be a multi-columns matrix, which means this function can solve multiple equations at
the same time.
    :param a: (Matrix) as above
    :param b: (Matrix) as above
    :return: (list of fundamental solutions, list of special solutions)
```
## cross.py
### polynomial_roots(_poly: Polynomial)
```markdown
(function)
return all complex roots of _poly !
    :param _poly: (Polynomial)
    :return: (list) roots
```
