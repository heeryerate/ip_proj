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
    """
    :param line: line from input file
    :return: tuple like: (instance id, number of items, knapsack capacity,
                            list of tuples like: [(weight, cost), (weight, cost), ...])
    """
    parts = [int(value) for value in line.split()]
    inst_id, n, b = parts[0:3]
    a = [parts[i] for i in range(3, len(parts), 2)]
    c = [parts[i+1] for i in range(3, len(parts), 2)]
    return (inst_id, n, b, a, c)


def solver(inst_file_path, solution_file_path):
    inst_file = open(inst_file_path, "r")
    sol_file = open(solution_file_path, "w")

    avg = 0
    for line in inst_file:
        inst_id, n, b, a, c = parse_line(line)
        l = [0] *n
        u = [1] *n
        I = n
        P = range(0, n)
        N = range(0)


        (c, a, b, n, l, u, I, err) = Simplify_MIKP(c, a, b, n, l, u, I)
        #get best cost and variables combination
        avg += n
        
        #status = preprocessing(c, a, b, l, u, n)
        #print ("preprocessing" ,status)

        #print("Original", c, a, b, l, u, n, I)

        #(c, a, b, n, l, u, I, obj_change) = Simplify_MIKP(c, a, b, n, l, u, I)
        #print ("Simplify_MIKP", c, a, b, l, u, n, I, obj_change)

        # print "******Record those relaxed variables"
        # print "******Fix the order"
        # print "******Find out why and what if the lower bound is greater and equal to the upper bound"

        #(c, a, b, n, l, u, I) = Strength_bounds(c, a, b, n, l, u, I)
        #print "Strength_bounds"
        #print(c, a, b, l, u, n, I)

        #(c, a, b, n, l, u, I, obj_change_fix) = Fix_variables(c, a, b, n, l, u, I)
        #print "Fix_variables"
        #print(c, a, b, l, u, n, I, obj_change_fix)

        #(c, a, b, n, l, u, I, obj_change_com) = Complement_variables(c, a, b, n, l, u, I)
        #print "complement_variables"
        #print(c, a, b, l, u, n, I, obj_change_com)

        #branch_direction = "down"

        #(x, k, status, objective, activity) = LP_PP_MIKP(c, a, b, n, l, u, P, N)
        #print ("LP_PP_MIKP", x, k, status, objective, activity)

        #(x, k, objective, activity, status) = PhaseII(c, a, b, n, l, u, P, N, x, k, objective, activity)
        #print ("PhaseII", x, k, objective, activity, status)

        #(x, k, objective, activity, status) = Branching(c, a, b, n, l, u, P, N, x, k, objective, activity, branch_direction)
        #(x, k, objective, activity, status) = Branching(c, a, b, n, l, u, P, N, x, k, objective, activity, branch_direction)
        #if n != 0:
         #   (x, k, objective, activity, status) =  Branch(x, k, n, b, a, c, l, u, P, N, objective, activity, status)
          #   print (inst_id, x, k, objective, status)
        #print (inst_id, c, a, b, n, l, u)

        
        # write best result to file
        #sol_file.write("%s %s %s  %s\n" % (inst_id, n, objective, x))
        #sol_file.write("%s %s %s %s %s %s %s\n" % (inst_id, c, a, b, n, l, u))
    print avg
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


#en = float("-inf")
#ep = float("inf")
# 
# a = [14, 52, 81, 55, 99]
# c = [104, 222, 64, 29,22]
# b = 100
# n = 5
# l = [0,0,0,0,0]
# u = [1,1,1,1,1]
# I = 5
# P = range(0, 5)
# N = range(0)
