def LP_PP_MIKP(c, a, b, n, l, u, P, N):
    k = -1
    x = l;
    en = float("-inf")
    ep = float("inf")
    activity = 0
    objective = 0
    for j in range(n-1,-1,-1):
        if j in N and u[j] == ep:
            k = j 
            x[k] = l[j]
            break
    
    for j in range(n):
        if j <= k:
            if j in P:
                activity = activity + u[j]*abs(a[j])
                objective = objective + u[j]*abs(c[j])
            else:
                activity = activity - l[j]*abs(a[j])
                objective = objective - l[j]*abs(c[j])
        else:
            if j in P:
                activity = activity + l[j]*abs(a[j])
                objective = objective + l[j]*abs(c[j])
            else:
                activity = activity - u[j]*abs(a[j])
                objective = objective - u[j]*abs(c[j])

    if activity < b:
        status = "feasible solution"
        return (x, k,  status, objective, activity)
    elif activity > b and k > -1:
        x[k] = (activity - b) / a[k]
        status = "optimal solution"
        return (x, k, status, objective, activity)
    else:
        status = "problem infeasible"
        return (x, k, status, objective, activity)
