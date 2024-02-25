# knapsack_big_data.py
from colorama import Fore, Style
import sys
import os
import logging
sys.setrecursionlimit(10000)

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
    Reads a file containing the knapsack problem data.

    Parameters:
    file_path (str): The path to the file to be read.

    Returns:
    items (list): A list of tuples, where each tuple contains the value and weight of an item.
    knapsack_capacity (int): The capacity of the knapsack.
    """
    logging.info(Fore.BLUE + "Reading knapsack file: " + file_path + Style.RESET_ALL)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        knapsack_capacity, _ = map(int, lines[0].split())
        items = [tuple(map(int, line.split())) for line in lines[1:]]
    logging.info(Fore.BLUE + f"Read {len(items)} items with total capacity {knapsack_capacity}" + Style.RESET_ALL)
    return items, knapsack_capacity

def knapsack_recursive(items, capacity, currentItemIndex, cachedResults):
    """
    Solves the knapsack problem using a recursive approach with memoization.

    Parameters:
    items (list): A list of tuples, where each tuple contains the value and weight of an item.
    capacity (int): The current capacity of the knapsack.
    currentItemIndex (int): The index of the current item to be considered.
    cachedResults (dict): A dictionary to store already computed results.

    Returns:
    int: The maximum value that can be achieved.
    """
    # Verifica se o resultado já está no cache
    if (currentItemIndex, capacity) in cachedResults:
        return cachedResults[(currentItemIndex, capacity)]
    
    # Caso base: nenhum item restante ou capacidade nula
    if currentItemIndex == 0 or capacity == 0:
        maxValue = 0
    elif items[currentItemIndex-1][1] > capacity:
        # O item atual não cabe, ignorá-lo
        maxValue = knapsack_recursive(items, capacity, currentItemIndex-1, cachedResults)
    else:
        # O item cabe, decidir se pega ou não
        valueWithoutItem = knapsack_recursive(items, capacity, currentItemIndex-1, cachedResults)
        valueWithItem = items[currentItemIndex-1][0] + knapsack_recursive(items, capacity-items[currentItemIndex-1][1], currentItemIndex-1, cachedResults)
        maxValue = max(valueWithoutItem, valueWithItem)
    
    # Armazena o resultado no cache antes de retornar
    cachedResults[(currentItemIndex, capacity)] = maxValue
    return maxValue

def knapsack_optimized(items, capacity):
    """
    Solves the knapsack problem using an optimized approach.

    Parameters:
    items (list): A list of tuples, where each tuple contains the value and weight of an item.
    capacity (int): The capacity of the knapsack.

    Returns:
    int: The maximum value that can be achieved.
    """
    logging.info(Fore.BLUE + "Solving knapsack problem with optimized approach" + Style.RESET_ALL)
    cachedResults = {}
    maxValue = knapsack_recursive(items, capacity, len(items), cachedResults)
    logging.info(Fore.BLUE + "Knapsack problem solved" + Style.RESET_ALL)
    return maxValue

def run():
    """
    Runs the main function of the script.

    Reads the knapsack problem data from a file, solves the problem using the knapsack_optimized() function,
    and logs the maximum value that can be achieved. If an error occurs during execution, it will be logged.
    """
    try:
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\knapsack-big-data.txt'
        logging.info(Fore.BLUE + "Starting run function" + Style.RESET_ALL)
        items, knapsack_capacity = read_knapsack_file(file_path)
        max_knapsack_value = knapsack_optimized(items, knapsack_capacity)
        logging.info(Fore.GREEN + f"Maximum value achievable: {max_knapsack_value}" + Style.RESET_ALL)
    except Exception as e:
        logging.exception(Fore.RED + "An error occurred: " + str(e) + Style.RESET_ALL)
    finally:
        logging.info(Fore.BLUE + "Run function finished" + Style.RESET_ALL)

if __name__ == "__main__":
    logging.info(Fore.BLUE + "Starting program" + Style.RESET_ALL)
    run()
    logging.info(Fore.BLUE + "Program finished" + Style.RESET_ALL)
