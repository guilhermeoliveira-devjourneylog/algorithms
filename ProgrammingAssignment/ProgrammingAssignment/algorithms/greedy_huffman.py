# greedy_huffman.py
from colorama import Fore, Style
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

# Configure logging for the application
configure_logging()

class Node:
    """
    Class to represent a node in a Huffman tree.
    
    Attributes:
        symbol: The symbol represented by the node.
        frequency: The frequency of the symbol in the data.
        left: The left child node.
        right: The right child node.
    """
    def __init__(self, symbol, frequency):
        """
        Initialize a node with a symbol, a frequency and pointers to the left and right child nodes.
        """
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        """
        Define less than comparison for nodes based on frequency.
        """
        return self.frequency < other.frequency
    
# Function to read numbers from a file
def read_frequencies_into_nodes(file_path):
    """
    Read frequencies from a file and convert them into nodes.
    
    Args:
        file_path: The path to the file containing the frequencies.
        
    Returns:
        A list of nodes representing the frequencies.
    """
    logging.info(Fore.BLUE + "Reading numbers from file..." + Style.RESET_ALL)
    frequencies = []
    with open(file_path, 'r') as file:
        next(file)  # Pula a primeira linha que contém o total de símbolos/frequências
        for line in file:  # Itera diretamente sobre as linhas restantes
            frequency = line.strip()
            logging.info("Read frequency: %s" % frequency)  # Registra a frequência lida
            frequencies.append(Node(None, int(frequency)))  # Converte cada linha em um objeto Node
    return frequencies

def create_priority_queue(node_list):
    """
    Create a priority queue from a list of nodes.
    
    Args:
        node_list: The list of nodes to be converted into a priority queue.
        
    Returns:
        A priority queue of nodes.
    """
    logging.info(Fore.BLUE + "Creating priority queue..." + Style.RESET_ALL)
    heapq.heapify(node_list)
    logging.info("Finished creating priority queue.")
    return node_list

def build_huffman_tree(priority_queue):
    """
    Build a Huffman tree from a priority queue of nodes.
    
    Args:
        priority_queue: The priority queue of nodes.
        
    Returns:
        The root node of the Huffman tree.
    """
    logging.info(Fore.BLUE + "Building Huffman tree..." + Style.RESET_ALL)
    while len(priority_queue) > 1:
        # Pop the two nodes with the lowest frequencies
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Log the frequencies of the nodes
        logging.info("Popped nodes with frequencies: %s, %s" % (left.frequency, right.frequency))

        # Create a new parent node with these two nodes as children
        parent = Node(None, left.frequency + right.frequency)
        parent.left = left
        parent.right = right

        # Push the new parent node back into the priority queue
        heapq.heappush(priority_queue, parent)

    # The last node in the priority queue is the root of the Huffman tree
    root = heapq.heappop(priority_queue)

    logging.info("Finished building Huffman tree.")
    return root

def max_codeword_length(node, depth=0):
    """
    Determine the maximum codeword length in a Huffman tree.
    
    Args:
        node: The root node of the Huffman tree.
        depth: The current depth in the tree (default is 0).
        
    Returns:
        The maximum codeword length.
    """
    if node is None:
        return 0  # If there's no node, there's no depth
    if node.left is None and node.right is None:  
        return depth  # Return current depth if leaf node
    left_depth = max_codeword_length(node.left, depth + 1)
    right_depth = max_codeword_length(node.right, depth + 1)
    return max(left_depth, right_depth)

def min_codeword_length(node, depth=0):
    """
    Determine the minimum codeword length in a Huffman tree.
    
    Args:
        node: The root node of the Huffman tree.
        depth: The current depth in the tree (default is 0).
        
    Returns:
        The minimum codeword length.
    """
    if node is None:
        return float('inf')  # Return infinity for comparison purposes
    if node.left is None and node.right is None:
        return depth  # Return current depth if leaf node
    left_depth = min_codeword_length(node.left, depth + 1)
    right_depth = min_codeword_length(node.right, depth + 1)
    return min(left_depth, right_depth)

# Main function to run the application
def run():
    """
    Main function to run the application.
    """
    try:
        logging.info(Fore.GREEN + "Starting the program." + Style.RESET_ALL)
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\huffman.txt'
        symbols_and_frequencies = read_frequencies_into_nodes(file_path)
        priority_queue = create_priority_queue(symbols_and_frequencies)
        huffman_tree = build_huffman_tree(priority_queue)
        max_length = max_codeword_length(huffman_tree)
        min_length = min_codeword_length(huffman_tree)
        if min_length == float('inf'): 
            min_length = 1
        print("The minimum length of a codeword is: ", min_length)
        print("The maximum length of a codeword is: ", max_length)

    except Exception as e:
        logging.exception(Fore.RED + "An error occurred during the execution." + Style.RESET_ALL)

# If the script is run as a program, call the main function
if __name__ == "__main__":
    run()
