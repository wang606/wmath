import ctypes


float1 = float
a = float1(32.4)
print(id(float1), id(float))
b = ctypes.cast(9483392, ctypes.py_object).value
print(b)
