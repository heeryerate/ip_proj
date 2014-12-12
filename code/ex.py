MINUS_INF = float("-inf")
INF = float("inf")

from a1 import preprocessing
from a2 import LP_PP_MIKP
from a3 import PhaseII
from a4 import dualPhaseII
from a5 import Branching
from pro import *


#en = float("-inf")
#ep = float("inf")

a = [55, 81, 14, 52]
c = [29, 64, 104, 222]
b = 100
n = 4
l = [0,0,0,0]
u = [1,1,1,1]
I = 4
P = range(0)
N = range(0, 4)

#status = preprocessing(c, a, b, l, u, n)
#print ("preprocessing" ,status)

print("Original", c, a, b, l, u, n, I)

(c, a, b, n, l, u, I, obj_change) = Simplify_MIKP(c, a, b, n, l, u, I)
print ("Simplify_MIKP", c, a, b, l, u, n, I, obj_change)

# print "******Record those relaxed variables"
# print "******Fix the order"
# print "******Find out why and what if the lower bound is greater and equal to the upper bound"

#(c, a, b, n, l, u, I) = Strength_bounds(c, a, b, n, l, u, I)
#print "Strength_bounds"
#print(c, a, b, l, u, n, I)

#(c, a, b, n, l, u, I, obj_change_fix) = Fix_variables(c, a, b, n, l, u, I)
#print "Fix_variables"
#print(c, a, b, l, u, n, I, obj_change_fix)

#(c, a, b, n, l, u, I, obj_change_com) = Complement_variables(c, a, b, n, l, u, I)
#print "complement_variables"
#print(c, a, b, l, u, n, I, obj_change_com)

#branch_direction = "down"

#(x, k, status, objective, activity) = LP_PP_MIKP(c, a, b, n, l, u, P, N)
#print ("LP_PP_MIKP", x, k, status, objective, activity)

#(x, k, objective, activity, status) = PhaseII(c, a, b, n, l, u, P, N, x, k, objective, activity)
#print ("PhaseII", x, k, objective, activity, status)

#(activity, x, k, objective, status) = Branching(c, a, b, n, l, u, P, N, x, k, objective, activity, branch_direction)
#print ("Branching", activity, x, k, objective, status)

#print x, status
