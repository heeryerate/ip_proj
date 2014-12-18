from prime_phase_II import PhaseII
from dual_Phase_II import dualPhaseII
from pro import *

class Queue(object):
    def __init__(self):
        self.buffer = deque()
        
    def push(self, value):
        self.buffer.appendleft(value)
        
    def pop(self):
        return self.buffer.pop()
    
    def __len__(self):
        return len(self.buffer)


class Node(object):
    def __init__(self, level, in_bag, cost, weight, bound):
        self.level = level
        self.in_bag = in_bag
        self.cost = cost
        self.weight = weight
        self.bound = bound
        
def Branch(x, k, n, b, a, c, l, u, P, N, objective, activity, status): 
    queue = Queue()

    #sorted ratios order by benefit/cost
    ratios = [(i, c[i] / float(a[i])) for i in range(n)]
    
    now_best = Node(0, [], 0.0, 0.0, 0.0) # best_so_far
    
    if now_best.weight >= b:
        print "infeasible solution"
        return 0
            
    get_bound(now_best, n, b, a, c, ratios)    

    try_this = Node(0, [], 0.0, 0.0, now_best.bound)
    
    queue.push(try_this)
    
    while len(queue) > 1:
        current_node = queue.pop()
        if current_node.bound > now_best.cost:
            cur_no = ratios[current_node.level][0]
            next_cost = c[cur_no]
            next_weight = a[cur_no]
            activity = Node(current_node.level + 1, current_node.in_bag + [cur_no],
                current_node.cost + next_cost, current_node.weight + next_weight, current_node.bound)
                
            if activity.weight <= b:
                (x, k, queue, now_best, status) = PhaseII(c, a, b, n, l, u, P, N, x, k, queue, objective, activity, now_best, status)
                        
            not_add = Node(current_node.level + 1, current_node.in_bag, current_node.cost,
                                current_node.weight, current_node.bound)
            not_add.bound = get_bound(not_add, n, b, a, c, ratios)    
            if not_add.bound > now_best.cost:
                (x, k, objective, activity, status) = dualPhaseII(c, a, b, n, l, u, P, N, x, k ,queue, objective, not_add, status)
                    
    objective = int(now_best.cost)
    x = now_best.in_bag
    status = "optimal solution"
    return (x, k, objective, ratios, status)
        
        

