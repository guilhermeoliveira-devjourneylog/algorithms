# dijkstra.py
from colorama import Fore, Style
from igraph import Graph, plot
import heapq
import sys
import os

# Get the absolute directory of the currently running script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Join the script's directory with the parent directory (os.pardir), creating a path to the project's root directory
project_root = os.path.join(script_dir, os.pardir)

# Add the project's root directory to Python's sys.path, allowing modules in this directory to be imported as packages
sys.path.append(os.path.abspath(project_root))
from utils.log_config import configure_logging
import logging

configure_logging()
    
def read_graph_from_file(file_path):
    """
    Reads a graph from a file.

    This function reads a text file that represents a graph. Each line in the file represents a vertex and its edges.
    The first part of each line is the vertex and the subsequent parts are the edges for that vertex, where each edge is represented by a neighbor,weight pair separated by a comma.
    For example, the line "1   2,1   3,2" represents a vertex 1 that has an edge to vertex 2 with weight 1 and an edge to vertex 3 with weight 2.

    Args:
        file_path (str): The path to the file containing the graph.

    Returns:
        dict: A dictionary representing the graph. Each key is a vertex and the corresponding value is another dictionary.
              The inner dictionary maps neighboring vertices to the weights of the edges connecting them to the key vertex.
              For example, if the input graph is {1: {2: 1, 3: 2}, 2: {1: 1, 3: 1}, 3: {1: 2, 2: 1}}, this represents a graph with three vertices and three edges.
              There is an edge with weight 1 between vertices 1 and 2, an edge with weight 2 between vertices 1 and 3, and an edge with weight 1 between vertices 2 and 3.
    """
    logging.info(Fore.GREEN + "Reading graph from file." + Style.RESET_ALL)
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')  
            vertex = int(parts[0])
            edges = {}
            for edge in parts[1:]:
                neighbor, weight = map(int, edge.split(','))  # Separates the neighbor from the weight.
                edges[neighbor] = weight
            graph[vertex] = edges
    logging.info(Fore.GREEN + "Finished reading graph from file." + Style.RESET_ALL)
    logging.info(Fore.BLUE + f"Graph: {graph}" + Style.RESET_ALL)
    return graph


def dijkstra(graph, start_vertex=1):
    """
    Runs the Dijkstra's algorithm on a graph.

    This function uses Dijkstra's algorithm to find the shortest path from a starting vertex to all other vertices in a graph.
    The graph is represented as a dictionary where each key is a vertex and the corresponding value is another dictionary.
    The inner dictionary maps neighboring vertices to the weights of the edges connecting them to the key vertex.

    Args:
        graph (dict): The graph on which to run the algorithm. 
                      For example, if the input graph is {1: {2: 1, 3: 2}, 2: {1: 1, 3: 1}, 3: {1: 2, 2: 1}}, 
                      this represents a graph with three vertices and three edges.
                      There is an edge with weight 1 between vertices 1 and 2, an edge with weight 2 between vertices 1 and 3, 
                      and an edge with weight 1 between vertices 2 and 3.
        start_vertex (int, optional): The starting vertex for the algorithm. Defaults to 1.

    Returns:
        dict: A dictionary mapping each vertex to the shortest distance from the starting vertex. 
              For example, if the starting vertex is 1, the output might be {1: 0, 2: 1, 3: 2}, 
              indicating that the shortest distance from vertex 1 to vertex 1 is 0, the shortest distance from vertex 1 to vertex 2 is 1, 
              and the shortest distance from vertex 1 to vertex 3 is 2.
    """
    logging.info(Fore.GREEN + "Running Dijkstra's algorithm." + Style.RESET_ALL)
    D = {v: float('inf') for v in graph}  
    D[start_vertex] = 0  

    queue = [(0, start_vertex)]  
    
    visited = set()  

    while queue:
        d, v = heapq.heappop(queue)
        if v in visited:
            continue  
        visited.add(v)  

        for neighbor, length in graph[v].items():
            if neighbor not in D:
                logging.error(f"Neighbor {neighbor} not found in distances dictionary. Possible missing vertex or incorrect input data.")
                continue
            old_distance = D[neighbor]
            new_distance = D[v] + length
            if new_distance < old_distance:
                D[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    logging.info(Fore.GREEN + "Finished running Dijkstra's algorithm." + Style.RESET_ALL)
    logging.info(Fore.BLUE + f"Distances: {D}" + Style.RESET_ALL)
    return D

def visualize_graph(graph):
    """
    Visualizes a graph using the igraph library.

    This function creates a Graph object, adds vertices and edges to it based on the input graph, and then plots the graph.
    The graph is saved as an image in the "igraph" subdirectory of the script's directory.

    Args:
        graph (dict): The graph to be visualized. This should be a dictionary where each key is a vertex and the corresponding value is another dictionary.
                      The inner dictionary should map neighboring vertices to the weights of the edges connecting them to the key vertex.

    Example:
        If the input graph is {1: {2: 1, 3: 2}, 2: {1: 1, 3: 1}, 3: {1: 2, 2: 1}}, this represents a graph with three vertices and three edges.
        There is an edge with weight 1 between vertices 1 and 2, an edge with weight 2 between vertices 1 and 3, and an edge with weight 1 between vertices 2 and 3.
    """
    logging.info("Visualizing graph.")
    g = Graph(directed=False)
    for vertex in graph:
        g.add_vertex(str(vertex))
    for vertex, edges in graph.items():
        for edge, weight in edges.items():
            if str(vertex) in g.vs["name"] and str(edge) in g.vs["name"]:
                g.add_edge(str(vertex), str(edge), weight=weight)

    image_path = os.path.join(script_dir, "igraph", "graph-dijkstra.png")
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    plot(g, target=image_path)
    logging.info(f"Finished visualizing graph. Image saved to {image_path}")
    
def get_specific_distances(distances, vertices):
    """
    Gets the distances for specific vertices.

    Args:
        distances (dict): A dictionary mapping vertices to distances.
        vertices (list): A list of vertices for which to get distances.

    Returns:
        str: A string containing the distances for the specified vertices, separated by commas.
    """
    return ','.join(str(distances.get(vertex, 1000000)) for vertex in vertices)
   
def run():
    try:
        logging.info(Fore.GREEN + "Starting the program." + Style.RESET_ALL)
         # file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\test-graph-dijkstra.txt'
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\graph-dijkstra.txt'
        graph = read_graph_from_file(file_path)
        distances = dijkstra(graph)
        logging.info(Fore.BLUE + "Distances from start vertex: {distances}" + Style.RESET_ALL)
        
        specific_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        distances_string = get_specific_distances(distances, specific_vertices)
        
        print("Specific distances:", distances_string)
        
        visualize_graph(graph)

    except Exception as e:
        logging.exception(Fore.RED + "An error occurred during the execution." + Style.RESET_ALL)
        
if __name__ == "__main__":
    run()
