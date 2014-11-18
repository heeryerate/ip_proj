def gete(c,a,b,l,u,n)
    e = c
    for i in range(n):
        if a[i]!=0:
            e[i] = c[i]/a[i]
        elif a[i]==0 and c[i]>0:
            e[i] = float("inf")
        elif a[i]==0 and c[i]<0:
            e[i] = float("-inf")
            


def prepocessing(c,a,b,e,l,u,n)
    k0 = -1
    k1 = -1
    k2 = -1
    ep = float("-inf")
    em = float("inf")
    status = "problem is not unbounded and is not trivial"
    for i in range(n):
        if a[i]<=0 and c[i]>0 and u[i] == float("inf") or a[i]>=0 and c[i]<0 and u[i] == float("-inf"):
            k0 = i
            status = "potentiator"
            return
        elif a[i]>0 and c[i]>0 and u[i] == float("inf") or a[i]<0 and c[i]<0 and u[i] == float("-inf") and e[i]>ep:
            ep = e[i]
            k1 = i
        elif a[i]>0 and c[i]>=0 and l[i] == float("-inf") or a[i]<0 and c[i]<=0 and u[i] == float("inf") and e[i]<em:
            em = e[i]
            k2 = i

    if ep > em:
        status = "incrementor/decrementor pair"
    elif em == 0:
        status = "accumulator"

    
            
