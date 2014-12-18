def PhaseII(c, a, b, n, l, u, P, N, x, k, q, objective, ac, nb, status):
    
    status = "None"
    while ac.weight > b:
        if k in P:
            if u[k] < float("inf") and a[k] * (u[k] - x[k]) < (b - ac.weight):
                ac.weight += a[k] * (u[k] - x[k])
                objective += c[k] * (u[k] - x[k])
            else:
                objective += (b - ac.weight) * c[k] / a[k]
                x[k] += (b - ac.weight) / a[k]
                ac.weight = b
                status = "tight optimal"
                return (x, k, objective, ac.weight, status)
        
        else:
            if abs(a[k]) * (x[k] - l[k]) < (b - ac.weight):
                ac.weight += abs(a[k]) * (x[k] - l[k])
                objective += (x[k] - l[k]) * abs(c[k])
            else:
                objective += (b - ac.weight) * abs(c[k]) / a[k]
                x[k] -= (b - ac.weight) / abs(a[k])
                activity = b
                status = "tight optimal"
                return (x, k, objective, activity, status)
            
        k += 1
        if k in P:
            x[k] = l[k]
        if k in N:
            x[k] = u[k]
        
    status = "optimal"
    if ac.cost > nb.cost:
        nb = ac
    if ac.bound > nb.cost:
        q.push(ac)
    return (x, k, q, nb, status)
     
        