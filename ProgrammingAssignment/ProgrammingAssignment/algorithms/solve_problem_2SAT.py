# solve_problem_2SAT.py
from colorama import Fore, Style
from tqdm import tqdm
import sys
import os
import logging
import collections

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
    Read a graph from a file.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    tuple: A tuple containing the number of variables and a list of clauses.
    """
    logging.info(f"{Fore.GREEN}Reading graph from file: {file_path}{Style.RESET_ALL}")
    clauses = []
    with open(file_path) as file:
        n = int(file.readline().strip())
        for line in file:
            parts = line.split()
            if len(parts) == 2:  
                a, b = map(int, parts)
                clauses.append((a, b))
            else:
                logging.warning(f"{Fore.YELLOW}Line skipped due to incorrect format: {line.strip()}{Style.RESET_ALL}")
    return n, clauses

MAX = 2000001

def add_edges(adj, a, b):
    """
    Add an edge to the adjacency list.

    Parameters:
    adj (dict): The adjacency list.
    a (int): The start node.
    b (int): The end node.
    """
    adj[a].append(b)

def dfs(adj, visited, u, stack):
    """
    Perform a depth-first search.

    Parameters:
    adj (dict): The adjacency list.
    visited (list): A list indicating whether each node has been visited.
    u (int): The current node.
    stack (list): The stack of nodes.
    """
    if visited[u]:
        return
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(adj, visited, v, stack)
    stack.append(u)

def dfs_inv(adj_inv, visited_inv, u, scc, counter):
    """
    Perform a depth-first search on the inverse graph.

    Parameters:
    adj_inv (dict): The adjacency list of the inverse graph.
    visited_inv (list): A list indicating whether each node has been visited in the inverse graph.
    u (int): The current node.
    scc (list): The strongly connected components.
    counter (int): The counter for the strongly connected components.
    """
    if visited_inv[u]:
        return
    visited_inv[u] = True
    for v in adj_inv[u]:
        if not visited_inv[v]:
            dfs_inv(adj_inv, visited_inv, v, scc, counter)
    scc[u] = counter

def process_2sat_instance(n, clauses):
    """
    Perform a depth-first search on the inverse graph.

    Parameters:
    adj_inv (dict): The adjacency list of the inverse graph.
    visited_inv (list): A list indicating whether each node has been visited in the inverse graph.
    u (int): The current node.
    scc (list): The strongly connected components.
    counter (int): The counter for the strongly connected components.
    """
    logging.info(f"{Fore.GREEN}Processing 2SAT instance with {n} variables{Style.RESET_ALL}")
    adj = collections.defaultdict(list)
    adj_inv = collections.defaultdict(list)
    visited = [False] * (2 * MAX)
    visited_inv = [False] * (2 * MAX)
    scc = [0] * (2 * MAX)
    stack = []

    for a, b in tqdm(clauses, desc="Processing clauses"):
        logging.debug(f"{Fore.WHITE}Adding edges for clause ({a}, {b}){Style.RESET_ALL}")
        if a > 0 and b > 0:
            add_edges(adj, a + n, b)
            add_edges(adj_inv, b, a + n)
            add_edges(adj, b + n, a)
            add_edges(adj_inv, a, b + n)
        elif a > 0 and b < 0:
            add_edges(adj, a + n, n - b)
            add_edges(adj_inv, n - b, a + n)
            add_edges(adj, -b, a)
            add_edges(adj_inv, a, -b)
        elif a < 0 and b > 0:
            add_edges(adj, -a, b)
            add_edges(adj_inv, b, -a)
            add_edges(adj, b + n, n - a)
            add_edges(adj_inv, n - a, b + n)
        else:
            add_edges(adj, -a, n - b)
            add_edges(adj_inv, n - b, -a)
            add_edges(adj, -b, n - a)
            add_edges(adj_inv, n - a, -b)
    
    logging.info(f"{Fore.GREEN}Starting first DFS pass{Style.RESET_ALL}")
    for i in tqdm(range(1, 2 * n + 1), desc="DFS pass"):
        if not visited[i]:
            dfs(adj, visited, i, stack)
            
    counter = 1
    logging.info(f"{Fore.GREEN}Starting second DFS pass for SCC identification{Style.RESET_ALL}")
    while stack:
        u = stack.pop()
        if not visited_inv[u]:
            dfs_inv(adj_inv, visited_inv, u, scc, counter)
            counter += 1
    
    for i in tqdm(range(1, n + 1), desc="Checking satisfiability"):
        if scc[i] == scc[i + n]:
            logging.info(f"{Fore.RED}Instance is Unsatisfiable{Style.RESET_ALL}")
            return False
    
    logging.info(f"{Fore.GREEN}Instance is Satisfiable{Style.RESET_ALL}")
    return True

def run():
    """
    Run the program.

    This function prompts the user for file paths, reads the graphs from the files, processes the 2-SAT instances,
    and prints the results.
    """
    file_paths = []
    results = []  # Lista para armazenar os resultados de satisfatibilidade

    while True:
        file_path = input(f"{Fore.YELLOW}Enter a file path for read (or 'done' to finish): {Style.RESET_ALL}").strip().lower()
        if file_path == 'done':
            break
        if not os.path.exists(file_path):
            print("File does not exist. Please try again.")
            continue
        file_paths.append(file_path)

    for file_path in tqdm(file_paths):
        try:
            logging.info(f"{Fore.GREEN}Processing file: {file_path}{Style.RESET_ALL}")
            n, clauses = read_graph_from_file(file_path)
            satisfiable = process_2sat_instance(n, clauses)
            results.append(satisfiable)  
            result_str = "Satisfiable" if satisfiable else "Unsatisfiable"
            print(f"Result for {os.path.basename(file_path)}: {result_str}")
        except Exception as e:
            logging.exception(f"{Fore.RED}An error occurred while processing {file_path}: {e}{Style.RESET_ALL}")

    result_bits = ''.join(['1' if r else '0' for r in results])
    logging.info(f"{Fore.CYAN}Summary of results: {result_bits}{Style.RESET_ALL}")

            
if __name__ == "__main__":
    run()
