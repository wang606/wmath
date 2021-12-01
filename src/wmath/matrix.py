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
    define the class of matrix and related operations among them.
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

    def __truediv__(self, other):
        assert self.basic_data_type().__name__ == other.basic_data_type().__name__
        assert self.size() == other.size()
        assert self.size()[0] == self.size()[1]
        return self * other.inverse(_new=True)

    def basic_data_type(self):
        """
        basic data type of this matrix.
        :return: (type)
        """
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

    def fill(self, _rows, _cols, other, _new=False):
        """
        fill specific part of {self} with corresponding values in {other}.
        the part is specified by {_rows} and {_cols}.
        the size of {other} must be bigger than or equal to (len(_rows), len(_cols)).
        :param _rows: (range or list of int)
        :param _cols:(range or list of int)
        :param _new: (bool) (bool) True for a new matrix, False for no
        :param other: (Matrix or list2d or tuple with the same basic_data_type of self)
        :return: (Matrix) if _new: a new matrix, else: self after filling
        """
        if _new:
            _self = +self
        else:
            _self = self
        if type(other).__name__ == 'Matrix':
            other = other.kernel
        __row, __col = 0, 0
        for _i in _rows:
            for _j in _cols:
                _self.kernel[_i][_j] = other[__row][__col]
                __col += 1
            __col = 0
            __row += 1
        return _self

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

    def stepped(self, standardized: bool = False, simplified: bool = False, _new: bool = False,
                _neg_needed: bool = False, _dependent_cols_needed: bool = False):
        """
        turn any matrix into stepped or standardized stepped or simplified stepped matrix.
        :param simplified: (bool)
        :param standardized: (bool)
        :param _new: (bool)
        :param _neg_needed: (bool)
        :param _dependent_cols_needed: (bool)
        :return: (Matrix) if _new: a new matrix, else: self after stepped or standardized stepped or simplified stepped.
            (multi) Matrix as above, [_neg: (bool) if _neg_needed], [_dependent_cols: (list) if _dependent_cols_needed]
        """
        if _new:
            _self = +self
        else:
            _self = self

        # dependent_cols and neg
        dependent_cols = []
        _row, _col = 0, 0
        _neg = False
        while _row < _self.size()[0] and _col < _self.size()[1]:

            # skip rows with a 'zero' beginning
            __row = _row
            while __row < _self.size()[0] and Meta.determine_meta(_self.kernel[__row][_col], 'ZERO'):
                __row += 1
            if __row == _self.size()[0]:
                _col += 1
                continue
            dependent_cols.append(_col)

            # upper-triangle method
            for ___row in range(__row + 1, _self.size()[0]):
                ___times = _self.kernel[___row][_col] / _self.kernel[__row][_col]
                _self.kernel[___row][_col] = Meta.get_meta(_self.kernel[___row][_col], 'ZERO')
                for ___col in range(_col + 1, _self.size()[1]):
                    _self.kernel[___row][___col] -= ___times * _self.kernel[__row][___col]

            # switch position if necessary
            if __row != _row:
                _list = _self.kernel[_row]
                _self.kernel[_row] = _self.kernel[__row]
                _self.kernel[__row] = _list
                _neg = not _neg

            _col += 1
            _row += 1

        # simplified
        if simplified:

            # independent_cols
            independent_cols = []
            for _i in range(_self.size()[1]):
                if _i not in dependent_cols:
                    independent_cols.append(_i)

            for _i in range(len(dependent_cols) - 1, -1, -1):
                for __row in range(_i):
                    __times = _self.kernel[__row][dependent_cols[_i]] / _self.kernel[_i][dependent_cols[_i]]
                    for __col in independent_cols:
                        if __col > dependent_cols[_i]:
                            _self.kernel[__row][__col] -= __times * _self.kernel[_i][__col]
                    _self.kernel[__row][dependent_cols[_i]] = Meta.get_meta(_self.kernel[-1][-1], 'ZERO')
                for __col in independent_cols:
                    if __col > dependent_cols[_i]:
                        _self.kernel[_i][__col] /= _self.kernel[_i][dependent_cols[_i]]
                _self.kernel[_i][dependent_cols[_i]] = Meta.get_meta(_self.kernel[-1][-1], 'ONE')
        else:

            # standardized
            if standardized:
                for _i in range(len(dependent_cols) - 1, -1, -1):
                    for __col in range(dependent_cols[_i] + 1, _self.size()[1]):
                        _self.kernel[_i][__col] /= _self.kernel[_i][dependent_cols[_i]]
                    _self.kernel[_i][dependent_cols[_i]] = Meta.get_meta(_self.kernel[-1][-1], 'ONE')

        if _neg_needed and _dependent_cols_needed:
            return _self, _neg, dependent_cols
        elif _neg_needed and ~_dependent_cols_needed:
            return _self, _neg
        elif ~_neg_needed and _dependent_cols_needed:
            return _self, dependent_cols
        else:
            return _self

    def rank(self):
        """
        rank of matrix.
        :return: (int) rank
        """
        _, dependent_cols = self.stepped(_new=True, _dependent_cols_needed=True)
        return len(dependent_cols)

    def determinant(self):
        """
        calc determinant of a square matrix.
        :return: (Fraction) determinant
        """
        assert self.size()[0] == self.size()[1]
        _self, _neg, _dependent_cols = self.stepped(_new=True, _neg_needed=True, _dependent_cols_needed=True)
        if len(_dependent_cols) < _self.size()[0]:
            return Meta.get_meta(_self.kernel[-1][-1], 'ZERO')
        if _neg ^ (_self.size()[0] % 2):
            _determinant = -Meta.get_meta(_self.kernel[-1][-1], 'ONE')
        else:
            _determinant = Meta.get_meta(_self.kernel[-1][-1], 'ONE')
        for _index in _dependent_cols:
            _determinant *= _self.kernel[_index][_index]
        return _determinant

    def inverse(self, _new: bool = False):
        """
        inverse
        _new decides whether to return a new matrix or applying change on {self}.
        :param _new: (bool)
        :return: (Matrix) if _new: a new matrix, else: self after inverse
        """
        assert self.size()[0] == self.size()[1]
        _kernel = (+self).kernel
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

        if _new:
            return Matrix(_inverse)
        else:
            self.kernel = _inverse
            return self

    def accompany(self):
        """
        accompany matrix
        :return: (Matrix) if _new: a new matrix, else: self after turning to its accompany matrix
        """
        assert self.size()[0] == self.size()[1]
        _inverse = self.inverse(_new=True)
        if _inverse is not None:
            _determinant = self.determinant()
            return _inverse.times(_determinant)
        if self.rank() < self.size()[0] - 1:
            return matrix_zero(self.size()[0], self.size()[1], Meta.get_meta(self.kernel[-1][-1], 'ZERO'))
        _kernel = []
        for _i in range(self.size()[0]):
            _kernel.append([])
            for _j in range(self.size()[1]):
                _i_list = [__i for __i in range(self.size()[0]) if __i != _i]
                _j_list = [__j for __j in range(self.size()[0]) if __j != _j]
                _kernel[_i].append(self.part(_i_list, _j_list).determinant())
        return Matrix(_kernel)


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


def matrix_horizontal_stack(matrices: list):
    """
    stack matrices horizontally.
    :param matrices: (list of Matrix)
    :return: (Matrix)
    """
    assert matrices
    for _i in range(1, len(matrices)):
        assert matrices[_i].basic_data_type() == matrices[0].basic_data_type()
        assert matrices[_i].size()[0] == matrices[0].size()[0]
    _matrices = deepcopy(matrices)
    _kernel = []
    for _i in range(_matrices[0].size()[0]):
        _kernel.append([])
        for _j in range(len(_matrices)):
            for _k in range(_matrices[_j].size()[1]):
                _kernel[_i].append(_matrices[_j].kernel[_i][_k])
    return Matrix(_kernel)


def matrix_vertical_stack(matrices: list):
    """
    stacking two matrices vertically.
    :param matrices: (list of Matrix)
    :return: (Matrix)
    """
    assert matrices
    for _i in range(1, len(matrices)):
        assert matrices[_i].basic_data_type() == matrices[0].basic_data_type()
        assert matrices[_i].size()[1] == matrices[0].size()[1]
    _matrices = deepcopy(matrices)
    _kernel = []
    _row = 0
    for _i in range(len(_matrices)):
        for _j in range(_matrices[_i].size()[0]):
            _kernel.append([])
            for _k in range(_matrices[0].size()[1]):
                _kernel[_row + _j].append(_matrices[_i].kernel[_j][_k])
        _row += _matrices[_i].size()[0]
    return Matrix(_kernel)


def homogeneous_linear_equations(a: Matrix):
    """
    figure out the fundamental system of solutions of homogeneous linear equations: a * X = Matrix(zero).
    :param a: (Matrix) as above
    :return: (list of Matrix) fundamental system of solutions
    """
    # upper triangle
    _a, dependent_cols = a.stepped(simplified=True, _new=True, _dependent_cols_needed=True)
    # fundamental solutions
    independent_cols = []
    for _i in range(_a.size()[1]):
        if _i not in dependent_cols:
            independent_cols.append(_i)
    _len = len(independent_cols)
    _fundamental_solutions_matrix = matrix_zero(_a.size()[1], _len, Meta.get_meta(_a.kernel[-1][-1], 'ZERO'))
    _fundamental_solutions_matrix.fill(dependent_cols, range(_len),
                                       (-_a.part(range(_a.size()[0]), independent_cols)).kernel)
    _fundamental_solutions_matrix.fill(independent_cols, range(_len),
                                       matrix_one(_len, _len, Meta.get_meta(_a.kernel[-1][-1], 'ONE')).kernel)
    _fundamental_solutions_list = [_fundamental_solutions_matrix.part(range(_a.size()[1]), [_i]) for _i in range(_len)]
    return _fundamental_solutions_list


def non_homogeneous_linear_equations(a: Matrix, b: Matrix):
    """
    figure out the fundamental system of solutions and one special solution of non homogeneous linear equations:
    a * X = b.
    good news ! argument {b} could be a multi-columns matrix, which means this function can solve multiple equations at
    the same time.
    :param a: (Matrix) as above
    :param b: (Matrix) as above
    :return: (list of fundamental solutions, list of special solutions)
    """
    assert a.basic_data_type().__name__ == b.basic_data_type().__name__
    assert a.size()[0] == b.size()[0]
    _a = matrix_horizontal_stack([a, b])
    _a, dependent_cols = _a.stepped(simplified=True, _dependent_cols_needed=True)
    # fundamental solutions
    _dependent_cols = []
    _independent_cols = []
    for _i in range(a.size()[1]):
        if _i in dependent_cols:
            _dependent_cols.append(_i)
        else:
            _independent_cols.append(_i)
    _rank = len(_dependent_cols)
    _len = len(_independent_cols)
    if _len == 0:
        _fundamental_solutions_list = []
    else:
        _fundamental_solutions_matrix = matrix_zero(a.size()[1], _len, Meta.get_meta(_a.kernel[-1][-1], 'ZERO'))
        _fundamental_solutions_matrix.fill(_dependent_cols, range(_len),
                                           (-_a.part(range(_a.size()[0]), _independent_cols)).kernel)
        _fundamental_solutions_matrix.fill(_independent_cols, range(_len),
                                           matrix_one(_len, _len, Meta.get_meta(_a.kernel[-1][-1], 'ONE')).kernel)
        _fundamental_solutions_list = [_fundamental_solutions_matrix.part(range(a.size()[1]), [i]) for i in range(_len)]
    # special solutions
    _special_solutions_list = []
    for _i in range(b.size()[1]):
        _row = b.size()[0] - 1
        while Meta.determine_meta(_a.kernel[_row][a.size()[1] + _i], 'ZERO'):
            _row -= 1
        if _row < _rank:
            _special_solution = matrix_zero(a.size()[1], 1, Meta.get_meta(_a.kernel[-1][-1], 'ZERO'))
            _special_solution.fill(_dependent_cols, [0], _a.part(range(_a.size()[0]), [a.size()[1] + _i]).kernel)
            _special_solutions_list.append(_special_solution)
        else:
            _special_solutions_list.append(None)
    return _fundamental_solutions_list, _special_solutions_list
