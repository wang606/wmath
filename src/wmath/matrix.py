"""
matrix.py
this script is response for the problems related to matrix in the rational number field.
"""
import wmath
from wmath.fraction import Fraction, list2str


class Matrix:
    """
    define the class of matrix in the rational number field and related operations among them.
    """
    def __init__(self, kernel: list):
        assert kernel
        _kernel = []
        for _i in kernel:
            assert len(_i) == len(kernel[0])
            _list = []
            for _j in _i:
                assert type(_j).__name__ == 'Fraction'
                _list.append(_j)
            _kernel.append(_list)
        self.kernel = _kernel

    def __str__(self):
        _str = str(list2str(self.kernel)).replace('\'', '').replace('], [', ']\n [')
        return _str

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
        _kernel = []
        for _i in self.kernel:
            _list = []
            for _j in _i:
                _list.append(_j)
            _kernel.append(_list)
        return Matrix(_kernel)

    def __neg__(self):
        _kernel = []
        for _i in self.kernel:
            _list = []
            for _j in _i:
                _list.append(-_j)
            _kernel.append(_list)
        return Matrix(_kernel)

    def __add__(self, other):
        assert self.size() == other.size()
        _kernel = []
        for _i in range(self.size()[0]):
            _kernel.append([])
            for _j in range(self.size()[1]):
                _kernel[_i].append(self.kernel[_i][_j] + other.kernel[_i][_j])
        return Matrix(_kernel)
    
    def __sub__(self, other):
        assert self.size() == other.size()
        _kernel = []
        for _i in range(self.size()[0]):
            _kernel.append([])
            for _j in range(self.size()[1]):
                _kernel[_i].append(self.kernel[_i][_j] - other.kernel[_i][_j])
        return Matrix(_kernel)
    
    def __mul__(self, other):
        assert self.size()[1] == other.size()[0]
        _len = self.size()[1]
        _kernel = [[Fraction(0, 1) for _j in range(other.size()[1])] for _i in range(self.size()[0])]
        for _i in range(self.size()[0]):
            for _j in range(other.size()[1]):
                for _k in range(_len):
                    _kernel[_i][_j] += self.kernel[_i][_k] * other.kernel[_k][_j]
        return Matrix(_kernel)
    
    def size(self):
        """
        total number of rows and columns.
        :return: (tuple)
        """
        return len(self.kernel), len(self.kernel[0])

    def part(self, rows, cols):
        """
        return a new Matrix with values deep-copied from {self}, specified by {rows} and {cols}.
        if rows(cols) is a tuple like (a1, a2), that means from row(col) a1 to row(col) a2, with a2 not included.
        if rows(cols) is a list like [a1, a2, ...], that means row(col) a1, a2, ..., with everyone included.
        :param rows: (tuple or list of int)
        :param cols: (tuple or list of int)
        :return: (Matrix)
        """
        if type(rows) == tuple:
            rows = [_i for _i in range(rows)]
        if type(cols) == tuple:
            cols = [_i for _i in range(cols)]
        _kernel = []
        for _i in rows:
            _list = []
            for _j in cols:
                _list.append(self.kernel[_i][_j])
            _kernel.append(_list)
        return Matrix(_kernel)

    def determinant(self):
        """
        calc determinant of a square matrix.
        :return: (Fraction) determinant
        """
        return determinant_upper_triangle(self.kernel)


def determinant_upper_triangle(x: list):
    """
    calc determinant of x as a 2d Matrix by upper-triangle method.
    :param x: (list2d of Fraction)
    :return: (Fraction) determinant
    """

    # check x and deepcopy x to _kernel
    _kernel = []
    for _i in range(len(x)):
        assert len(x[_i]) == len(x)
        _kernel.append([])
        for _j in x[_i]:
            _kernel[_i].append(_j)

    _len = len(_kernel)
    _pos = True

    for _index in range(_len):

        # skip rows with a 'zero' beginning
        _row = _index
        while _row < _len and _kernel[_row][_index] == Fraction(0, 1):
            _row += 1
        if _row == _len:
            return Fraction(0, 1)

        # upper-triangle method
        for __row in range(_row + 1, _len):
            __times = _kernel[__row][_index] / _kernel[_row][_index]
            for __col in range(_index, _len):
                _kernel[__row][__col] -= __times * _kernel[_row][__col]

        # switch position if necessary
        if _row != _index:
            _list = _kernel[_index]
            _kernel[_index] = _kernel[_row]
            _kernel[_row] = _list
            _pos = not _pos

    # cumulative multiplication
    if _pos ^ (_len % 2):
        _determinant = Fraction(-1, 1)
    else:
        _determinant = Fraction(1, 1)
    for _index in range(_len):
        _determinant *= _kernel[_index][_index]

    return _determinant
