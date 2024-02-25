# kruskal_hash.py
from colorama import Fore, Style
import sys
import os

# Get the absolute directory of the currently running script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Join the script's directory with the parent directory (os.pardir), creating a path to the project's root directory
root_dir = os.path.join(script_dir, os.pardir)

# Add the project's root directory to Python's sys.path, allowing modules in this directory to be imported as packages
sys.path.append(os.path.abspath(root_dir))
from utils.log_config import configure_logging
import logging

# Configure logging for the application
configure_logging()

def read_graph_from_file(file_name):
    """
    Reads a graph from a file and returns a set of nodes and the number of bits per node.

    Parameters:
    file_name (str): The name of the file to read from.

    Returns:
    nodes (set): A set of nodes read from the file.
    bits (int): The number of bits per node.
    """
    logging.info(Fore.BLUE + f"Reading graph from file {file_name}..." + Style.RESET_ALL)
    nodes = set() 
    with open(file_name, 'r') as file:
        node_count, bits = map(int, next(file).strip().split())
        logging.info(Fore.BLUE + f"Number of nodes: {node_count}, Number of bits per node: {bits}" + Style.RESET_ALL)
      
        for line in file:
            node = int(line.replace(' ', '').strip(), 2)
            nodes.add(node)  
    logging.info(Fore.GREEN + f"Graph read successfully. Total nodes read: {len(nodes)}" + Style.RESET_ALL)
    return nodes, bits

class DisjointSet:
    """
    A class to represent a Disjoint Set data structure.

    ...

    Attributes:
    parent (list): A list where the index represents a node and the value represents the parent of the node.
    rank (list): A list where the index represents a node and the value represents the rank of the node.
    set_count (int): The number of disjoint sets.

    Methods:
    find_set(node): Finds the representative of the set that node belongs to.
    merge_sets(node1, node2): Merges the two sets that node1 and node2 belong to.
    """
    def __init__(self, node_count):
        self.parent = list(range(node_count))
        self.rank = [0] * node_count
        self.set_count = node_count  

    def find_set(self, node):
        """
        Finds the representative of the set that node belongs to.

        Parameters:
        node (int): The node to find the representative for.

        Returns:
        int: The representative of the set that node belongs to.
        """
        if self.parent[node] != node:
            self.parent[node] = self.find_set(self.parent[node])
        return self.parent[node]

    def merge_sets(self, node1, node2):
        """
        Merges the two sets that node1 and node2 belong to.

        Parameters:
        node1 (int): A node in the first set to merge.
        node2 (int): A node in the second set to merge.
        """
        root1 = self.find_set(node1)
        root2 = self.find_set(node2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                root1, root2 = root2, root1
            self.parent[root2] = root1
            if self.rank[root1] == self.rank[root2]:
                self.rank[root1] += 1
            self.set_count -= 1 

def generate_masks(bit_count, dist):
    """
    Generates bit masks for a given number of bits and distance.

    Parameters:
    bit_count (int): The number of bits.
    dist (int): The distance.

    Returns:
    masks (list): A list of bit masks.
    """
    masks = []
    for i in range(bit_count):
        masks.append(1 << i)
    if dist == 2:
        for i in range(bit_count):
            for j in range(i + 1, bit_count):
                masks.append((1 << i) | (1 << j))
    return masks

def kruskal_hash(nodes, bit_count):
    """
    Runs the optimized Kruskal's hash algorithm on a set of nodes.

    Parameters:
    nodes (set): A set of nodes.
    bit_count (int): The number of bits per node.

    Returns:
    clusters (int): The number of clusters with spacing at least 3.
    """
    logging.info(Fore.BLUE + "Running optimized Kruskal's hash algorithm..." + Style.RESET_ALL)
    node_count = len(nodes)
    disjoint_set = DisjointSet(node_count)
    node_table = {node: i for i, node in enumerate(nodes)}
    
    masks = generate_masks(bit_count, 1) + generate_masks(bit_count, 2)
    logging.info(Fore.BLUE + f"Generated {len(masks)} bit masks." + Style.RESET_ALL)

    for i, node in enumerate(nodes):
        for mask in masks:  # Use the pre-calculated bit masks
            neighbor = node ^ mask
            if neighbor in node_table:
                disjoint_set.merge_sets(i, node_table[neighbor])

    clusters = disjoint_set.set_count  # Use the counter in the DisjointSet class
    logging.info(Fore.GREEN + f"Optimized Kruskal's hash algorithm completed. Number of clusters with spacing at least 3: {clusters}" + Style.RESET_ALL)
    return clusters

def run():
    """
    Main function to run the program. It reads a graph from a file, finds its minimum spanning tree using Prim's algorithm,
    and prints the result.
    """
    try:
        logging.info(Fore.GREEN + "Starting the program." + Style.RESET_ALL)
        nodes, bit_count = read_graph_from_file('C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\graph-clustering-big.txt')
        result = kruskal_hash(nodes, bit_count)
        logging.info(Fore.GREEN + f"Kruskal's hash algorithm result for big clustering: {result}" + Style.RESET_ALL)

    except Exception as e:
        logging.exception(Fore.RED + "An error occurred during the execution." + Style.RESET_ALL)

if __name__ == "__main__":
    run()
