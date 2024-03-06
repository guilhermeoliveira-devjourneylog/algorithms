# traveling_salesman_problem.py
from colorama import Fore, Style
from tqdm import tqdm
import sys
import os
import logging
import math

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
    Reads a file containing city coordinates and returns a list of tuples, where each tuple contains the coordinates of a city.
    
    :param file_path: Path to the file to be read.
    :return: List of tuples, where each tuple contains the coordinates of a city.
    """
    logging.info(f"Reading graph from file: {file_path}")
    cities = []
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        if not first_line.isdigit():
            raise ValueError(f"Invalid file format. The first line of the file should be a number, but got: {first_line}")
        num_cities = int(first_line)
        for line in file:
            _, x_coord, y_coord = line.split()
            cities.append((float(x_coord), float(y_coord)))
    logging.info(f"Read {len(cities)} cities from file: {file_path}")
    return cities

def calculate_distance(city1, city2):
    """
    Calculates the Euclidean distance between two cities.

    :param city1: Tuple containing the coordinates of the first city.
    :param city2: Tuple containing the coordinates of the second city.
    :return: Euclidean distance between the two cities.
    """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_heuristic(cities):
    """
    Solves the traveling salesman problem using the nearest neighbor heuristic.

    :param cities: List of tuples, where each tuple contains the coordinates of a city.
    :return: A tuple containing the sequence of visited cities and the total distance traveled.
    """
    logging.info(Fore.GREEN + "Starting Nearest Neighbor Heuristic" + Style.RESET_ALL)
    n = len(cities)
    visited = [False] * n
    visited[0] = True
    path = [0]
    total_distance = 0.0
    src = 0
    
    pbar = tqdm(total=n, desc="Processing cities", ncols=100)
    
    while sum(visited) < n:
        min_dist = float('inf')
        dest = None
        for i in range(1, n):
            if not visited[i]:
                dist = calculate_distance(cities[src], cities[i])
                if dist < min_dist:
                    min_dist = dist
                    dest = i
        total_distance += min_dist
        visited[dest] = True
        path.append(dest)
        src = dest
            
        pbar.update(1) 

    pbar.close()  

    # Add distance to return to the starting city
    total_distance += calculate_distance(cities[src], cities[0])
    
    logging.info(Fore.GREEN + "Finished Nearest Neighbor Heuristic." + Style.RESET_ALL)
    logging.info(Fore.BLUE + f"Total distance traveled: {total_distance}" + Style.RESET_ALL)
    logging.info(Fore.BLUE + f"Sequence of cities visited: {path}" + Style.RESET_ALL)
    
    return path, total_distance

def run():
    file_paths = []

    while True:
        file_path = input("Enter a file path for read (or 'done' to finish): ").strip().lower()
        if file_path == 'done':
            break
        file_paths.append(file_path)

    for file_path in file_paths:
        try:
            logging.info(f"Processing file: {file_path}")
            cities = read_graph_from_file(file_path)
            logging.info("Starting the nearest neighbor heuristic...")
            final_path, total_distance = nearest_neighbor_heuristic(cities) 
            logging.info(f"Total path distance (rounded): {round(total_distance)}")
            logging.info(f"The final path is: {final_path}")
        except Exception as e:
            logging.exception(f"An error occurred while processing {file_path}: {e}")
            
if __name__ == "__main__":
    run()
