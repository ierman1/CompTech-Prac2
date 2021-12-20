# Practica 2

## Problema 2.1

# [2, -4, 1, 9, -6, 7, -3]

#We want our function to return those indices and the value of the sum.

### Divide and Conquer
def maxsum_subseq_dnc(lst, low = None, high = None):
    '''lst is a list of integers'''
    
    if low is None and high is None:
        low, high = 0, len(lst) - 1

    if high == low:
        return high, low, lst[0]

    mid = (low + high) // 2

    maxLeft = None
    maxRight = None

    '''
        Bucle para encontrar la max sum de la sublista de la izquierda, incluyendo el elemento del medio 
    '''
    tmp = 0
    startLeft = 0
    endLeft = 0
    acumulator = 0
    for i in range(mid, low - 1, -1):
        tmp += lst[i]
        acumulator += 1
        if maxLeft == None or tmp > maxLeft:
            startLeft = i
            acumulator = 0
            maxLeft = tmp

    endLeft = startLeft + acumulator

    '''
        Encuentra la max sum de la sublista de la derecha, excluyendo el elemendo del medio
    '''
    tmp = 0
    for i in range(mid + 1, high + 1):
        tmp += lst[i]
        if maxRight == None or tmp > maxRight:
            maxRight = tmp

    
    maxCrossing = max(maxsum_subseq_dnc(lst, low, mid), maxsum_subseq_dnc(lst, mid + 1, high))

    '''
        Devuelve el máximo de las tres secuencias
    '''
    return max(maxCrossing, maxLeft + maxRight)
        
### Dynamic Programming
def maxsum_subseq_dp(lst):
    '''lst is a list of integers'''
    
    sum = 0
    max = 0
    tmpStart = 0
    tmpEnd = 0
    start = 0
    end = 0
    
    '''
        Iteramos por la lista 'lst', en cada iteración sumamos el valor actual. Comprobamos si la suma  
        actual es positiva. 
        
        - En caso de serlo, comprobamos si la suma actual es más grande que el valor máximo
          hasta el momento para actualizarlo o no. Seguidamente actualizamos el valor end a la iteración actual. 
          Comprobamos si el valor temporal de principio es menor que el final, en caso de serlo los igualamos.
        
        - En caso de que la suma actual fuese negativa, reiniciamos el valor de suma y actualizamos el campo 
          start.
    '''

    for i in range(len(lst)):

        sum += lst[tmpStart]

        if sum < 0:
            sum = 0
            start = tmpStart + 1
            tmpStart = i + 1
            tmpEnd = len(lst)
        else:
            if sum > max:
                max = sum
                if tmpStart < tmpEnd:
                    tmpEnd = tmpStart
                end = i

            tmpStart += 1
    
    return start, end, max
    
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
    
    '''
        Iteramos por la lista de vertices y, por cada uno iteramos a través de una lista que va de 1 a X
        donde X = grado máximo del grafo. Este bucle representa los posibles colores que puede tener el 
        grafo, así que en cada iteración comprobaremos las adyacencias del vértice y sus colores. Si ninguna
        coincide se le puede asignar el color.
    '''
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

    '''
        Iteramos sobre una lista de visitados cuya longitud máxima es el número de vértices del
        grafo. En cada iteración tomamos como referéncia el último vértice en el trail y comprobamos sus
        adyacencias. La primera adyacencia no visitada que encontremos se añade al trail y a la lista
        de visitados y se le asigna un color que no sea usado por ninguna de sus adyacencias. En caso
        de no encontrar un color válido la función devuelve un diccionario vacío.
    '''
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


print(maxsum_subseq_dp([2, 2, 1, -9, -7, 7, -3]))
print(maxsum_subseq_dp([2, -4, 1, 9, -6, 7, -3]))
print(maxsum_subseq_dnc([2, -4, 1, 9, -6, 7, -3]))
print(coloring_greedy(Graph([(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)])))
print(coloring_backtrack(Graph([(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]), 2))
print(coloring_backtrack(Graph([(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]), 4))
print(coloring_backtrack(Graph([(1, 5), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4), (1, 6)]), 4))