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



def max_degree(graph):
    max = 0
    for i in range(graph.nverts):
        new = len(graph.get(i))
        if  new > max:
            max = new

    return max

### Greedy
def coloring_greedy(graph):
    '''graph is an instance of class Graph'''
    
    result = {}
    maxDegree = max_degree(graph)
    
    for i in range(graph.nverts):
        for c in range(1, maxDegree + 1):
            found = False
            for a in graph.get(i):
                if a in result and result[a] == c:
                    found = True
                    break
            if not found:
                result[i] = c
                break

    return result
        
def is_safe(color, adj, visited, assignements):
    for a in adj:
        if a in visited and assignements[a] == color:
            return False

    return True

### Backtrack
def coloring_backtrack(graph, n):
    '''graph is an instance of class Graph, n is the maximum number of colors to be used'''
    
    visited = [0]
    trail = [0]
    res = { 0: 1 }

    while len(visited) != graph.nverts:
        tmp = trail[-1]
        found = False

        for v in graph.get(tmp):
            if v not in visited:
                visited.append(v)
                trail.append(v)
                found = True

                for c in range(1, n + 1):
                    if is_safe(c, graph.get(v), visited, res):
                        res[v] = c
                        break

                if not v in res:
                    return {}

                break

        if not found:
            trail = trail[:-1]

    return res

#lst = [2, -4, 1, 9, -6, 7, -3]
#print(maxsum_subseq_dnc(lst))

print(coloring_greedy(Graph([(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)])))
print(coloring_backtrack(Graph([(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]), 2))
print(coloring_backtrack(Graph([(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]), 4))
print(coloring_backtrack(Graph([(1, 5), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4), (1, 6)]), 4))