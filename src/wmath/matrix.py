"""
matrix.py
this script is response for the problems related to matrix.
"""
from wmath.meta import Meta
from wmath.paradigm import Paradigm
from wmath.fraction import list2str
from copy import deepcopy


class Matrix(Paradigm):
    """
    define the class of matrix and related operations among them.
    """
    def __init__(self, kernel: list, _deepcopy: bool = False):
        super().__init__()
        if _deepcopy:
            kernel = deepcopy(kernel)
        else:
            kernel = kernel
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

    def horizontal_split(self):
        """
        return a list of Matrix which is horizontally split from self.
        :return: (list of Matrix)
        """
        _self = +self
        _list = []
        for _i in range(_self.size()[1]):
            _list.append([])
            for _j in range(_self.size()[0]):
                _list[_i].append([_self.kernel[_j][_i]])
        for _i in range(_self.size()[1]):
            _list[_i] = Matrix(_list[_i])
        return _list

    def vertical_split(self):
        """
        return a list of Matrix which is vertically split from self.
        :return: (list of Matrix)
        """
        _self = +self
        _list = []
        for _i in range(_self.size()[0]):
            _list.append([[]])
            for _j in range(_self.size()[1]):
                _list[_i][0].append(_self.kernel[_i][_j])
        for _i in range(_self.size()[0]):
            _list[_i] = Matrix(_list[_i])
        return _list

    def part(self, _rows=None, _cols=None, _deepcopy: bool = True):
        """
        return a new Matrix with values copied or deep-copied from {self}, specified by {rows} and {cols}.
        _rows(_cols) accept range (_from, _to, _step) or list [a1, a2, ...] type.
        :param _rows: (range or list of int or None if you choose all rows)
        :param _cols: (range or list of int or None if you choose all cols)
        :param _deepcopy: (bool)
        :return: (Matrix)
        """
        if _rows is None:
            _rows = range(self.size()[0])
        if _cols is None:
            _cols = range(self.size()[1])
        _kernel = []
        for _i in _rows:
            _list = []
            for _j in _cols:
                if _deepcopy:
                    _list.append(deepcopy(self.kernel[_i][_j]))
                else:
                    _list.append(self.kernel[_i][_j])
            _kernel.append(_list)
        return Matrix(_kernel)

    def fill(self, other, _rows=None, _cols=None, _new=False):
        """
        fill specific part of {self} with corresponding values in {other}.
        the part is specified by {_rows} and {_cols}.
        the size of {other} must be bigger than or equal to (len(_rows), len(_cols)).
        :param other: (Matrix or list2d or tuple with the same basic_data_type of self)
        :param _rows: (range or list of int or None if you choose all rows)
        :param _cols: (range or list of int or None if you choose all cols)
        :param _new: (bool) (bool) True for a new matrix, False for no
        :return: (Matrix) if _new: a new matrix, else: self after filling
        """
        if _new:
            _self = +self
        else:
            _self = self
        if type(other).__name__ == 'Matrix':
            other = other.kernel
        if _rows is None:
            _rows = range(_self.size()[0])
        if _cols is None:
            _cols = range(_self.size()[1])
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

    def transpose(self, _new: bool = True, _deepcopy: bool = True):
        """
        transpose
        _new decides whether to return a new matrix or applying change on {self}.
        :param _new: (bool)
        :param _deepcopy: (bool)
        :return: (Matrix) if _new: a new matrix, else: self after transpose
        """
        _kernel = []
        for _i in range(self.size()[1]):
            _kernel.append([])
            for _j in range(self.size()[0]):
                if _deepcopy:
                    _kernel[_i].append(deepcopy(self.kernel[_j][_i]))
                else:
                    _kernel[_i].append(self.kernel[_j][_i])
        if _new:
            return Matrix(_kernel)
        else:
            self.kernel = _kernel
            return self

    def conjugate(self, _new: bool = True):
        """
        conjugate
        :param _new: (bool)
        :return: (Matrix) if _new: a new matrix, else: self after conjugate
        """
        if _new:
            _self = +self
        else:
            _self = self
        for _i in range(_self.size()[0]):
            for _j in range(_self.size()[1]):
                _self.kernel[_i][_j] = _self.kernel[_i][_j].conjugate()
        return _self

    def stepped(self, standardized: bool = False, simplified: bool = False, _new: bool = True,
                _neg_needed: bool = False, _independent_cols_needed: bool = False):
        """
        turn any matrix into stepped or standardized stepped or simplified stepped matrix.
        :param simplified: (bool)
        :param standardized: (bool)
        :param _new: (bool)
        :param _neg_needed: (bool)
        :param _independent_cols_needed: (bool)
        :return: (Matrix) if _new: a new matrix, else: self after stepped or standardized stepped or simplified stepped.
            (multi) Matrix as above, [_neg: (bool) if _neg_needed],
            [_independent_cols: (list) if _independent_cols_needed]
        """
        if _new:
            _self = +self
        else:
            _self = self

        # independent_cols and neg
        independent_cols = []
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
            independent_cols.append(_col)

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

            # dependent_cols
            dependent_cols = []
            for _i in range(_self.size()[1]):
                if _i not in independent_cols:
                    dependent_cols.append(_i)

            for _i in range(len(independent_cols) - 1, -1, -1):
                for __row in range(_i):
                    __times = _self.kernel[__row][independent_cols[_i]] / _self.kernel[_i][independent_cols[_i]]
                    for __col in dependent_cols:
                        if __col > independent_cols[_i]:
                            _self.kernel[__row][__col] -= __times * _self.kernel[_i][__col]
                    _self.kernel[__row][independent_cols[_i]] = Meta.get_meta(_self.kernel[-1][-1], 'ZERO')
                for __col in dependent_cols:
                    if __col > independent_cols[_i]:
                        _self.kernel[_i][__col] /= _self.kernel[_i][independent_cols[_i]]
                _self.kernel[_i][independent_cols[_i]] = Meta.get_meta(_self.kernel[-1][-1], 'ONE')
        else:

            # standardized
            if standardized:
                for _i in range(len(independent_cols) - 1, -1, -1):
                    for __col in range(independent_cols[_i] + 1, _self.size()[1]):
                        _self.kernel[_i][__col] /= _self.kernel[_i][independent_cols[_i]]
                    _self.kernel[_i][independent_cols[_i]] = Meta.get_meta(_self.kernel[-1][-1], 'ONE')

        if _neg_needed and _independent_cols_needed:
            return _self, _neg, independent_cols
        elif _neg_needed and ~_independent_cols_needed:
            return _self, _neg
        elif ~_neg_needed and _independent_cols_needed:
            return _self, independent_cols
        else:
            return _self

    def trace(self):
        """
        trace of matrix.
        :return: (self.basic_data_type())
        """
        assert self.size()[0] == self.size()[1]
        _trace = Meta.get_meta(self.kernel[-1][-1], 'ZERO')
        for _i in range(self.size()[0]):
            _trace += self.kernel[_i][_i]
        return _trace

    def rank(self):
        """
        rank of matrix.
        :return: (int) rank
        """
        _, independent_cols = self.stepped(_independent_cols_needed=True)
        return len(independent_cols)

    def determinant_upper_triangle(self):
        """
        calc determinant of a square matrix with upper triangle method.
        :return: (Fraction) determinant
        """
        assert self.size()[0] == self.size()[1]
        _self, _neg, _independent_cols = self.stepped(_neg_needed=True, _independent_cols_needed=True)
        if len(_independent_cols) < _self.size()[0]:
            return Meta.get_meta(_self.kernel[-1][-1], 'ZERO')
        if _neg:
            _determinant = -Meta.get_meta(_self.kernel[-1][-1], 'ONE')
        else:
            _determinant = Meta.get_meta(_self.kernel[-1][-1], 'ONE')
        for _index in _independent_cols:
            _determinant *= _self.kernel[_index][_index]
        return _determinant

    def determinant_definition(self):
        """
        calc determinant of a square matrix according to the definition of determinant.
        it runs much slower than determinant_upper_triangle(). but it's very useful when upper triangle is invalid, such
        as Matrix(Polynomial) since Polynomial's truediv return two arguments rather than one.
        :return: (Fraction) determinant
        """
        assert self.size()[0] == self.size()[1]

        def __determinant(__self: Matrix, __rows, __cols):
            assert len(__rows) == len(__cols)
            if len(__rows) == 1:
                return __self.kernel[__rows[0]][__cols[0]]
            _determinant = Meta.get_meta(__self.kernel[-1][-1], 'ZERO')
            for _i in range(len(__rows)):
                if _i % 2:
                    _determinant -= __self.kernel[__rows[_i]][__cols[0]] * \
                                    __determinant(__self, __rows[:_i] + __rows[_i + 1:], __cols[1:])
                else:
                    _determinant += __self.kernel[__rows[_i]][__cols[0]] * \
                                    __determinant(__self, __rows[:_i] + __rows[_i + 1:], __cols[1:])
            return _determinant

        return __determinant(self, list(range(self.size()[0])), list(range(self.size()[1])))

    def inverse(self, _new: bool = True):
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
            _determinant = self.determinant_upper_triangle()
            return _inverse.times(_determinant)
        if self.rank() < self.size()[0] - 1:
            return matrix_zero(self.size()[0], self.size()[1], Meta.get_meta(self.kernel[-1][-1], 'ZERO'))
        _kernel = []
        for _i in range(self.size()[0]):
            _kernel.append([])
            for _j in range(self.size()[1]):
                _i_list = [__i for __i in range(self.size()[0]) if __i != _i]
                _j_list = [__j for __j in range(self.size()[0]) if __j != _j]
                _kernel[_i].append(self.part(_i_list, _j_list).determinant_upper_triangle())
        return Matrix(_kernel)

    def is_diagonal(self):
        if self.size()[0] != self.size()[1]:
            return False
        for _i in range(self.size()[0]):
            for _j in range(self.size()[1]):
                if _i != _j and not Meta.determine_meta(self.kernel[_i][_j], 'ZERO'):
                    return False
        return True

    def is_upper_triangle(self):
        if self.size()[0] != self.size()[1]:
            return False
        for _i in range(self.size()[0]):
            for _j in range(_i):
                if not Meta.determine_meta(self.kernel[_i][_j], 'ZERO'):
                    return False
        return True

    def is_hermite(self):
        if self.size()[0] != self.size()[1]:
            return False
        for _i in range(self.size()[0]):
            for _j in range(_i + 1, self.size()[1]):
                if not Meta.determine_meta(self.kernel[_i][_j] - self.kernel[_j][_i].conjugate(), 'ZERO'):
                    return False
        return True

    def is_upper_hessenberg(self):
        if self.size()[0] != self.size()[1]:
            return False
        for _i in range(self.size()[0]):
            for _j in range(self.size()[1]):
                if _j < _i - 1:
                    if not Meta.determine_meta(self.kernel[_i][_j], 'ZERO'):
                        return False
        return True

    def is_tridiagonal(self):
        if self.size()[0] != self.size()[1]:
            return False
        for _i in range(self.size()[0]):
            for _j in range(self.size()[1]):
                if _j < _i - 1 or _j > _i + 1:
                    if not Meta.determine_meta(self.kernel[_i][_j], 'ZERO'):
                        return False
        return True

    def qr_schmidt_decomposition(self, _column_linearly_independent: bool = False):
        """
        QR decomposition of matrix using schmidt method.
        :param _column_linearly_independent: (bool) mark this param True if you are sure
                                                    that the matrix is column linearly independent
        :return: (Matrix, Matrix) Q, R
        """
        def __inner(col1: Matrix, col2: Matrix):
            __result = Meta.get_meta(col1.kernel[-1][-1], 'ZERO')
            for __i in range(col1.size()[0]):
                __result += col1.kernel[__i][0] * col2.kernel[__i][0].conjugate()
            return __result

        _one = Meta.get_meta(self.kernel[-1][-1], 'ONE')
        independent_cols = []
        if not _column_linearly_independent:
            _, independent_cols = self.stepped(_independent_cols_needed=True)
            _column_linearly_independent = len(independent_cols) == self.size()[1]

        if _column_linearly_independent:

            _self = self.horizontal_split()
            _unitary = [+_i for _i in _self]
            _triangle = matrix_one(self.size()[1], self.size()[1], _one)
            _inner = []

            for _i in range(self.size()[1]):
                for _j in range(_i):
                    _coefficient = __inner(_self[_i], _unitary[_j]) / _inner[_j]
                    _triangle.kernel[_j][_i] = _coefficient
                    _unitary[_i] -= _unitary[_j].times(_coefficient, _new=True)
                _inner.append(__inner(_unitary[_i], _unitary[_i]))

            _unitary = matrix_horizontal_stack(_unitary)

            for _i in range(self.size()[1]):
                _coefficient = _inner[_i] ** 0.5
                _triangle.times(_coefficient, _rows=[_i])
                _unitary.times(_one / _coefficient, _cols=[_i])

            return _unitary, _triangle

        else:
            independent_part = self.part(_cols=independent_cols)
            independent_unitary, _ = independent_part.qr_schmidt_decomposition(_column_linearly_independent=True)
            dependent_unitary_list = homogeneous_linear_equations(independent_part.transpose().conjugate())
            for _i in dependent_unitary_list:
                _i.times(_one / __inner(_i, _i) ** 0.5)
            dependent_unitary = matrix_horizontal_stack(dependent_unitary_list)
            _unitary = matrix_zero(self.size()[0], self.size()[1], _one)
            _unitary.fill(independent_unitary.kernel, _rows=None, _cols=independent_cols)
            dependent_cols = []
            for _i in range(self.size()[1]):
                if _i not in independent_cols:
                    dependent_cols.append(_i)
            _unitary.fill(dependent_unitary.kernel, _rows=None, _cols=dependent_cols)
            _triangle = _unitary.transpose().conjugate() * self
            return _unitary, _triangle

    def qr_householder_decomposition(self, _unitary_need: bool = False):
        """
        qr decomposition of matrix using householder method.
        matrix must be square.
        :param _unitary_need: (bool)
        :return: ([Matrix, ]Matrix) [Q, ]R
        """
        assert self.size()[0] == self.size()[1]
        _triangle = +self
        _len = _triangle.size()[0]
        _one = Meta.get_meta(_triangle.kernel[-1][-1], 'ONE')
        _unitary = matrix_one(_len, _len, _one)
        for _i in range(_len - 1):
            if Meta.determine_meta(_triangle.part(_rows=range(_i + 1, _len), _cols=[_i]), 'ZERO'):
                continue
            _v = _triangle.part(_rows=range(_i, _len), _cols=[_i])
            _v_norm_2 = (_v.transpose() * _v.conjugate()).kernel[0][0] ** 0.5
            _e = matrix_one(_len - _i, 1, -(_v.kernel[0][0] / abs(_v.kernel[0][0])) * _v_norm_2)
            _u = _v - _e
            _times = _one * 2 / (_u.transpose() * _u.conjugate()).kernel[0][0]
            _sub_p = matrix_one(_len - _i, _len - _i, _one) - (_u * _u.transpose().conjugate()).times(_times)
            _triangle.fill(_e.kernel, _rows=range(_i, _len), _cols=[_i])
            _triangle.fill((_sub_p * _triangle.part(_rows=range(_i, _len), _cols=range(_i + 1, _len))).kernel,
                           _rows=range(_i, _len), _cols=range(_i + 1, _len))
            if _unitary_need:
                _unitary.fill((_sub_p * _unitary.part(_rows=range(_i, _len))).kernel, _rows=range(_i, _len))
        if _unitary_need:
            _unitary.transpose(_new=False).conjugate(_new=False)
            return -_unitary, -_triangle
        else:
            return -_triangle

    def qr_givens_decomposition(self, _unitary_need: bool = True):
        """
        qr decomposition of matrix using givens method.
        matrix must be square.
        :param _unitary_need: (bool)
        :return: ([Matrix, ]Matrix) [Q, ]R
        """
        assert self.size()[0] == self.size()[1]
        _triangle = +self
        _len = _triangle.size()[0]
        _one = Meta.get_meta(_triangle.kernel[-1][-1], 'ONE')
        _unitary = matrix_one(_len, _len, _one)
        for _i in range(_len - 1):
            for _j in range(_i + 1, _len):
                if Meta.determine_meta(_triangle.kernel[_j][_i], 'ZERO'):
                    continue
                _a = _triangle.kernel[_i][_i]
                _a_norm = _a * _a.conjugate()
                _b = _triangle.kernel[_j][_i]
                _b_norm = _b * _b.conjugate()
                _norm_2 = (_a_norm + _b_norm) ** 0.5
                _c1 = _a.conjugate() / _norm_2
                _s1 = _b.conjugate() / _norm_2
                _s2 = -_b / _norm_2
                _c2 = _a / _norm_2
                _g = Matrix([[_c1, _s1], [_s2, _c2]])
                _triangle.fill((_g * _triangle.part(_rows=[_i, _j], _cols=range(_i, _len))).kernel,
                               _rows=[_i, _j], _cols=range(_i, _len))
                if _unitary_need:
                    _unitary.fill((_g * _unitary.part(_rows=[_i, _j])).kernel, _rows=[_i, _j])
        if _unitary_need:
            _unitary.transpose(_new=False).conjugate(_new=False)
            return _unitary, _triangle
        else:
            return _triangle

    def upper_hessenberg(self, _unitary_need: bool = False, _is_hermite: bool = False):
        """
        make the matrix upper hessenberg.
        unitary * self * (unitary^T.conjugate()) is a hessenberg matrix.
        :param _unitary_need: (bool)
        :param _is_hermite: (bool) mark this param True if you are sure that the matrix is a hermitian
        :return: (Matrix or Matrix, Matrix)
        """
        assert self.size()[0] == self.size()[1]
        if not _is_hermite:
            _is_hermite = self.is_hermite()
        _triangle = +self
        _len = _triangle.size()[0]
        _one = Meta.get_meta(_triangle.kernel[-1][-1], 'ONE')
        _unitary = matrix_one(_len, _len, _one)
        for _i in range(1, _len - 1):
            if Meta.determine_meta(_triangle.part(_rows=range(_i + 1, _len), _cols=[_i - 1]), 'ZERO'):
                continue
            _v = _triangle.part(_rows=range(_i, _len), _cols=[_i - 1])
            _v_norm_2 = (_v.transpose() * _v.conjugate()).kernel[0][0] ** 0.5
            _e = matrix_one(_len - _i, 1, -(_v.kernel[0][0] / abs(_v.kernel[0][0])) * _v_norm_2)
            _u = _v - _e
            _times = _one * 2 / (_u.transpose() * _u.conjugate()).kernel[0][0]
            _sub_p = matrix_one(_len - _i, _len - _i, _one) - (_u * _u.transpose().conjugate()).times(_times)
            _triangle.fill(_e.kernel, _rows=range(_i, _len), _cols=[_i - 1])
            if _is_hermite:
                _triangle.fill(_e.transpose().conjugate().kernel, _rows=[_i - 1], _cols=range(_i, _len))
            else:
                _triangle.fill((_triangle.part(_rows=range(_i), _cols=range(_i, _len)) * _sub_p).kernel,
                               _rows=range(_i), _cols=range(_i, _len))
            _triangle.fill((_sub_p * _triangle.part(_rows=range(_i, _len), _cols=range(_i, _len)) *
                            _sub_p).kernel, _rows=range(_i, _len), _cols=range(_i, _len))
            if _unitary_need:
                _unitary.fill((_sub_p * _unitary.part(_rows=range(_i, _len))).kernel, _rows=range(_i, _len))
        if _unitary_need:
            return _triangle, _unitary
        else:
            return _triangle

    def eigenvalue(self):
        """
        Q * self * Q.transpose().conjugate() is an upper triangle matrix which contains all self's eigenvalue.
        :return: ([Matrix, ]Matrix) [Q, ]D
        """
        assert self.size()[0] == self.size()[1]
        if not self.is_upper_hessenberg():
            _self = self.upper_hessenberg()
        else:
            _self = +self
        _eigenvalue = []
        _is_tridiagonal = _self.is_tridiagonal()
        while not _self.is_upper_triangle():
            _len = _self.size()[0]
            _givens = [matrix_one(2, 2, Meta.get_meta(_self.kernel[-1][-1], 'ONE'))] * (_len - 1)
            for _i in range(_len - 1):
                if Meta.determine_meta(_self.kernel[_i + 1][_i], 'ZERO'):
                    continue
                _a = _self.kernel[_i][_i]
                _a_norm = _a * _a.conjugate()
                _b = _self.kernel[_i + 1][_i]
                _b_norm = _b * _b.conjugate()
                _norm_2 = (_a_norm + _b_norm) ** 0.5
                _c1 = _a.conjugate() / _norm_2
                _s1 = _b.conjugate() / _norm_2
                _s2 = -_b / _norm_2
                _c2 = _a / _norm_2
                _g = Matrix([[_c1, _s1], [_s2, _c2]])
                _givens[_i] = _g
                if _is_tridiagonal:
                    _self.fill((_g * _self.part(_rows=[_i, _i + 1], _cols=range(_i, min(_i + 3, _len)))).kernel, _rows=[_i, _i + 1], _cols=range(_i, min(_i + 3, _len)))
                else:
                    _self.fill((_g * _self.part(_rows=[_i, _i + 1], _cols=range(_i, _len))).kernel, _rows=[_i, _i + 1], _cols=range(_i, _len))
            for _i in range(_len - 1):
                if _is_tridiagonal:
                    _self.fill((_self.part(_rows=range(max(0, _i - 1), _i + 2), _cols=[_i, _i + 1]) * _givens[_i].transpose().conjugate()).kernel, _rows=range(max(0, _i - 1), _i + 2), _cols=[_i, _i + 1])
                else:
                    _self.fill((_self.part(_rows=range(_i + 2), _cols=[_i, _i + 1]) * _givens[_i].transpose().conjugate()).kernel, _rows=range(_i + 2), _cols=[_i, _i + 1])
            if Meta.determine_meta(_self.kernel[-1][-2], 'ZERO'):
                _eigenvalue.append(_self.kernel[-1][-1])
                _self = _self.part(range(_len - 1), range(_len - 1))
        for _i in range(_self.size()[0]):
            _eigenvalue.append(_self.kernel[_i][_i])
        return _eigenvalue


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


def matrix_one(_row: int, _col: int, _value, _other_value=None):
    """
    return a 'E' matrix with {_value} on the diagonal, with a size (_row, _col).
    :param _row: (int)
    :param _col: (int)
    :param _value: (any)
    :param _other_value: (any) by default, _other_value is None, that means Meta.get_meta(_value, 'ZERO').
    :return: (Matrix)
    """
    if _other_value is None:
        _other_value = Meta.get_meta(_value, 'ZERO')
    _kernel = [[_other_value for _j in range(_col)] for _i in range(_row)]
    for _i in range(min(_row, _col)):
        _kernel[_i][_i] = _value
    return Matrix(_kernel)


def matrix_horizontal_stack(matrices: list, _deepcopy: bool = True):
    """
    stack matrices horizontally.
    :param matrices: (list of Matrix)
    :param _deepcopy: (bool)
    :return: (Matrix)
    """
    assert matrices
    for _i in range(1, len(matrices)):
        assert matrices[_i].basic_data_type() == matrices[0].basic_data_type()
        assert matrices[_i].size()[0] == matrices[0].size()[0]
    if _deepcopy:
        _matrices = deepcopy(matrices)
    else:
        _matrices = matrices
    _kernel = []
    for _i in range(_matrices[0].size()[0]):
        _kernel.append([])
        for _j in range(len(_matrices)):
            for _k in range(_matrices[_j].size()[1]):
                _kernel[_i].append(_matrices[_j].kernel[_i][_k])
    return Matrix(_kernel)


def matrix_vertical_stack(matrices: list, _deepcopy: bool = True):
    """
    stacking two matrices vertically.
    :param matrices: (list of Matrix)
    :param _deepcopy: (bool)
    :return: (Matrix)
    """
    assert matrices
    for _i in range(1, len(matrices)):
        assert matrices[_i].basic_data_type() == matrices[0].basic_data_type()
        assert matrices[_i].size()[1] == matrices[0].size()[1]
    if _deepcopy:
        _matrices = deepcopy(matrices)
    else:
        _matrices = matrices
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
    _a, independent_cols = a.stepped(simplified=True, _independent_cols_needed=True)
    # fundamental solutions
    dependent_cols = []
    for _i in range(_a.size()[1]):
        if _i not in independent_cols:
            dependent_cols.append(_i)
    _len = len(dependent_cols)
    if _len == 0:
        return []
    _fundamental_solutions_matrix = matrix_zero(_a.size()[1], _len, Meta.get_meta(_a.kernel[-1][-1], 'ZERO'))
    _fundamental_solutions_matrix.fill((-_a.part(range(_a.size()[0]), dependent_cols)).kernel,
                                       independent_cols, range(_len))
    _fundamental_solutions_matrix.fill(matrix_one(_len, _len, Meta.get_meta(_a.kernel[-1][-1], 'ONE')).kernel,
                                       dependent_cols, range(_len))
    _fundamental_solutions_list = [_fundamental_solutions_matrix.part(range(_a.size()[1]), [_i]) for _i in range(_len)]
    return _fundamental_solutions_list


def non_homogeneous_linear_equations(a: Matrix, b: Matrix):
    """
    figure out the fundamental system of solutions and one special solution of non-homogeneous linear equations:
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
    _a, independent_cols = _a.stepped(simplified=True, _independent_cols_needed=True)
    # fundamental solutions
    _independent_cols = []
    _dependent_cols = []
    for _i in range(a.size()[1]):
        if _i in independent_cols:
            _independent_cols.append(_i)
        else:
            _dependent_cols.append(_i)
    _rank = len(_independent_cols)
    _len = len(_dependent_cols)
    if _len == 0:
        _fundamental_solutions_list = []
    else:
        _fundamental_solutions_matrix = matrix_zero(a.size()[1], _len, Meta.get_meta(_a.kernel[-1][-1], 'ZERO'))
        _fundamental_solutions_matrix.fill((-_a.part(range(_a.size()[0]), _dependent_cols)).kernel,
                                           _independent_cols, range(_len))
        _fundamental_solutions_matrix.fill(matrix_one(_len, _len, Meta.get_meta(_a.kernel[-1][-1], 'ONE')).kernel,
                                           _dependent_cols, range(_len))
        _fundamental_solutions_list = [_fundamental_solutions_matrix.part(range(a.size()[1]), [i]) for i in range(_len)]
    # special solutions
    _special_solutions_list = []
    for _i in range(b.size()[1]):
        _row = b.size()[0] - 1
        while Meta.determine_meta(_a.kernel[_row][a.size()[1] + _i], 'ZERO'):
            _row -= 1
        if _row < _rank:
            _special_solution = matrix_zero(a.size()[1], 1, Meta.get_meta(_a.kernel[-1][-1], 'ZERO'))
            _special_solution.fill(_a.part(range(_a.size()[0]), [a.size()[1] + _i]).kernel, _independent_cols, [0])
            _special_solutions_list.append(_special_solution)
        else:
            _special_solutions_list.append(None)
    return _fundamental_solutions_list, _special_solutions_list
