
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
def LP_PP_MIKP(c, a, b, n, l, u, P, N):
    k = -1
    x = c
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
            if j in N:
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
