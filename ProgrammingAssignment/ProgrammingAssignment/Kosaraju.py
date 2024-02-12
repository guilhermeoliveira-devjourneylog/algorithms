from colorama import Fore, Style
from collections import defaultdict
import logging
from log_config import configure_logging
import sys

configure_logging()

def read_graph_from_file(file_path):
    logging.info(f"Attempting to read graph data from {file_path}")
    graph = defaultdict(list)
    graph_rev = defaultdict(list)
    try:
        with open(file_path, 'r') as file:
            edge_count = 0
            for line in file:
                tail, head = map(int, line.split())
                graph[tail].append(head)
                graph_rev[head].append(tail)
                edge_count += 1

            all_vertices = set(graph.keys()) | set(graph_rev.keys())

        logging.info(f"File successfully read with {len(all_vertices)} vertices and {edge_count} edges.")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An error occurred while reading the file: {e}")
        sys.exit(1)
    return graph, graph_rev

def dfs_iterative(graph, start_vertex, visited, stack=None, count=False):
    logging.debug(f"Entering DFS for vertex {start_vertex}.")
    stack_dfs = [start_vertex]
    size = 0 if count else None

    while stack_dfs:
        vertex = stack_dfs.pop()
        if vertex not in visited:
            visited.add(vertex)
            logging.debug(f"Marking vertex {vertex} as visited.")
            if count:
                size += 1
                logging.debug(f"Current SCC size: {size}.")
            if stack is not None:
                stack.append(vertex)
            for neighbor in graph[vertex]:  
                if neighbor not in visited:
                    logging.debug(f"Visiting neighbor {neighbor} of vertex {vertex}. Adding to stack.")
                    stack_dfs.append(neighbor)
                    
    logging.debug(f"Exiting DFS for vertex {start_vertex} with SCC size: {size if count else 'N/A'}.")
    return size if count else None

def first_pass(graph_rev, visited, finish_order):
    logging.info("Starting first pass of Kosaraju's algorithm.")
    for vertex in graph_rev:
        if vertex not in visited:
            dfs_iterative(graph_rev, vertex, visited, finish_order)

def second_pass(graph, visited, finish_order):
    logging.info("First pass completed. Starting second pass.")
    scc_sizes = []
    while finish_order:
        vertex = finish_order.pop()
        logging.debug(f"Processing vertex {vertex} from finish_order in second DFS pass.")
        if vertex not in visited:
            scc_size = dfs_iterative(graph, vertex, visited, count=True)
            scc_sizes.append(scc_size)
            logging.info(f"SCC found with {scc_size} vertices starting from vertex {vertex}.")
    return scc_sizes

def kosaraju(graph, graph_rev):
    logging.info("Starting Kosaraju's algorithm.")
    visited = set()
    finish_order = []
    first_pass(graph_rev, visited, finish_order)
    visited.clear()
    scc_sizes = second_pass(graph, visited, finish_order)
    top_5_sccs = sorted(scc_sizes, reverse=True)[:5] + [0] * (5 - len(scc_sizes))
    logging.info("Kosaraju's algorithm completed. SCCs identified.")
    return top_5_sccs

def main():
    try:
        logging.info("Starting the program.")
        # file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\Data\\graph.txt'
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\Data\\test_graph_simple.txt'
        graph, graph_rev = read_graph_from_file(file_path)
        top_5_sccs = kosaraju(graph, graph_rev)
        print(f"{Fore.GREEN}Top 5 SCC sizes: {','.join(map(str, top_5_sccs))}{Style.RESET_ALL}")
    except Exception as e:
        logging.exception("An error occurred during the execution.")

if __name__ == "__main__":
    main()