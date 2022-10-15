# This program checks whether an user input integer is a cube or a square, or is neither.

from math import sqrt
from numpy import cbrt

n = int(input())
flag = 0
if int(int((cbrt(n)))**3) == n:
    print('This is a cube number')
else:
    flag += 1
if int(int(sqrt(n))**2) == n:
    print('This is a square number')
else:
    flag += 1
if flag == 2:
    print('This is neither a cube number, nor a square number')
