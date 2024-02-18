# kosaraju
from colorama import Fore, Style
from igraph import Graph, plot
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
    Reads a text file containing edges of a graph and returns an igraph.Graph object.
    
    Args:
        file_path (str): The path to the text file to be read.

    Returns:
        graph (igraph.Graph): The graph read from the file.
    """
    logging.info(f"Attempting to read graph data from {file_path}")
    edges = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                tail, head = map(int, line.split())
                edges.append((tail - 1, head - 1))  # Subtract 1 from each vertex label

        logging.info(f"File successfully read with {len(edges)} edges.")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    graph = Graph.TupleList(edges, directed=True)
    return graph

def kosaraju(graph):
    """
    Runs the Kosaraju's algorithm on the provided graph and returns the sizes of the 5 largest strongly connected components.

    Args:
        graph (igraph.Graph): The graph to be analyzed.

    Returns:
        top_5_sccs (list): A list containing the sizes of the 5 largest strongly connected components.
    """
    logging.info("Starting Kosaraju's algorithm.")
    sccs = graph.connected_components(mode="STRONG") 
    scc_sizes = []
    for scc in sccs:
        original_labels = [vertex_index + 1 for vertex_index in scc]  
        scc_size = len(original_labels)  
        scc_sizes.append(scc_size)
    top_5_sccs = sorted(scc_sizes, reverse=True)[:5] + [0] * (5 - len(scc_sizes))  
    logging.info("Kosaraju's algorithm completed. SCCs identified.")
    return top_5_sccs
    
def visualize_graph(graph):
    """
    Visualizes the provided graph using the Fruchterman Reingold layout algorithm and saves the visualization as a PNG image.

    Args:
        graph (igraph.Graph): The graph to be visualized.
    """
    image_path = os.path.join(script_dir, "igraph", "graph-kosaraju.png")
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    layout = graph.layout("fr") 
    plot(graph, layout=layout, target=image_path)
    logging.info(f"Finished visualizing graph. Image saved to {image_path}")
    

def run():
    """
    The main function of the program. Reads a graph from a file, visualizes the graph, runs the Kosaraju's algorithm on the graph, and prints the sizes of the 5 largest strongly connected components.
    """
    try:
        logging.info("Starting the program.")
        # file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\test-graph-kosaraju.txt'
        file_path = 'C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\graph-kosaraju.txt'
        graph = read_graph_from_file(file_path)
        visualize_graph(graph)
        top_5_sccs = kosaraju(graph)
        print(f"{Fore.GREEN}Top 5 SCC sizes: {','.join(map(str, top_5_sccs))}{Style.RESET_ALL}")
    except Exception as e:
        logging.exception("An error occurred during the execution.")

if __name__ == "__main__":
    run()