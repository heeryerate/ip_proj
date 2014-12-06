from a1 import preprocessing
from a2 import LP_PP_MIKP
from a3 import PhaseII
from a4 import dualPhaseII
from a5 import Branching
from math import floor

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

status = preprocessing(c, a, b, l, u, n)
print ("preprocessing" ,status)

(x, k, status, objective, activity) = LP_PP_MIKP(c, a, b, n, l, u, P, N)
print ("LP_PP_MIKP", x, k, status, objective, activity)

(x, k, objective, activity, status) = PhaseII(c, a, b, n, l, u, P, N, x, k, objective, activity)
print ("PhaseII", x, k, objective, activity, status)

(activity, x, k, objective, status) = Branching(c, a, b, n, l, u, P, N, x, k, objective, activity, branch_direction)
print ("Branching", activity, x, k, objective, status)

#print x, status