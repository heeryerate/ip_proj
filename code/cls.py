from pulp import *
import argparse
from time import time

def parse_line(line):
    parts = [int(value) for value in line.split()]
    inst_id, n, b = parts[0:3]
    a = [parts[i] for i in range(3, len(parts), 2)]
    c = [parts[i+1] for i in range(3, len(parts), 2)]
    return (inst_id, n, b, a, c)


def solver(inst_file_path, solution_file_path):
    inst_file = open(inst_file_path, "r")
    sol_file = open(solution_file_path, "w")

    for line in inst_file:
        inst_id, n, b, a, c = parse_line(line)

	N = range(n)
	
	clt = LpProblem("Knapsack", LpMaximize)
	x = LpVariable.dicts("x", N, 0, 1, LpInteger)
	
	clt += lpSum(c[i] * x[i] for i in N)
        clt += lpSum(a[i] * x[i] for i in N) <= b
   		
	clt.solve()

	i = 0
	y = range(n)
	for v in clt.variables():
	    y[i] = v.varValue
    	    i += 1
	
	print(inst_id, n, value(clt.objective), y, LpStatus[clt.status])

        
        sol_file.write("%s %s %s  %s\n" % (inst_id, n, clt.objective, x))

    inst_file.close()
    sol_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script solving the 0/1 knapsack problem')
    parser.add_argument('-f', '--inst-file', required=True, type=str, dest="inst_file_path", 
                        help='Path to inst *.dat file')
    parser.add_argument('-o', type=str, dest="solution_file_path", default="knap_4.sol.dat",
                        help='Path to file where solutions will be saved. Default value: output.sol.dat')
    args = parser.parse_args()

    solving_time = 0
    t_start = time()
    solver(args.inst_file_path, args.solution_file_path)
    t_finish = time()
    solving_time += (t_finish - t_start)
    print (solving_time, "TIME FOR CLS")
