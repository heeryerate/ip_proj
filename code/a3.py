def PhaseII(c, a, b, n, l, u, P, N, x, k, objective, activity):
    
    status = "None"
    while activity > b:
        if k in P:
            if u[k] < float("inf") and a[k] * (u[k] - x[k]) < (b - activity):
                activity += a[k] * (u[k] - x[k])
                objective += c[k] * (u[k] - x[k])
            else:
                objective += (b - activity) * c[k] / a[k]
                x[k] += (b - activity) / a[k]
                activity = b
                status = "tight optimal"
                return (x, k, objective, activity, status)
        
        else:
            if abs(a[k]) * (x[k] - l[k]) < (b - activity):
                activity += abs(a[k]) * (x[k] - l[k])
                objective += (x[k] - l[k]) * abs(c[k])
            else:
                objective += (b - activity) * abs(c[k]) / a[k]
                x[k] -= (b - activity) / abs(a[k])
                activity = b
                status = "tight optimal"
                return (x, k, objective, activity, status)
            
        k += 1
        if k in P:
            x[k] = l[k]
        if k in N:
            x[k] = u[k]
        
    status = "optimal"
    return (x, k, objective, activity, status)
     
        