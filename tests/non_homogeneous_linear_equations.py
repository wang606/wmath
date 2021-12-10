import wmath
import random
import time
import copy


def get_random_list2d(m, n):
    molecule = [[random.randint(-50, 50) for _i in range(n)] for _j in range(m)]
    denominator = [[random.randint(1, 100) for _k in range(n)] for _l in range(m)]
    fraction = [[wmath.Fraction([molecule[_m][_n], denominator[_m][_n]]) for _n in range(n)] for _m in range(m)]
    return fraction


def get_random_list(n):
    molecule = [random.randint(-50, 50) for _i in range(n)]
    denominator = [random.randint(1, 100) for _k in range(n)]
    fraction = [wmath.Fraction([molecule[_n], denominator[_n]]) for _n in range(n)]
    return fraction


def get_random_float_list2d(m, n):
    molecule = [[random.randint(-50, 50) for _i in range(n)] for _j in range(m)]
    denominator = [[random.randint(1, 100) for _k in range(n)] for _l in range(m)]
    _float = [[molecule[_m][_n] / denominator[_m][_n] for _n in range(n)] for _m in range(m)]
    return _float


start_time = time.time()
# a * X = b, with result stored in c.
a = wmath.Matrix(get_random_float_list2d(8, 8))
b = wmath.Matrix(get_random_float_list2d(8, 4))
c = wmath.non_homogeneous_linear_equations(a, b)
# out put the result
# fundamental solutions
if c[0]:
    for i in c[0]:
        print(i.formula(), end=', ')
else:
    # in most situations, the rank is full.
    print('no fundamental solutions found')
print('\n\n')
# special solutions
for i in c[1]:
    if i:
        print(i.formula(), end=', ')
    else:
        print('None', end=', ')
print('\n\n')
# verification
for i in range(len(c[1])):
    j = a * c[1][i] - b.part(range(b.size()[0]), [i])
    # the output should be all True
    print(wmath.Meta.determine_meta(j, 'ZERO'), end=', ')
end_time = time.time()
print(end_time - start_time)
