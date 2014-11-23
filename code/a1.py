def gete(c,a,n,en,ep):
    e = c
    for i in range(n):
        if a[i]!=0:
            e[i] = c[i]/a[i]
        elif a[i]==0 and c[i]>0:
            e[i] = ep
        elif a[i]==0 and c[i]<0:
            e[i] = en
    return e


def preprocessing(c,a,b,l,u,n):
    k0 = -1
    k1 = -1
    k2 = -1
    en = float("-inf")
    ep = float("inf")
    e = gete(c,a,n,en,ep)
    status = "problem is not unbounded and is not trivial"
    for i in range(n):
        if (a[i]<=0 and c[i]>0 and u[i] == ep) or (a[i]>=0 and c[i]<0 and l[i] == en):
            k0 = i
            status = "potentiator"
            return status
        elif (a[i]>0 and c[i]>0 and u[i] == ep) or (a[i]<0 and c[i]<0 and l[i] == en) and e[i]>ep:
            en = e[i]
            k1 = i
        elif (a[i]>0 and c[i]>=0 and l[i] == en) or (a[i]<0 and c[i]<=0 and u[i] == ep) and e[i]<en:
            ep = e[i]
            k2 = i

    if en > ep:
        status = "incrementor/decrementor pair"
    elif ep == 0:
        status = "accumulator"
    return status
