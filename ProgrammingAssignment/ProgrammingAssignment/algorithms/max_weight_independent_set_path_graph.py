# max_weight_independent_set_path_graph.py
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

def read_file(file_path):
    """
    Function to read numbers from a file.
    Ignores the first line that contains the number of vertices.
    """
    logging.info(Fore.YELLOW + "Reading file: " + file_path + Style.RESET_ALL)
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file.readlines()[1:]]

def max_weight_independent_set(weights):
    """
    Function to calculate the maximum weight independent set.
    It uses a dynamic programming approach.
    """
    logging.info(Fore.YELLOW + "Calculating max weight independent set." + Style.RESET_ALL)
    max_weights = [0, weights[0]]
    
    # Build up the max_weights list with the maximum weight of the independent set for the first i vertices
    for i in range(2, len(weights) + 1):
        max_weights.append(max(max_weights[i - 1], max_weights[i - 2] + weights[i - 1]))
    
    # Backtrack to find the vertices included in the maximum weight independent set
    i = len(weights)
    vertices = []
    while i > 1:
        if max_weights[i - 1] > max_weights[i - 2] + weights[i - 1]:
            i -= 1
        else:
            vertices.append(i)
            i -= 2
    if i == 1:
        vertices.append(i)
    
    return sorted(vertices)

def vertices_to_bit_string(vertices, vertices_of_interest):
    """
    Function to convert the vertices to a bit string.
    The bit string has a '1' for each vertex of interest that is in the maximum weight independent set, and '0' otherwise.
    """
    logging.info(Fore.YELLOW + "Converting vertices to bit string." + Style.RESET_ALL)
    return ''.join('1' if i in vertices else '0' for i in vertices_of_interest)
    
def run():
    """
    Main function to run the application.
    It reads the weights from a file, calculates the maximum weight independent set, and converts the result to a bit string.
    """
    try:
        logging.info(Fore.GREEN + "Starting the program." + Style.RESET_ALL)
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\mwis.txt'
        weights = read_file(file_path)
        
        vertices = max_weight_independent_set(weights)
    
        vertices_of_interest = [1, 2, 3, 4, 17, 117, 517, 997]
    
        bit_string = vertices_to_bit_string(vertices, vertices_of_interest)

        logging.info(Fore.GREEN + "Bit string: " + bit_string + Style.RESET_ALL)
    except Exception as e:
        logging.exception(Fore.RED + "An error occurred during the execution." + Style.RESET_ALL)

# If the script is run as a program, call the main function
if __name__ == "__main__":
    run()
