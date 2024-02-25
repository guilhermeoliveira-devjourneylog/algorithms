# kruskal.py
from colorama import Fore, Style
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

# Configure logging for the application
configure_logging()

def read_graph_from_file(file_path):
    """
    Reads a graph from a file. The graph is represented as a list of edges with weights.
    Each line in the file represents an edge in the format: node1 node2 weight
    """
    logging.info(Fore.BLUE + "Reading graph from file..." + Style.RESET_ALL)
    edge_list = []
    with open(file_path, 'r') as file:
        total_nodes = int(next(file))
        for line in file:
            node1, node2, edge_weight = map(int, line.strip().split())
            edge_list.append((node1 - 1, node2 - 1, edge_weight))  # Subtract 1 from node1 and node2
    logging.info(Fore.GREEN + "Graph read successfully." + Style.RESET_ALL)
    return total_nodes, edge_list

class DisjointSetUnion:
    """
    A class to represent a disjoint set union. It supports operations like finding the set a node belongs to
    and merging two sets.
    """
    def __init__(self, total_nodes):
        self.parent = list(range(total_nodes))
        self.rank = [0] * total_nodes

    def find_set(self, node):
        """
        Finds the representative of the set that the node belongs to.
        """
        if self.parent[node] != node:
            self.parent[node] = self.find_set(self.parent[node])
        return self.parent[node]

    def union_sets(self, node1, node2):
        """
        Merges the sets that node1 and node2 belong to.
        """
        root1 = self.find_set(node1)
        root2 = self.find_set(node2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root1] += 1

def kruskal(edge_list, total_nodes, total_clusters):
    """
    Implements Kruskal's algorithm to find the minimum spanning tree of a graph.
    """
    disjoint_set = DisjointSetUnion(total_nodes)
    cluster_count = total_nodes  
    sorted_edges = sorted(edge_list, key=lambda edge: edge[2])

    for edge in sorted_edges:
        node1, node2, edge_weight = edge
        if disjoint_set.find_set(node1) != disjoint_set.find_set(node2):
            if cluster_count == total_clusters:  
                return edge_weight
            disjoint_set.union_sets(node1, node2)
            cluster_count -= 1  

    return 0  # Return 0 if no such edge is found

def run():
    """
    Main function to run the program. It reads a graph from a file, finds its minimum spanning tree using Kruskal's' algorithm,
    and prints the result.
    """
    try:
        logging.info(Fore.GREEN + "Starting the program." + Style.RESET_ALL)
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\graph-clustering.txt'
        total_clusters = 4  
        total_nodes, edge_list = read_graph_from_file(file_path)
        result = kruskal(edge_list, total_nodes, total_clusters)
        logging.info(Fore.GREEN + f"Kruskal's algorithm result: {result}" + Style.RESET_ALL)

    except Exception as e:
        logging.exception(Fore.RED + "An error occurred during the execution." + Style.RESET_ALL)

if __name__ == "__main__":
    run()