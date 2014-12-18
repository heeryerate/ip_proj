MINUS_INF = float("-inf")
INF = float("inf")

def gete(c,a,n):
    e = range(n)
    for i in range(n):
        if a[i]!=0:
            e[i] = float(c[i])/a[i]
        elif a[i]==0 and c[i]>0:
            e[i] = INF
        elif a[i]==0 and c[i]<0:
            e[i] = MINUS_INF

    return e


def preprocessing(c,a,b,l,u,n):
    k0 = -1
    k1 = -1
    k2 = -1
    en = MINUS_INF
    ep = INF
    e = gete(c,a,n)
    status = "problem is not unbounded and is not trivial"
    for i in range(n):
        if (a[i]<=0 and c[i]>0 and u[i] == INF) or (a[i]>=0 and c[i]<0 and l[i] == MINUS_INF):
            k0 = i
            status = "potentiator"
            return status
        elif (a[i]>0 and c[i]>0 and u[i] == INF) or (a[i]<0 and c[i]<0 and l[i] == MINUS_INF) and e[i] > en:
            en = e[i]
            k1 = i
        elif (a[i]>0 and c[i]>=0 and l[i] == MINUS_INF) or (a[i]<0 and c[i]<=0 and u[i] == INF) and e[i] < ep:
            ep = e[i]
            k2 = i

    if en > ep:
        status = "incrementor/decrementor pair"
    elif ep == 0:
        status = "accumulator"
    return status
