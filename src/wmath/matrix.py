"""
matrix.py
this script is response for the problems related to matrix in the rational number field.
"""
from wmath.meta import Meta
from wmath.paradigm import Paradigm
from wmath.fraction import list2str
from copy import deepcopy


class Matrix(Paradigm):
    """
    define the class of matrix in the rational number field and related operations among them.
    """
    def __init__(self, kernel: list):
        super().__init__()
        assert kernel
        _type = type(kernel[-1][-1]).__name__
        _kernel = []
        for _i in kernel:
            assert len(_i) == len(kernel[0])
            _list = []
            for _j in _i:
                assert type(_j).__name__ == _type
                _list.append(_j)
            _kernel.append(_list)
        self.kernel = _kernel

    def __str__(self):
        _str = str(list2str(self.kernel)).replace('\'', '').replace('], [', ']\n [')
        return _str

    def __invert__(self):
        return self.inverse(_new=True)

    def __eq__(self, other):
        if self.kernel == other.kernel:
            return True
        if self.size() != other.size():
            return False
        for _i in range(self.size()[0]):
            if self.kernel[_i] == other.kernel[_i]:
                continue
            for _j in range(self.size()[1]):
                if self.kernel[_i][_j] != other.kernel[_i][_j]:
                    return False
        return True

    def __pos__(self):
        return deepcopy(self)

    def __neg__(self):
        _kernel = []
        for _i in self.kernel:
            _list = []
            for _j in _i:
                _list.append(-_j)
            _kernel.append(_list)
        return Matrix(_kernel)

    def __add__(self, other):
        assert self.basic_data_type().__name__ == other.basic_data_type().__name__
        assert self.size() == other.size()
        _kernel = []
        for _i in range(self.size()[0]):
            _kernel.append([])
            for _j in range(self.size()[1]):
                _kernel[_i].append(self.kernel[_i][_j] + other.kernel[_i][_j])
        return Matrix(_kernel)
    
    def __sub__(self, other):
        assert self.basic_data_type().__name__ == other.basic_data_type().__name__
        assert self.size() == other.size()
        _kernel = []
        for _i in range(self.size()[0]):
            _kernel.append([])
            for _j in range(self.size()[1]):
                _kernel[_i].append(self.kernel[_i][_j] - other.kernel[_i][_j])
        return Matrix(_kernel)
    
    def __mul__(self, other):
        assert self.basic_data_type().__name__ == other.basic_data_type().__name__
        assert self.size()[1] == other.size()[0]
        _len = self.size()[1]
        _kernel = [[Meta.get_meta(self.kernel[-1][-1], 'ZERO')
                    for _j in range(other.size()[1])]
                   for _i in range(self.size()[0])]
        for _i in range(self.size()[0]):
            for _j in range(other.size()[1]):
                for _k in range(_len):
                    _kernel[_i][_j] += self.kernel[_i][_k] * other.kernel[_k][_j]
        return Matrix(_kernel)

    def basic_data_type(self):
        return type(self.kernel[-1][-1])

    def formula(self):
        """
        :return: (string) the formula form string of the matrix
        """
        _str = '\\begin{pmatrix}\n'
        if hasattr(type(self.kernel[-1][-1]), 'formula'):
            for _i in range(self.size()[0]):
                for _j in range(self.size()[1]):
                    _str += '{' + self.kernel[_i][_j].formula() + '}&'
                _str += '\\\\\n'
        else:
            for _i in range(self.size()[0]):
                for _j in range(self.size()[1]):
                    _str += '{' + str(self.kernel[_i][_j]) + '}&'
                _str += '\\\\\n'
        _str += '\\end{pmatrix}'
        return _str

    def size(self):
        """
        total number of rows and columns.
        :return: (tuple)
        """
        return len(self.kernel), len(self.kernel[0])

    def part(self, _rows, _cols):
        """
        return a new Matrix with values deep-copied from {self}, specified by {rows} and {cols}.
        _rows(_cols) accept range (_from, _to, _step) or list [a1, a2, ...] type.
        :param _rows: (range or list of int)
        :param _cols: (range or list of int)
        :return: (Matrix)
        """
        _kernel = []
        for _i in _rows:
            _list = []
            for _j in _cols:
                _list.append(deepcopy(self.kernel[_i][_j]))
            _kernel.append(_list)
        return Matrix(_kernel)

    def times(self, _times, _new: bool = False, _rows=None, _cols=None):
        """
        multiply each fraction in {self} by _times.
        if _rows(_cols) is not None, it would only multiply the specific rows(cols).
        _rows(_cols) accept range (_from, _to, _step) or list [a1, a2, ...] type.
        _new decides whether to return a new matrix or applying change on {self}.
        :param _times: (self.basic_data_type()) times
        :param _new: (bool) True for a new matrix, False for no
        :param _rows: (range or list of int) keep None if you want to change all rows
        :param _cols: (range or list of int) keep None if you want to change all cols
        :return: (Matrix) if _new: a new matrix, else: self after multiplication
        """
        if _new:
            _self = +self
        else:
            _self = self
        if _rows is None:
            _rows = range(_self.size()[0])
        if _cols is None:
            _cols = range(_self.size()[1])
        for _i in _rows:
            for _j in _cols:
                _self.kernel[_i][_j] *= _times
        return _self

    def transpose(self, _new: bool = False):
        """
        transpose
        _new decides whether to return a new matrix or applying change on {self}.
        :param _new: (bool)
        :return: (Matrix) if _new: a new matrix, else: self after transpose
        """
        _kernel = []
        for _i in range(self.size()[1]):
            _kernel.append([])
            for _j in range(self.size()[0]):
                _kernel[_i].append(deepcopy(self.kernel[_j][_i]))
        if _new:
            return Matrix(_kernel)
        else:
            self.kernel = _kernel
            return self

    def determinant(self):
        """
        calc determinant of a square matrix.
        :return: (Fraction) determinant
        """
        return determinant_upper_triangle(self.kernel)

    def inverse(self, _new: bool = False):
        """
        inverse
        _new decides whether to return a new matrix or applying change on {self}.
        :param _new: (bool)
        :return: (Matrix) if _new: a new matrix, else: self after inverse
        """
        _kernel = inverse_in_matrix(self.kernel)
        if _kernel is None:
            return None
        if _new:
            return Matrix(_kernel)
        else:
            self.kernel = _kernel
            return self

    def accompany(self, _new: bool = False):
        """[TODO]
        accompany matrix
        :param _new: (bool)
        :return: (Matrix) if _new: a new matrix, else: self after turning to its accompany matrix
        """
        _kernel = inverse_in_matrix(self.kernel)
        if _kernel is not None:
            _determinant = determinant_upper_triangle(self.kernel)
            return Matrix(_kernel).times(_determinant)
        pass


def matrix_zero(_row: int, _col: int, _filled):
    """
    return a matrix filled with {_filled}, with a size (_row, _col).
    :param _row: (int)
    :param _col: (int)
    :param _filled: (any)
    :return: (Matrix)
    """
    _kernel = [[_filled for _j in range(_col)] for _i in range(_row)]
    return Matrix(_kernel)


def matrix_one(_row: int, _col: int, _value):
    """
    return a 'E' matrix with {_value} on the diagonal, with a size (_row, _col).
    :param _row: (int)
    :param _col: (int)
    :param _value: (any)
    :return: (Matrix)
    """
    _kernel = [[Meta.get_meta(_value, 'ZERO') for _j in range(_col)] for _i in range(_row)]
    for _i in range(min(_row, _col)):
        _kernel[_i][_i] = _value
    return Matrix(_kernel)


def determinant_upper_triangle(x: list):
    """
    calc determinant of x as a 2d Matrix by upper-triangle method.
    :param x: (list2d)
    :return: (type(x[-1][-1])) determinant
    """

    # check x and deepcopy x to _kernel
    _kernel = []
    for _i in range(len(x)):
        assert len(x[_i]) == len(x)
        _kernel.append([])
        for _j in x[_i]:
            _kernel[_i].append(deepcopy(_j))

    _len = len(_kernel)
    _neg = False

    for _index in range(_len):

        # skip rows with a 'zero' beginning
        _row = _index
        while _row < _len and Meta.determine_meta(_kernel[_row][_index], 'ZERO'):
            _row += 1
        if _row == _len:
            return Meta.get_meta(_kernel[-1][-1], 'ZERO')

        # upper-triangle method
        for __row in range(_row + 1, _len):
            __times = _kernel[__row][_index] / _kernel[_row][_index]
            for __col in range(_index + 1, _len):
                _kernel[__row][__col] -= __times * _kernel[_row][__col]

        # switch position if necessary
        if _row != _index:
            _list = _kernel[_index]
            _kernel[_index] = _kernel[_row]
            _kernel[_row] = _list
            _neg = not _neg

    # cumulative multiplication
    if _neg ^ (_len % 2):
        _determinant = -Meta.get_meta(_kernel[-1][-1], 'ONE')
    else:
        _determinant = Meta.get_meta(_kernel[-1][-1], 'ONE')
    for _index in range(_len):
        _determinant *= _kernel[_index][_index]

    return _determinant


def inverse_in_matrix(x: list):
    """
    calc inverse of x as a 2d Matrix by expanded-matrix method.
    :param x: (list2d)
    :return: (type(x[-1][-1])) inverse of origin matrix
    """

    # check x and deepcopy x to _kernel
    _kernel = []
    for _i in range(len(x)):
        assert len(x[_i]) == len(x)
        _kernel.append([])
        for _j in x[_i]:
            _kernel[_i].append(deepcopy(_j))
    _len = len(_kernel)

    # create _inverse as result
    _inverse = [[Meta.get_meta(_kernel[-1][-1], 'ZERO') for _j in range(_len)] for _i in range(_len)]
    for _i in range(_len):
        _inverse[_i][_i] = Meta.get_meta(_kernel[-1][-1], 'ONE')

    # upper triangle
    for _index in range(_len):

        # skip rows with a 'zero' beginning
        _row = _index
        while _row < _len and Meta.determine_meta(_kernel[_row][_index], 'ZERO'):
            _row += 1
        if _row == _len:
            return None

        for __row in range(_row + 1, _len):
            __times = _kernel[__row][_index] / _kernel[_row][_index]
            for __col in range(_index + 1, _len):
                _kernel[__row][__col] -= __times * _kernel[_row][__col]
            for __col in range(_len):
                _inverse[__row][__col] -= __times * _inverse[_row][__col]

        # switch position if necessary
        if _row != _index:
            _list = _kernel[_index]
            _kernel[_index] = _kernel[_row]
            _kernel[_row] = _list
            _list = _inverse[_index]
            _inverse[_index] = _inverse[_row]
            _inverse[_row] = _list

    # lower triangle
    for _index in range(_len - 1, -1, -1):
        for _row in range(_index):
            _times = _kernel[_row][_index] / _kernel[_index][_index]
            for _col in range(_len):
                _inverse[_row][_col] -= _times * _inverse[_index][_col]
        for _col in range(_len):
            _inverse[_index][_col] /= _kernel[_index][_index]

    return _inverse
