from math import floor

def Domination(a1, c1, l1, u1, a2, c2, l2, u2 ):
    LOOP_MAX = 12313456
    
    if c2 ==0 or a2 ==0 or c1 / c2 == a1 / a2:
        status = "failure"
        return (status, k1, k2)
    else c2 / a2 > c1 / a1:
        #(c1, a1, l1, u1) = (c2, a2, l2, u2)
        #Compute k1, k2 (recursion) and obtain status
        (status, k_1, k_2) = Domination(a2, c2, l2, u2, a1, c1, l1, u1 )
        k1 = k_2
        k2 = k_1
        return (status, k1, k2)

    if a1 != 0:
        if -a2 * c1 \ a1 + c2 > 0:
            k2 = -1
        else:
            k2 = 1
    else a2 != 0:
        if -a1 * c2 \ a2 + c1 >0:
            k2 = -1
        else:
            k2 = 1
    
    L1 = max(l1-u1, k1, -1*LOOP_MAX)
    U2 = min(u2-l2, k2, LOOP_MAX)

    if abs(L1) <= abs(U2):
        for k1 in range(-1, L1):
            k2 = floor(-k1(a1/a2))
            if k2 < -k1(c1/c2):
                status = "success"
                return (status, k1, k2)
    else:
        for k2 in range(1, U2):
            k1 = floor(-k2(c2/c1)) - 1
            if k1 >= -k2(a2/a1):
                status = "success"
                return = (status, k1, k2)
    status = "failure"
    return (status, k1, k2)
    
