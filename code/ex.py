from a1 import preprocessing
from a2 import *

en = float("-inf")
ep = float("inf")

a = [10, 8, -1, -3, -6]
c = [2, 6, -3, -4, -7]
b = 10
n = 5
l = [0, 0, 1, 0, 0]
u = [5, 10, 9, ep, 2]
P = range(2)
N = range(2, 5)

branch_direction = "down"

print preprocessing(c, a, b, l, u, n)
<<<<<<< HEAD

(x, status) = LP_PP_MIKP(c, a, b, n, l, u, P, N)
=======
(x, k, status, objective, activity) = LP_PP_MIKP(c, a, b, n, l, u, P, N)
>>>>>>> 96f9312fd4f6f826deb7d1f35b8ff1e9b888a4b5

print x, status
