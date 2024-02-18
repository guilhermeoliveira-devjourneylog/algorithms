from colorama import Fore, Style
import random
import copy

def contract_vertices(graph, vertex1, vertex2):
    """Merge or "contract" the vertices vertex1 and vertex2."""
    for node in graph[vertex2]:
        if node != vertex1:
            graph[vertex1].append(node)
        graph[node].remove(vertex2)
        if node != vertex1:
            graph[node].append(vertex1)
    del graph[vertex2]
    print(f'{Fore.YELLOW}Contracting vertices {vertex1} and {vertex2}{Style.RESET_ALL}')


def perform_randomized_contraction(graph):
    """Perform the randomized contraction algorithm until only 2 vertices remain."""
    while len(graph) > 2:
        vertex1 = random.choice(list(graph.keys()))
        vertex2 = random.choice(graph[vertex1])
        contract_vertices(graph, vertex1, vertex2)
    return len(graph[list(graph.keys())[0]])

def read_graph(file_path):
    """Read a graph from a file. The first part of each line is the vertex, the rest are its neighbors."""
    graph = {}
    with open(file_path) as file:
        for line in file:
            parts = [int(i) for i in line.split()]
            graph[parts[0]] = parts[1:]
    print(f'{Fore.CYAN}Graph read from file {file_path} with {len(graph)} vertices{Style.RESET_ALL}')
    return graph

def find_minimum_cut(graph):
    """Find the minimum cut of a graph using the randomized contraction algorithm."""
    min_cut = float('inf')
    num_iterations = 1000  
    for i in range(num_iterations):
        print(f'Starting iteration {i+1} of {num_iterations}')
        copied_graph = copy.deepcopy(graph)
        cut = perform_randomized_contraction(copied_graph)
        min_cut = min(min_cut, cut)
        print(f'{Fore.BLUE}Minimum cut found so far: {min_cut}{Style.RESET_ALL}')
    return min_cut

def main():
    file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\karger-min-cut.txt'
    graph = read_graph(file_path)
    print(f'{Fore.RED}Minimum cut: {find_minimum_cut(graph)}{Style.RESET_ALL}')
    print(f'{Fore.GREEN}End of the script{Style.RESET_ALL}')

if __name__ == "__main__":
    main()
