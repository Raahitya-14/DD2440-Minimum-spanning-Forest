#!/usr/bin/env python3

import math
import sys
import random
from queue import Queue
 
def msf_approx(w, n, q): 
    random.seed()
    cc_sum = 0
    for i in range(1, w):
        cc_sum += cc_approx(i, w, n, q)
    trees = cc_approx(w, w, n, q) # if we think of trees as connected components, they should be estimated by cc_approx for max weight. 
    if trees < 1:
        trees = 1
    return  n - (w*trees) + cc_sum # remove the max weight for each maximal non-connected component (tree)


def cc_approx(currentW, w, n, q):
    b_sum = 0
    lim = 1
    if w > 0:
        lim = math.ceil(float(q)/w) # this will lead to each cc_approx requesting at least q/maxWeight nodes, so it will exceed the node limit since bfs will be done on all of the q nodes

    for i in range(0, lim):
        x = math.floor(1.0/random.random())
        if x > 50:
            x = 50
        b_sum += bfs(random.randint(0, n-1), currentW, x)
    
    return (float(n)/(lim))*b_sum

# searches neighbours to node with weight w or less until none are left (return 1)
# or x nodes have been searched (return 0)
def bfs(root, w, x):
    node_queue = Queue()
    node_queue.put_nowait(root)
    seen_nodes = [root]
    node_count = 0

    while (not node_queue.empty()) and (node_count < x):
        n = node_queue.get_nowait()
        node_count += 1

        neighbours = get_neighbours(n)

        for node in neighbours: # add neigbours of n with weight <= w into node_queue if neigbour is not in seen_nodes
            if (node[1] <= w) and (node[0] not in seen_nodes):
                seen_nodes.append(node[0])
                node_queue.put_nowait(node[0])
        
    if(node_queue.empty()):
        return 1
    else:
        return 0

def get_neighbours(node):
    print(node)
    sys.stdout.flush()
    line = sys.stdin.readline().split()
    return [ (int(line[i]), int(line[i+1])) for i in range(1, len(line), 2)]


def main():
    n = int(sys.stdin.readline().strip())
    w = int(sys.stdin.readline().strip())
    q = int(sys.stdin.readline().strip())
    if n == 2:
        msf_value = w
    else:
        msf_value = msf_approx(w, n, q)
    sys.stdout.write("end {:.2f}\n".format(msf_value))
    sys.stdout.flush()

if __name__ == "__main__":
    main()