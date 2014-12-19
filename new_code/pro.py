import numpy as np
from preprocessing import gete
from collections import deque

def get_bound(node, n, b, a, c, ratios):
    if node.weight >= b:
        print "infeasible solution"
        return 0
    else:
        @memoized
        def bestvalue(i,j):
            if i == 0:
                return 0
            weight = a[i-1]
            cost = c[i - 1]
            if weight > j:
                return bestvalue(i - 1, j)
            else:
                return max(bestvalue(i - 1, j), bestvalue(i - 1, j - weight) + cost)
        j = b
        node.in_bag = [0] * n
        for i in xrange(len(a),0,-1):
            if (bestvalue(i,j) != bestvalue(i-1,j)):
                node.in_bag[i-1] = 1
                j -= a[i-1]
        node.cost = bestvalue(len(a),b)

def Strength_bounds(c, a, b, n, l, u, I):
    pu = range(n)
    pl = range(n)

    for k in range(n):
        if a[k] <= 0:
            pu[k] = float("inf")
        else:
            u1 = sum(a[i]*l[i] for i in range(I) if a[i] > 0 and i != k)
            u2 = sum(a[i]*u[i] for i in range(I) if a[i] < 0 and i != k)
            pu[k] = (b - u1 - u2) / a[k]
        
        if a[k] >= 0:
            pl[k] = float("-inf")
        else:  
            l1 = sum(a[i]*u[i] for i in range(I) if a[i] > 0 and i != k)
            l2 = sum(a[i]*l[i] for i in range(I) if a[i] < 0 and i != k)
            pl[k] = (b - l1 - l2) / a[k]

    for k in range(n):
        if k in range(I):
            pu[k] = min(np.floor(u[k]), np.floor(pu[k]))
            pl[k] = max(np.ceil(l[k]), np.ceil(pl[k]))
        else:
            pu[k] = min(u[k], pu[k])
            pl[k] = max(l[k], pl[k])    
    u = pu
    l = pl
    return (c, a, b, n, l, u, I)

def Fix_variables(c, a, b, n, l, u, I):
    obj_change_fix = 0
    for k in range(n):
        if a[k] <= 0 and c[k] > 0 or a[k] < 0 and c[k] >= 0:
            obj_change_fix += c[k]*u[k]
            b += -a[k]*u[k]
            a[k] = 0
            c[k] = 0
        elif a[k] >= 0 and c[k] < 0 or a[k] > 0 and c[k] <=0:
            obj_change_fix += c[k]*l[k]
            b += -a[k]*l[k]
            a[k] = 0
            c[k] = 0

    count = 0
    pI = 0
    pa = range(n)
    pc = range(n)
    pl = range(n)
    pu = range(n)
    for k in range(n):
        pa[count] = a[k]
        pc[count] = c[k]
        pl[count] = l[k] 
        pu[count] = u[k] 

        if a[k] != 0 and c[k] != 0:
            if k in range(I):       
                count += 1
                pI = count
            else:
                count += 1

    I = pI
    n = count
    a = pa[ : n]
    c = pc[ : n]
    l = pl[ : n]
    u = pu[ : n]

    return (c, a, b, n, l, u, I, obj_change_fix) 

def Complement_variables(c, a, b, n, l, u, I):
    obj_change_com = 0
    for k in range(n):
        if l[k] >= float("-inf") and l[k] < 0:
            obj_change_com += c[k]*l[k]
            b += -a[k]*l[k]
            l[k] = 0
            u[k] = u[k] - l[k]
        elif l[k] == float("-inf"):
            obj_change_com += c[k]*u[k]
            b += -a[k]*u[k]
            a[k] = -a[k]
            c[k] = -c[k]
            l[k] = 0
            u[k] = float("inf")

    return (c, a, b, n, l, u, I, obj_change_com) 

def Sort_data(c, a, b, n, l, u, I):
    e = gete(c,a,n)

    index = np.argsort(e)
    pa = range(n)
    pc = range(n)
    pl = range(n)
    pu = range(n)

    for i in range(n):
        pc[i] = c[index[n-1-i]]
        pa[i] = a[index[n-1-i]]
        pl[i] = l[index[n-1-i]]
        pu[i] = u[index[n-1-i]]

    a = pa
    c = pc
    l = pl
    u = pu

    return (c, a, b, n, l, u, I)

#def Aggregate_variables(c, a, b, n, l, u, I):
#    print "NEXT TIME..."
#    print "BLA BLA BLA BLA.."

def Simplify_MIKP(c, a, b, n, l, u, I):
    (c, a, b, n, l, u, I) = Strength_bounds(c, a, b, n, l, u, I)
    (c, a, b, n, l, u, I, obj_change_fix) = Fix_variables(c, a, b, n, l, u, I)
    (c, a, b, n, l, u, I, obj_change_com) = Complement_variables(c, a, b, n, l, u, I)
    (c, a, b, n, l, u, I) = Sort_data(c, a, b, n, l, u, I)
    #Aggregate_variables(c, a, b, n, l, u, I)

    return (c, a, b, n, l, u, I, obj_change_com+obj_change_fix) 


import collections
import functools


class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
        
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__
    
    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)
















