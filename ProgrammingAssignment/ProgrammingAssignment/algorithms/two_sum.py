# two_sum.py
from colorama import Fore, Style
from concurrent.futures import ProcessPoolExecutor
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
    """
    Reads numbers from a file and stores them in a set.
    
    Args:
        file_path (str): The path to the file to be read.
        
    Returns:
        set: A set of numbers read from the file.
    """
    logging.info(Fore.YELLOW + "Reading numbers from file..." + Style.RESET_ALL)
    with open(file_path, 'r') as f:
        numbers = {int(line.strip()) for line in f}
    logging.info(Fore.GREEN + f"Finished reading numbers from file. Total numbers: {len(numbers)}" + Style.RESET_ALL)
    return numbers

def process_segment(numbers_set, segment):
    """
    Processes a segment of target values. For each target value in the segment, it checks if there are two numbers in the set that sum up to the target value.
    The function starts by logging the start of processing this segment. Then it initializes an empty set to store valid target values.
    It then iterates over each target value in the segment. For each target, it iterates over each number in the set and calculates the complement of the current number with respect to the target.
    If the complement is in the set and is not the same as the current number, it means we found two distinct numbers that sum up to the target. The target is then added to the set of valid targets and the valid pair found is logged.
    If a valid pair is found for a target, the inner loop is broken and the function moves on to the next target. Once all targets in the segment have been processed, the function logs the end of processing this segment and returns the set of valid targets found in this segment.
    
    Args:
        numbers_set (set): A set of numbers. These are the numbers that will be checked to see if any two numbers sum up to a target value.
        segment (list): A list of target values. These are the values that we want to check if any two numbers from the set can sum up to.
        
    Returns:
        set: A set of valid target values. A target value is considered valid if there are two distinct numbers in the set that sum up to it.
    """
    # Log the start of processing this segment
    logging.info(Fore.YELLOW + f"Processing segment: {segment[0]}-{segment[-1]}" + Style.RESET_ALL)
    
    # Initialize an empty set to store valid target values
    valid_targets_segment = set()
    
    # Iterate over each target value in the segment
    for target in segment:
        # For each target, iterate over each number in the set
        for number in numbers_set:
            # Calculate the complement of the current number with respect to the target
            complement = target - number
            
            # If the complement is in the set and is not the same as the current number,
            # it means we found two distinct numbers that sum up to the target
            if complement in numbers_set and complement != number:
                # Add the target to the set of valid targets
                valid_targets_segment.add(target)
                
                # Log the valid pair found
                logging.info(Fore.BLUE + f"Found valid pair: ({number}, {complement}) for target: {target}" + Style.RESET_ALL)
                
                # Break the inner loop as we found a valid pair for this target
                break  
    
    # Log the end of processing this segment
    logging.info(Fore.GREEN + f"Finished processing segment. Valid targets in segment: {len(valid_targets_segment)}" + Style.RESET_ALL)
    
    # Return the set of valid targets found in this segment
    return valid_targets_segment

def two_sum_using_hashing_parallel(numbers, target_range):
    """
    Solves the "Two Sum" problem using parallel processing. The function first converts the list of numbers into a set for faster lookup. 
    Then it divides the range of target values into segments, where the size of each segment is determined by the total number of target values divided by the number of CPUs. 
    Each segment is then processed in parallel using a process pool executor. For each segment, the function `process_segment` is called which checks if there are two distinct numbers in the set that sum up to the target value. 
    The results from each process are then collected and the set of valid targets is updated with the valid targets found in each segment. 
    The function logs the start and end of the calculation, as well as the number of segments prepared for parallel processing. 
    Finally, the function returns the total number of valid target values found.
    
    Args:
        numbers (list): A list of numbers. These are the numbers that will be checked to see if any two numbers sum up to a target value.
        target_range (range): A range of target values. These are the values that we want to check if any two numbers from the list can sum up to.
        
    Returns:
        int: The total number of valid target values found. A target value is considered valid if there are two distinct numbers in the list that sum up to it.
    """
    # Log the start of the calculation
    logging.info(Fore.YELLOW + "Calculating two sum using parallel processing..." + Style.RESET_ALL)
    
    # Convert the list of numbers into a set for faster lookup
    numbers_set = set(numbers) 
    
    # Initialize an empty set to store valid target values
    valid_targets = set()
    
    # Convert the range of target values into a list
    target_range_list = list(target_range)
    
    # Calculate the size of each segment by dividing the total number of target values by the number of CPUs
    segment_size = len(target_range_list) // os.cpu_count() 
    
    # Divide the list of target values into segments
    segments = [target_range_list[i:i + segment_size] for i in range(0, len(target_range_list), segment_size)]
    
    # Log the number of segments prepared for parallel processing
    logging.info(Fore.YELLOW + f"Prepared {len(segments)} segments for parallel processing" + Style.RESET_ALL)

    # Create a process pool executor
    with ProcessPoolExecutor() as executor:
        # Map the function process_segment to each segment and execute them in parallel
        results = executor.map(process_segment, [numbers_set] * len(segments), segments)
        
        # Iterate over the results returned by each process
        for result in results:
            # Update the set of valid targets with the valid targets found in this segment
            valid_targets.update(result)
    
    # Log the end of the calculation
    logging.info(Fore.GREEN + f"Finished calculating two sum using parallel processing. Total valid targets: {len(valid_targets)}" + Style.RESET_ALL)
    
    # Return the number of valid target values found
    return len(valid_targets)

def run():
    try:
        logging.info(Fore.GREEN + "Starting the program." + Style.RESET_ALL)
        # file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\test-algo1-programming-prob-2sum.txt'
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\algo1-programming-prob-2sum.txt'
        target_range = range(-10000, 10001)
        numbers = read_numbers_from_file(file_path)
        count = two_sum_using_hashing_parallel(numbers, target_range)
        logging.info(Fore.GREEN + f"Number of target values: {count}" + Style.RESET_ALL)
    except Exception as e:
        logging.exception(Fore.RED + "An error occurred during the execution." + Style.RESET_ALL)        
if __name__ == "__main__":
    run()


