def dualPhaseII(c, a, b, n, l, u, P, N, x, k, objective, activity):
        
    status = "None"
    while activity < b:
        if k in P:
            if a[k] * (x[k] - l[k]) < (activity - b):
                activity -= a[k] * (x[k] - l[k])
                objective -= c[k] * (x[k] - l[k])
            else:
                objective -= (activity - b) * c[k] / a[k]
                x[k] -= (activity - b) / a[k]
                activity = b
                status = "tight optimal"
                return (x, k, objective, activity, status)
            
        else:
            if u[k] < float("inf") and abs(a[k]) * (u[k] - x[k]) < (activity - b):
                activity -= abs(a[k]) * (u[k] - x[k])
                objective -= abs(c[k]) * (u[k] - x[k])
            else:
                objective -= (activity - b) * abs(c[k]) / abs(a[k])
                x[k] += (activity - b) / abs(a[k])
                activity = b
                status = "tight optimal"
                return (x, k, objective, activity, status)
            
        k = k - 1
        if k in P:
            x[k] = u[k]
        else:
            x[k] = l[k]
    
    status = "problem infeasible"
    return (x, k, objective, activity, status)