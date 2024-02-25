# knapsack.py
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

def read_knapsack_file(file_path):
    """
    Read the knapsack file and return the items and the knapsack capacity.

    Parameters:
    file_path (str): The path to the knapsack file.

    Returns:
    tuple: A tuple containing the items and the knapsack capacity.
    """
    logging.info(Fore.BLUE + "Reading knapsack file: " + file_path + Style.RESET_ALL)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        knapsack_capacity = int(lines[0].split()[0])  # Only take the knapsack capacity
        items = [tuple(map(int, line.split())) for line in lines[1:]]
    return items, knapsack_capacity

def knapsack(items, knapsack_capacity):
    """
    Solve the knapsack problem using dynamic programming.

    Parameters:
    items (list): A list of tuples, where each tuple contains the value and weight of an item.
    knapsack_capacity (int): The capacity of the knapsack.

    Returns:
    int: The maximum value that can be achieved.
    """
    logging.info(Fore.BLUE + "Solving knapsack problem." + Style.RESET_ALL)
    # Initialize the dynamic programming table
    max_value_table = [[0 for _ in range(knapsack_capacity + 1)] for _ in range(len(items) + 1)]

    # Fill the table
    for item_index in range(1, len(items) + 1):
        item_value, item_weight = items[item_index-1]
        for weight_limit in range(1, knapsack_capacity + 1):
            if item_weight <= weight_limit:
                max_value_table[item_index][weight_limit] = max(max_value_table[item_index-1][weight_limit], 
                                                                 max_value_table[item_index-1][weight_limit-item_weight] + item_value)
            else:
                max_value_table[item_index][weight_limit] = max_value_table[item_index-1][weight_limit]

    return max_value_table[-1][-1]

def run():
    """
    Run the knapsack problem solver.
    """
    try:
        logging.info(Fore.GREEN + "Starting the knapsack problem solver." + Style.RESET_ALL)
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\knapsack.txt'
        items, knapsack_capacity = read_knapsack_file(file_path)
        max_knapsack_value = knapsack(items, knapsack_capacity)
        logging.info(Fore.GREEN + f"Maximum value achievable: {max_knapsack_value}" + Style.RESET_ALL)
    except Exception as e:
        logging.exception(Fore.RED + "An error occurred: " + str(e) + Style.RESET_ALL)

if __name__ == "__main__":
    run()