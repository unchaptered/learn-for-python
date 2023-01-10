# Address of variables

a = [1, 2, 3]
b = a
print(a, b)                 # [1, 2, 3] [1, 2, 3]
print(id(a), id(b), '\n')   # 2411176307912 2411176307912

a[1] = 4
print(a, b)                 # [1, 4, 3] [1, 4, 3]
print(id(a), id(b), '\n')   # 2411176307912 2411176307912

c = a[:]
print(a, c)                 # [1, 4, 3] [1, 4, 3] [1, 4, 3]
print(id(a), id(c), '\n')   # 1544109010120 1544109026990

from copy import copy

d = copy(a)
print(a, d)                 # [1, 4, 3], [1, 4, 3]
print(id(a), id(d))         # 2672299650248 2672301164744