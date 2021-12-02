# Practica 2

## Problema 2.1

# [2, -4, 1, 9, -6, 7, -3]

#We want our function to return those indices and the value of the sum.

def partition(lst):
    half = len(lst) // 2
    return lst[0 : half], lst[1, -2], lst[half + 1 : -1]

### Divide and Conquer
def maxsum_subseq_dnc(lst, low = None, high = None):
    '''lst is a list of integers'''
    
    if low is None and high is None:
        low, high = 0, len(lst) - 1

    if high == low:
        return lst[0]

    mid = (low + high) // 2

    maxLeft = None
    maxRight = None

    '''
        Trobar la max sublist de l'esquerra, incloent l'element del mig
    '''
    tmp = 0
    for i in range(mid, low - 1, -1):
        tmp += lst[i]
        if maxLeft == None or tmp > maxLeft:
            maxLeft = tmp

    '''
        Trobar la max sum de la sublist de la dreta, excloent l'element del mig 
    '''
    tmp = 0
    for i in range(mid + 1, high + 1):
        tmp += lst[i]
        if maxRight == None or tmp > maxRight:
            maxRight = tmp

    maxCrossing = max(maxsum_subseq_dnc(lst, low, mid), maxsum_subseq_dnc(lst, mid + 1, high))

    '''
        Retorna el màxim de les tres sequències
    '''
    return max(maxCrossing, maxLeft + maxRight)
        
### Dynamic Programming
def maxsum_subseq_dp(lst):
    '''lst is a list of integers'''
    #TODO
    pass

##Problema 2.2

class Graph:
    def __init__(self, edge_list):
        self.nverts = max(map(max, edge_list)) + 1

        self._adjacent = dict(map(lambda x: (x, set()), range(self.nverts)))
        for v_a, v_b in edge_list:
            self._adjacent[v_a].add(v_b)
            self._adjacent[v_b].add(v_a)

    def get(self, x):
        if x < self.nverts:
            return list(self._adjacent[x])
        else:
            raise AttributeError(f'Value {x} is not a vertex in this graph.')


### Greedy
def coloring_greedy(graph):
    '''graph is an instance of class Graph'''
    
    result = {}
    

    pass
        
def is_safe(vertex):
    pass

### Backtrack
def coloring_backtrack(graph, n):
    '''graph is an instance of class Graph, n is the maximum number of colors to be used'''
    
    maxColor = 1
    result = { 0: maxColor }
    visited = []
    queue = []

    queue.append(0)
    visited.append(0)

    while len(queue) != 0:

        tmp = queue.pop(0)

        for v in graph.get(tmp):
            visited.append(v)
            queue.append(v)

            if is_safe(v):
                maxColor = result[tmp] + 1
            else:
                maxColor += 1
            
            result[v] = maxColor

            

                




    pass

'''
If all colors are assigned,
    print vertex assigned colors
Else
    a. Trying all possible colors, assign a color to the vertex
    b. If color assignment is possible, recursivelty assign colors to next vertices
    c. If color assignment is not possible, de-assign color, return False
'''
    

lst = [2, -4, 1, 9, -6, 7, -3]
print(maxsum_subseq_dnc(lst))

print(coloring_greedy(Graph([(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)])))
print(coloring_backtrack(Graph([(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]), 2))