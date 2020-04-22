from polynomial import Polynomial, p1, p2
from matrix import *

p3 = Polynomial(5, 1, -2)
print("p1 = " + str(p1))
print("p2 = " + str(p2))
print("p3 = " + str(p3))

m1 = Matrix(
    [
        [1, 2, 5, 6],
        [3, 4, 4, 2],
        [7, 3, 9, 0],
    ]
)
print("m1 = " + str(m1))