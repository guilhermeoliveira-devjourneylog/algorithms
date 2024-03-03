# graph_for_the_all_pairs_shortest_path
from colorama import Fore, Style
import numpy as np
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
    Reads a file representing a graph and returns an adjacency matrix.
    
    Args:
        file_path (str): The path to the file representing the graph.

    Returns:
        graph (list of list of int): The adjacency matrix of the graph.
    """
    logging.info(f"{Fore.GREEN}Reading graph from file: {file_path}{Style.RESET_ALL}")
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_vertices, num_edges = map(int, lines[0].split())
        graph = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        for vertex_index in range(num_vertices):
            graph[vertex_index][vertex_index] = 0
        for line in lines[1:]:
            start_vertex, end_vertex, edge_weight = map(int, line.split())
            graph[start_vertex-1][end_vertex-1] = edge_weight
    logging.info(f"Finished reading graph from file: {file_path}")
    return graph

def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm to find the shortest distance between all pairs of vertices.

    Args:
        graph (list of list of int): The adjacency matrix of the graph.

    Returns:
        distance_matrix (np.array): The matrix of distances between all pairs of vertices.
    """
    logging.info(f"{Fore.GREEN}Starting optimized Floyd-Warshall algorithm.{Style.RESET_ALL}")

    # Number of vertices in the graph. The distance matrix will be a square matrix of this size.
    num_vertices = len(graph)
    
    # Convert the graph's adjacency matrix to a NumPy array for efficient operations.
    distance_matrix = np.array(graph)

    # Start updating the distance matrix using the optimized Floyd-Warshall algorithm.
    for intermediate_vertex_index in range(num_vertices):
        logging.debug(f"Processing intermediate vertex {intermediate_vertex_index+1}/{num_vertices}.")

        # Vectorized operation to update the distance matrix.
        # This line calculates, for each pair of vertices (i, j), the lesser of the current distance and
        # the distance passing through the intermediate vertex indexed by `intermediate_vertex_index`.
        distance_matrix = np.minimum(distance_matrix, distance_matrix[:, intermediate_vertex_index][:, np.newaxis] + distance_matrix[intermediate_vertex_index, :])

    logging.info(f"{Fore.GREEN}Optimized Floyd-Warshall algorithm completed successfully.{Style.RESET_ALL}")

    # The updated distance matrix is returned. It contains the shortest distances between all pairs of vertices.
    return distance_matrix

def check_for_negative_cycle(distance_matrix):
    """
    Checks if there is a negative cycle in the graph.

    Args:
        distance_matrix (np.array): The matrix of distances between all pairs of vertices.

    Returns:
        bool: True if there is a negative cycle, False otherwise.
    """
    logging.info(f"{Fore.GREEN}Checking for negative cycle{Style.RESET_ALL}")
    num_vertices = distance_matrix.shape[0] 
    for vertex_index in range(num_vertices):
        if distance_matrix[vertex_index, vertex_index] < 0: 
            logging.warning(f"Negative cycle found at vertex {vertex_index}")
            return True
    logging.info("No negative cycle found")
    return False


def run():
    """
    Main function that coordinates the whole process. It asks the user to input the paths of the files representing the graphs.
    For each file, it reads the graph, calculates the distance matrix using the Floyd-Warshall algorithm, checks if there is a negative cycle and, if not, finds the shortest path in the graph.
    It repeats this process for all files and, in the end, prints the shortest path among all the shortest paths found.
    """
    file_paths = []
    shortest_paths = []  
    while True:
        file_path = input("Enter a file path for read (or 'done' to finish): ").strip().lower() 
        if file_path == 'done':
            break
        file_paths.append(file_path)
    for file_path in file_paths:
        try:
            logging.info(f"Processing file: {file_path}")
            graph = read_graph_from_file(file_path)
            dist = floyd_warshall(graph)
            if check_for_negative_cycle(dist):
                logging.info(f"{Fore.YELLOW}Graph in {file_path} has a negative-cost cycle.{Style.RESET_ALL}")
            else:
                shortest_path = min(min(row) for row in dist)
                shortest_paths.append(shortest_path)
        except Exception as e:
            logging.exception(f"{Fore.RED}An error occurred while processing {file_path}: {e}{Style.RESET_ALL}")
    if shortest_paths:
        shortest_of_shortest_paths = min(shortest_paths)
        logging.info(f"{Fore.GREEN}The shortest of the shortest paths is: {shortest_of_shortest_paths}{Style.RESET_ALL}")
    else:
        logging.info(f"{Fore.RED}All graphs have a negative-cost cycle or an error occurred.{Style.RESET_ALL}")

if __name__ == "__main__":
    run()
