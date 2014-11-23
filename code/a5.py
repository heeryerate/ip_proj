from math import floor
from a3 import PhaseII
from a4 import dualPhaseII

def Branching(c, a, b, n, l, u, P, N, x, k, objective, activity, branch_direction):
    
    if branch_direction == "down":
        u[k] = floor(x[k])
        activity += a[k] * (u[k] - x[k])
        objective -= c[k] * (u[k] - x[k])
        x[k] = u[k]
        if a[k] > 0:
            (x, k, objective, activity, status) = \
            PhaseII(c, a, b, n, l, u, P, N, x, k, objective, activity)
            return (x, k, objective, activity, status)
        else:
            (x, k, objective, activity, status) = \
            dualPhaseII(c, a, b, n, l, u, P, N, x, k, objective, activity)
            return (x, k, objective, activity, status)
    
    else:
        l[k] = floor(x[k]) + 1
        activity -= a[k] * (x[k] - l[k])
        objective += c[k] * (x[k] - l[k])
        x[k] = l[k]
        if a[k] > 0:
            (x, k, objective, activity, status) = \
            dualPhaseII(c, a, b, n, l, u, P, N, x, k, objective, activity)
            return (x, k, objective, activity, status)
        else:
            (x, k, objective, activity, status) = \
            PhaseII(c, a, b, n, l, u, P, N, x, k, objective, activity)
            return (x, k, objective, activity, status)
        