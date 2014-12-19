import argparse
from time import time
from preprocessing import preprocessing
from reformulation import LP_PP_MIKP
from prime_phase_II import PhaseII
from dual_Phase_II import dualPhaseII
from Branching import Branch
from pro import *
from domination import *

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
        l = [0] *n
        u = [1] *n
        I = n
        P = range(0, n)
        N = range(0)

        #print("Original", c, a, b, l, u, n, I)
        
        #status = preprocessing(c, a, b, l, u, n)
        #print ("preprocessing" ,status)   

        #(c, a, b, n, l, u, I, obj_change) = Simplify_MIKP(c, a, b, n, l, u, I)
        #print ("Simplify_MIKP", c, a, b, l, u, n, I, obj_change)

        #(c, a, b, n, l, u, I) = Strength_bounds(c, a, b, n, l, u, I)
        #print ("Strength_bounds", c, a, b, l, u, n, I)

        #(c, a, b, n, l, u, I, obj_change_fix) = Fix_variables(c, a, b, n, l, u, I)
        #print ("Fix_variables", c, a, b, l, u, n, I, obj_change_fix)

        #(c, a, b, n, l, u, I, obj_change_com) = Complement_variables(c, a, b, n, l, u, I)
        #print ("complement_variables", c, a, b, l, u, n, I, obj_change_com)

        (x, k, status, objective, activity) = LP_PP_MIKP(c, a, b, n, l, u, P, N)
        #print ("LP_PP_MIKP", x, k, status, objective, activity)

        #(x, k, objective, activity, status) = PhaseII(c, a, b, n, l, u, P, N, x, k, objective, activity)
        #print ("PhaseII", x, k, objective, activity, status)

        (x, k, objective, activity, status) =  Branch(x, k, n, b, a, c, l, u, P, N, objective, activity, status)
        print (inst_id, x, k, objective, status)
        #print (inst_id, c, a, b, n, l, u)

        # write result to file
        #sol_file.write("%s %s %s  %s\n" % (inst_id, n, objective, x))

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
    print (solving_time, "TIME FOR MAIN")
