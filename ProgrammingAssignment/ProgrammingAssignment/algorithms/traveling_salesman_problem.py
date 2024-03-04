# traveling_salesman_problem.py
from colorama import Fore, Style
import numpy as np
import math
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
    Reads a file containing city coordinates and returns a list of tuples, where each tuple represents a city and contains its x and y coordinates.

    Parameters:
    file_path (str): The path to the file to be read.

    Returns:
    cities (list): A list of tuples, where each tuple contains the x and y coordinates of a city.
    """
    logging.info(f"{Fore.GREEN}Reading graph from file: {file_path}{Style.RESET_ALL}")
    # 'cities' is a list that will store the coordinates of each city
    cities = []
    
    # 'file' is a file object opened for reading
    with open(file_path, 'r') as file:
        
        # 'num_cities' is the number of cities, which is the first line of the file
        num_cities = int(file.readline())
        
        # For each remaining line in the file
        for line in file:
            
            # 'x_coord' and 'y_coord' are the x and y coordinates of the city, respectively
            x_coord, y_coord = map(float, line.split())
            
            # Add the city to the list of cities
            cities.append((x_coord, y_coord))
            
    logging.info(f"{Fore.BLUE}Read {len(cities)} cities from file: {file_path}{Style.RESET_ALL}")
    return cities

def calculate_distance_matrix(cities):
    """
    Calculates and returns a distance matrix for a list of cities. The distance matrix is a 2D numpy array where the element at [i, j] represents the Euclidean distance between city i and city j.

    Parameters:
    cities (list): A list of tuples, where each tuple contains the x and y coordinates of a city.

    Returns:
    dist (numpy.ndarray): A 2D numpy array representing the distance matrix.
    """
    num_cities = len(cities)
    dist = np.zeros((num_cities, num_cities), dtype=np.float32)

    logging.info(f"{Fore.YELLOW}Calculating distance matrix for {num_cities} cities.{Style.RESET_ALL}")
    
    # 'city1_index' and 'city2_index' are indices representing two cities. We calculate the distance between
    # every pair of cities and store it in the 'dist' matrix. 'city1_index' and 'city2_index' can be the same,
    # in which case the distance is 0 because it's the same city.
    for city1_index in range(num_cities):
        for city2_index in range(num_cities):
            dist[city1_index, city2_index] = math.sqrt((cities[city1_index][0] - cities[city2_index][0])**2 + (cities[city1_index][1] - cities[city2_index][1])**2)
            logging.debug(f"Distance between city at position {city1_index} and city at position {city2_index} is {dist[city1_index, city2_index]}")
    
    logging.info(f"{Fore.CYAN}Finished calculating distance matrix.{Style.RESET_ALL}")
    return dist

def reconstruct_path(parent, cost_matrix, num_cities):
    """
    Reconstructs the optimal path for the Traveling Salesman Problem using the parent matrix and the cost matrix.

    Parameters:
    parent (numpy.ndarray): A 2D numpy array where the element at [i, j] represents the city visited before city i when visiting the subset of cities represented by j.
    cost_matrix (numpy.ndarray): A 2D numpy array where the element at [i, j] represents the minimum cost to visit the subset of cities represented by j ending at city i.
    num_cities (int): The number of cities.

    Returns:
    path (list): The optimal path represented as a list of city indices.
    """
    mask = (1 << num_cities) - 1
    city_index = np.argmin(cost_matrix[:, mask])
    path = [city_index]
    
    logging.info(f"{Fore.MAGENTA}Reconstructing path.{Style.RESET_ALL}")
    
    while mask:
        city_index = parent[city_index][mask]
        if city_index == -1:
            break
        path.append(city_index)
        mask &= ~(1 << city_index)
        logging.debug(f"City at position {city_index} added to the path.")
    
    path.reverse()
    logging.info(f"{Fore.WHITE}Finished reconstructing path.{Style.RESET_ALL}")
    return path

def tsp(cities):
    """
    Solves the Traveling Salesman Problem using dynamic programming.

    Parameters:
    cities (list): A list of tuples, where each tuple contains the x and y coordinates of a city.

    Returns:
    min_cost (int): The minimum cost to visit all cities and return to the starting city.
    path (list): The optimal path represented as a list of city indices.
    """
    num_cities = len(cities)
    dist = calculate_distance_matrix(cities)

    cost_matrix = np.full((num_cities, 1 << num_cities), np.inf, dtype=np.float32)
    parent = np.full((num_cities, 1 << num_cities), -1, dtype=int)  
    cost_matrix[0][1] = 0

    logging.info(f"{Fore.GREEN}Starting the Traveling Salesman Problem solution for {num_cities} cities.{Style.RESET_ALL}")

    for subset in range(1, 1 << num_cities):
        for current_city_index in range(num_cities):
            if not (subset & (1 << current_city_index)):
                continue
            prev_subset = subset & ~(1 << current_city_index)
            if prev_subset == 0:
                continue

            for next_city_index in range(num_cities):
                if not (prev_subset & (1 << next_city_index)):
                    continue
                new_cost = cost_matrix[next_city_index][prev_subset] + dist[next_city_index][current_city_index]
                if new_cost < cost_matrix[current_city_index][subset]:
                    cost_matrix[current_city_index][subset] = new_cost
                    parent[current_city_index][subset] = next_city_index
                    logging.debug(f"{Fore.YELLOW}Updated cost and parent for city {current_city_index} in subset {subset}.{Style.RESET_ALL}")

    path = reconstruct_path(parent, cost_matrix, num_cities)
    min_cost = np.min(cost_matrix[:, (1 << num_cities) - 1])
    
    logging.info(f"{Fore.GREEN}Finished the Traveling Salesman Problem solution. Minimum cost is {min_cost}.{Style.RESET_ALL}")
    
    return math.floor(min_cost), path

def two_opt_swap(route, start_index, end_index):
    """
    Performs a 2-opt swap operation on a route.

    Parameters:
    route: The current route represented as a list of city indices.
    start_index: The starting index of the section of the route to be reversed. Should be a value between 0 and len(route) - 1.
    end_index: The ending index of the section of the route to be reversed. Should be a value between start_index + 1 and len(route).

    Returns:
    new_route: The new route after the 2-opt swap operation.
    """
    # Creates a new route by reversing the section of the route between the indices start_index and end_index (inclusive).
    new_route = route[:start_index] + route[start_index:end_index+1][::-1] + route[end_index+1:]
    return new_route


def route_distance(city_route, distance_matrix):
    """
    Calculates the total distance of a route.

    Parameters:
    city_route: The route represented as a list of city indices.
    distance_matrix: A 2D numpy array where the element at [i, j] represents the distance between city i and city j.

    Returns:
    total_distance: The total distance of the route.
    """
    # Calculates the sum of the distances between each pair of consecutive cities in the route.
    total_distance = sum(distance_matrix[city_route[i], city_route[i + 1]] for i in range(len(city_route) - 1))
    # Adds the distance from the last city in the route to the first city.
    total_distance += distance_matrix[city_route[-1], city_route[0]]
    return total_distance


def two_opt(city_list, initial_city_route, distance_matrix):
    """
    Performs the 2-opt algorithm to find a better route.

    Parameters:
    city_list: The list of cities.
    initial_city_route: The initial route represented as a list of city indices.
    distance_matrix: A 2D numpy array where the element at [i, j] represents the distance between city i and city j.

    Returns:
    best_route: The best route found after performing the 2-opt algorithm.
    """
    best_route = initial_city_route
    improved = True
    while improved:
        improved = False
        for start_index in range(1, len(best_route) - 1):
            for end_index in range(start_index + 1, len(best_route)):
                new_route = two_opt_swap(best_route, start_index, end_index)
                if route_distance(new_route, distance_matrix) < route_distance(best_route, distance_matrix):
                    best_route = new_route
                    improved = True
    return best_route

def nearest_neighbor_heuristic(cities, dist):
    """
    Solves the Traveling Salesman Problem using the Nearest Neighbor heuristic.

    Parameters:
    cities (list): A list of tuples, where each tuple contains the x and y coordinates of a city.
    dist (numpy.ndarray): A 2D numpy array where the element at [i, j] represents the distance between city i and city j.

    Returns:
    path (list): The path found using the Nearest Neighbor heuristic represented as a list of city indices.
    total_cost (float): The total cost of the path found.
    """
    num_cities = len(cities)
    visited = set()
    total_cost = 0
    path = [0] 
    visited.add(0)
    current_city = 0
    while len(visited) < num_cities:
        nearest = None
        nearest_dist = float('inf')
        for next_city in range(num_cities):
            if next_city not in visited and dist[current_city, next_city] < nearest_dist:
                nearest = next_city
                nearest_dist = dist[current_city, next_city]
        visited.add(nearest)
        path.append(nearest)
        total_cost += nearest_dist
        current_city = nearest
    total_cost += dist[current_city, 0]  
    path.append(0) 
    logging.info(f"{Fore.GREEN}Finished Nearest Neighbor Heuristic. Total cost: {total_cost}{Style.RESET_ALL}")
    return path, total_cost

def run():
    """
    Main function to run the Traveling Salesman Problem solution.

    It prompts the user to enter file paths for reading city data and whether to use the nearest neighbor heuristic.
    It then processes each file, calculates the shortest path using the chosen method, and logs the results.
    Finally, it finds and logs the shortest of the shortest paths calculated.

    No parameters.

    Returns:
    None
    """
    file_paths = []
    shortest_paths = []

    while True:
        file_path = input("Enter a file path for read (or 'done' to finish): ").strip().lower()
        if file_path == 'done':
            break
        file_paths.append(file_path)

    heuristic = input("Use nearest neighbor heuristic? [y/N]: ").strip().lower()

    for file_path in file_paths:
        try:
            logging.info(f"{Fore.GREEN}Processing file: {file_path}{Style.RESET_ALL}")
            cities = read_graph_from_file(file_path)
            dist = calculate_distance_matrix(cities)  

            if heuristic == 'y':
                initial_path, initial_cost = nearest_neighbor_heuristic(cities, dist)
                optimized_path = two_opt(cities, initial_path, dist)
                optimized_cost = route_distance(optimized_path, dist)
                logging.info(f"Initial cost with Nearest Neighbor Heuristic: {initial_cost}")
                logging.info(f"Optimized cost with 2-opt: {optimized_cost}")
                shortest_paths.append((optimized_cost, optimized_path))
            else:
                total_cost, path = tsp(cities)
                logging.info(f"Dynamic Programming Solution cost for {file_path}: {total_cost}")
                shortest_paths.append((total_cost, path))
        except Exception as e:
            logging.exception(f"{Fore.RED}An error occurred while processing {file_path}: {e}{Style.RESET_ALL}")

    if shortest_paths:
        shortest_of_shortest_paths = min(shortest_paths, key=lambda x: x[0])
        logging.info(f"{Fore.GREEN}The shortest of the shortest paths is: {shortest_of_shortest_paths[0]}{Style.RESET_ALL}")
        logging.info(f"Path: {shortest_of_shortest_paths[1]}")
    else:
        logging.info(f"{Fore.RED}No paths calculated.{Style.RESET_ALL}")

if __name__ == "__main__":
    run()
