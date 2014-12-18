import numpy as np
import random

listlst = [4] * 15 + [10] * 15 + [15] * 15 + [20] * 15 + [22] * 15 + [25] * 15 + [27] * 15 + [30] * 15

count = 1

for n in listlst:
	a = range(n)
	c = range(n)
	l = range(n)
	u = range(n)
	for i in range(n):
		a[i] = random.randint(-100,100)
		if a[i] == 0:
			a[i] += 1
		c[i] = random.randint(-100,100)
		l[i] = random.randint(-100,100)
		u[i] = random.randint(-100,100)
	b = random.randint(1,100)

	pa = (str(w) for w in a)
	pc = (str(w) for w in a)

	print 10000+count, n, b, " ".join(pa), " ".join(pc)
     
    #print ' '.join(map(str, a))
	#print 10000+count, n, b, a, c
	count += 1