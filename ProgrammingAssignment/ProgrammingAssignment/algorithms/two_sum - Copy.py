# two_sum.py
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
    
def read_numbers_from_file(file_path):
    logging.info(Fore.YELLOW + "Reading numbers from file..." + Style.RESET_ALL)
    numbers = np.loadtxt(file_path, dtype=int)
    logging.info(Fore.GREEN + f"Finished reading numbers from file. Total numbers: {numbers.size}" + Style.RESET_ALL)
    return numbers


def two_sum(numbers, target_range):
    logging.info(Fore.YELLOW + "Calculating two sum..." + Style.RESET_ALL)
    valid_targets = set()
    numbers_set = set(numbers)
    for target in target_range:
        logging.info(Fore.BLUE + f"Processing target: {target}" + Style.RESET_ALL)
        for number in numbers_set:
            complement = target - number
            if complement in numbers_set and complement != number:
                valid_targets.add(target)
                logging.info(Fore.BLUE + f"Found valid target: {target}" + Style.RESET_ALL)
                break
    logging.info(Fore.GREEN + f"Finished calculating two sum. Total valid targets: {len(valid_targets)}" + Style.RESET_ALL)
    return len(valid_targets)

def run():
    try:
        logging.info(Fore.GREEN + "Starting the program." + Style.RESET_ALL)
         # file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\test-algo1-programming-prob-2sum.
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\algo1-programming-prob-2sum.txt'
        target_range = range(-10000, 10001)
        numbers = read_numbers_from_file(file_path)
        logging.info(Fore.YELLOW + f"Starting two sum calculation for {numbers.size} numbers." + Style.RESET_ALL)
        count = two_sum(numbers, target_range)
        logging.info(Fore.GREEN + f"Number of target values: {count}" + Style.RESET_ALL)
    except Exception as e:
        logging.exception(Fore.RED + "An error occurred during the execution." + Style.RESET_ALL)        
if __name__ == "__main__":
    run()
    


