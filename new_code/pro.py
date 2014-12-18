#import numpy as np
from preprocessing import gete

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



















