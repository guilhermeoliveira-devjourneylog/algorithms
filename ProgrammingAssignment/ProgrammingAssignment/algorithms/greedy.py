# greedy.py
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

# Function to read numbers from a file
def read_numbers_from_file(file_path):
    """Reads job data from a file. Each job is represented by a weight and a length."""
    logging.info(Fore.BLUE + "Reading numbers from file: " + file_path + Style.RESET_ALL)
    with open(file_path, 'r') as file:
        lines = file.readlines()

    num_jobs = int(lines[0])
    jobs = []

    for line in lines[1:]:
        weight, length = map(int, line.split())
        jobs.append((weight, length))
        
    logging.info(Fore.BLUE + "Finished reading numbers from file." + Style.RESET_ALL)
    return num_jobs, jobs

# Function to schedule jobs
def schedule_jobs(num_jobs, jobs):
    """Schedules jobs based on their weight and length. Returns the total weighted completion time."""
    logging.info(Fore.BLUE + "Scheduling jobs." + Style.RESET_ALL)
    jobs.sort(key=lambda x: (x[0]-x[1], x[0]), reverse=True)

    completion_time = 0
    weighted_completion_time = 0

    for weight, length in jobs:
        completion_time += length
        weighted_completion_time += weight * completion_time
    return weighted_completion_time

def schedule_jobs_by_ratio(num_jobs, jobs):
    """Schedules jobs based on the ratio of their weight to length. Returns the total weighted completion time."""
    logging.info(Fore.BLUE + "Scheduling jobs by ratio." + Style.RESET_ALL)
    
    # Sort jobs based on the ratio of weight to length
    jobs.sort(key=lambda x: x[0]/x[1], reverse=True)

    completion_time = 0
    weighted_completion_time = 0

    for weight, length in jobs:
        completion_time += length
        weighted_completion_time += weight * completion_time
    return weighted_completion_time


# Main function to run the application
def run():
    """Main function to run the application. Reads job data from a file, schedules the jobs by both methods, and prints the total weighted completion times."""
    try:
        logging.info(Fore.GREEN + "Starting the program." + Style.RESET_ALL)
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\greedy-job.txt'
        
        num_jobs, jobs = read_numbers_from_file(file_path)
        
        jobs_copy1 = jobs.copy()
        result1 = schedule_jobs(num_jobs, jobs_copy1)
        logging.info(Fore.GREEN + "Difference Method - Finished scheduling jobs. Result: " + str(result1) + Style.RESET_ALL)
        logging.info(Fore.GREEN + "Difference Method - Number of jobs: " + str(num_jobs) + ". First job: " + str(jobs_copy1[0]) + ". Last job: " + str(jobs_copy1[-1]) + Style.RESET_ALL)

        jobs_copy2 = jobs.copy()
        result2 = schedule_jobs_by_ratio(num_jobs, jobs_copy2)
        logging.info(Fore.GREEN + "Ratio Method - Finished scheduling jobs. Result: " + str(result2) + Style.RESET_ALL)
        logging.info(Fore.GREEN + "Ratio Method - Number of jobs: " + str(num_jobs) + ". First job: " + str(jobs_copy2[0]) + ". Last job: " + str(jobs_copy2[-1]) + Style.RESET_ALL)
        
    except Exception as e:
        logging.exception(Fore.RED + "An error occurred during the execution." + Style.RESET_ALL)
        
# If the script is run as a program, call the main function
if __name__ == "__main__":
    run()
