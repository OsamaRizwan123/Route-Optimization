from sys import maxsize
from itertools import permutations

# Number of vertices in the graph
V = 14

# Implementation of the Traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # Store all vertices apart from the source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # Store the minimum weight Hamiltonian Cycle
    min_path = maxsize
    
    # Generate all permutations of the vertices
    next_permutation = permutations(vertex)

    # Iterate through each permutation
    for i in next_permutation:
        # Store current path weight (cost)
        current_pathweight = 0

        # Compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]  # Return to the start

        # Update the minimum path weight
        min_path = min(min_path, current_pathweight)

    return min_path

# Driver Code
if __name__ == "__main__":
    # Matrix representation of the graph
    graph = [
        [0, 0.8, 5.8, 1.9, 0.65, 6.6, 1.4, 1.7, 2.2, 6.5, 1.8, 1.6, 1.3, 1.3],
        [0.8, 0, 5.7, 1.3, 0.9, 7, 0.75, 0.95, 1.4, 6.9, 3.2, 2, 1.9, 1.7],
        [5.8, 5.7, 0, 7, 4.6, 0.85, 6.7, 7, 6.9, 0.7, 3.5, 6.4, 6.5, 4.3],
        [1.9, 1.3, 7, 0, 2.7, 6, 0.75, 0.75, 0.25, 5.9, 2.1, 4.7, 3.6, 2.2],
        [0.65, 0.9, 4.6, 2.7, 0, 6.5, 1.6, 2, 2.4, 6.4, 1.3, 1.6, 2.1, 0.85],
        [6.6, 7, 0.85, 6, 6.5, 0, 7.5, 7.8, 7.7, 0.45, 4.3, 7.2, 7.4, 7],
        [1.4, 0.75, 6.7, 0.75, 1.6, 7.5, 0, 0.18, 1, 6.5, 3.7, 3.2, 2.6, 2.4],
        [1.7, 0.95, 7, 0.75, 2, 7.8, 0.18, 0, 1, 6.7, 3.8, 2.9, 2.9, 3.4],
        [2.2, 1.4, 6.9, 0.25, 2.4, 7.7, 1, 1, 0, 5.6, 1.8, 3.3, 3.4, 2],
        [6.5, 6.9, 0.7, 5.9, 6.4, 0.45, 6.5, 6.7, 5.6, 0, 5.2, 7, 7.2, 6.9],
        [1.8, 3.2, 3.5, 2.1, 1.3, 4.3, 3.7, 3.8, 1.8, 5.2, 0, 3, 3.7, 0.95],
        [1.6, 2, 6.4, 4.7, 1.6, 7.2, 3.2, 2.9, 3.3, 7, 3, 0, 1.9, 1.8],
        [1.3, 1.9, 6.5, 3.6, 2.1, 7.4, 2.6, 2.9, 3.4, 7.2, 3.7, 1.9, 0, 2.6],
        [1.3, 1.7, 4.3, 2.2, 0.85, 7, 2.4, 3.4, 2, 6.9, 0.95, 1.8, 2.6, 0]
    ]

    # Starting vertex
    s = 0

    # Print the result
    print("The minimum cost of the Hamiltonian cycle is:", travellingSalesmanProblem(graph, s))