import wmath


c = [[1]]
a = wmath.Matrix([c, [[2]]])
b = a.part([0], [0], _deepcopy=False)
d = a.part([0], [0], _deepcopy=True)
print('b=', b, '\nd=', d)
c[0][0] = 10
print('b=', b, '\nd=', d)
a.kernel[0][0][0] = 11
print('b=', b, '\nd=', d, '\nc=', c)
