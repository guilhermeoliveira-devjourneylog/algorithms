# median_maintenance.py
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

configure_logging()
    
def read_graph_from_file(file_path):
    """
    Reads a text file containing numbers, each on a new line.
    Returns a list of numbers.

    :param file_path: The path to the file to be read.
    :return: A list of numbers.
    """
    logging.info(Fore.BLUE + f"Reading numbers from file: {file_path}" + Style.RESET_ALL)
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    logging.info(Fore.BLUE + f"Finished reading {len(numbers)} numbers from file" + Style.RESET_ALL)
    return numbers

def median_maintenance(numbers):
    """
    Performs median maintenance on a list of numbers.
    Returns the sum of the medians, modulo 10000.

    :param numbers: The list of numbers.
    :return: The sum of the medians, modulo 10000.
    """
    logging.info(Fore.YELLOW + "Starting median maintenance" + Style.RESET_ALL)
    lower = [] 
    higher = [] 
    medians = []

    for number in numbers:
        if not lower or number < -lower[0]:
            heapq.heappush(lower, -number)
        else:
            heapq.heappush(higher, number)

        if len(lower) < len(higher):
            heapq.heappush(lower, -heapq.heappop(higher))
        elif len(lower) > len(higher) + 1:
            heapq.heappush(higher, -heapq.heappop(lower))

        medians.append(-lower[0])

    result = sum(medians) % 10000
    logging.info(Fore.YELLOW + f"Finished median maintenance. The sum of the medians, modulo 10000, is {result}" + Style.RESET_ALL)
    return result

def run():
    try:
        logging.info(Fore.GREEN + "Starting the program." + Style.RESET_ALL)
         # file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\test-median.txt'
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\median.txt'
        numbers = read_graph_from_file(file_path)
        result = median_maintenance(numbers)
        logging.info(f"The sum of the medians, modulo 10000, is {result}")

    except Exception as e:
        logging.exception(Fore.RED + "An error occurred during the execution." + Style.RESET_ALL)
        
if __name__ == "__main__":
    run()



