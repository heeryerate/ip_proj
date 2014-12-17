"""
The Capacitated lot-sizing problem: two formulations.
Authors: Xi He, September 2, 2014
"""

#Import PuLP modeler functions
from pulp import *

T=6

#the list of the periods
Periods = [1, 2, 3, 4, 5, 6]

#the dictionary of the production costs
Production_cost = dict(zip(Periods, [3, 4, 3, 4, 4, 5]))

#the dictionary of the demands
Demand = dict(zip(Periods, [6, 7, 4, 6, 3, 8]))

#the dictionary of the storage costs
Storage_cost = dict(zip(Periods, [1, 1, 1, 1, 1, 1]))

#the dictionary of the set-up costs
Setup_cost = dict(zip(Periods, [12, 15, 30, 23, 19, 45]))

#Capacity
CAPACITY = 10

#######################################
#      The first formulation
#######################################

#Create the 'cls' variable to contain the problem data
cls = LpProblem("Capacitated lot-sizing problem_f1",  LpMinimize)

#three dictionaries called 'y,s,x' are created to contain the variables
y = LpVariable.dicts("y",  Periods, 0, None)
s = LpVariable.dicts("s", Periods,  0, None)
x = LpVariable.dicts("x", Periods, 0, 1,  LpInteger)

#the objection function
cls += lpSum([Production_cost[i] * y[i] + Storage_cost[i] * s[i] + Setup_cost[i] * x[i] for i in Periods]), "Total Cost"

#the constrains
cls += y[1] == Demand[1] + s[1], "The first period"

for i in Periods[1: T]:    
    cls += s[i - 1] + y[i] - Demand[i] - s[i]  == 0

w = sum(Demand.values())

for i in Periods:
    cls += y[i] - w * x[i] <= 0

cls += s[T] == 0

for i in Periods:
    cls += y[i] <= CAPACITY

#cls.writeLP("Capacitated lot-sizing problem_f1.lp")

cls.solve()

# The status of the solution
print("Status:", LpStatus[cls.status])

# Each of the variables with it's resolved optimum value
for v in cls.variables():
    print(v.name, "=", v.varValue )

# The optimized objective function value
print("Total Cost = ",  value(cls.objective))


####################################
#      The second formulation
#####################################

#Create the 'clt' variable to contain the problem data
clt = LpProblem("Capacitated lot-sizing problem_f2", LpMinimize)

#two dictionaries called 'q,x' are created to contain the variables
q = LpVariable.dicts("q", (Periods , Periods), 0, None)
x = LpVariable.dicts("x", Periods, 0, 1, LpInteger)

#the objection function
clt += lpSum([lpSum([(Production_cost[i] + (lpSum([Storage_cost[p] for p in Periods[i - 1: t - 1]]))) * q[i][t] for i in Periods[0: t]]) for t in Periods]) + lpSum([Setup_cost[i] * x[i] for i in Periods])

#the constrains
for t in Periods:
    clt += lpSum([q[i][t] for i in Periods[0: t]]) == Demand[t]
    
for i in Periods:
    clt += lpSum([q[i][t] for t in Periods[i - 1: T]]) <= CAPACITY

for i in Periods:
    for t in Periods[i-1: T]:
        clt += q[i][t] <= Demand[t]*x[i]

clt.writeLP("Capacitated lot-sizing problem_f2.lp")

clt.solve()

# The status of the solution
print("Status:", LpStatus[clt.status]) 

# Each of the variables with it's resolved optimum value
for v in clt.variables():
    print(v.name, "=", v.varValue)

# The optimized objective function value
print("Total Cost = ", value(clt.objective))

