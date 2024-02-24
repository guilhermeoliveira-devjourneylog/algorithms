# greedy.py
from colorama import Fore, Style
from igraph import Graph, plot
from mpl_toolkits.mplot3d import Axes3D
import heapq
import sys
import os
import matplotlib.pyplot as plt
import networkx as nx

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

def read_graph_from_file(filename):
    """
    Read a graph from a file. The file should contain the number of nodes and edges on the first line,
    followed by lines representing the edges (from_node, to_node, cost).
    """
    logging.info(Fore.BLUE + "Reading graph from file: " + filename + Style.RESET_ALL)
    with open(filename, 'r') as file:
        lines = file.readlines()
        nodes_count, edges_count = map(int, lines[0].split())
        graph = {i+1: {} for i in range(nodes_count)}  
        for line in lines[1:]:
            from_node, to_node, cost = map(int, line.split())
            graph[from_node][to_node] = cost
            graph[to_node][from_node] = cost 
            logging.info(f"Read edge from {from_node} to {to_node} with cost {cost}")
    logging.info("Finished reading graph from file.")
    return graph

def prim(graph, start_node):
    """
    Implement the Prim's algorithm to find the minimum spanning tree of a graph.
    The graph is represented as a dictionary where the keys are the nodes and the values are dictionaries
    representing the connected nodes and their costs.
    """
    logging.info(Fore.YELLOW + "Starting Prim's algorithm." + Style.RESET_ALL)
    mst = {start_node}  
    edges = [(cost, start_node, to) for to, cost in graph[start_node].items()]
    heapq.heapify(edges)
    
    total_cost = 0

    while edges:
        cost, frm, to = heapq.heappop(edges)
        logging.info(f"Considering edge from {frm} to {to} with cost {cost}")
        if to not in mst:
            mst.add(to)
            total_cost += cost
            logging.info(f"Added edge from {frm} to {to} with cost {cost} to the MST. Current total cost: {total_cost}")
            for to_next, cost2 in graph[to].items():
                if to_next not in mst:  
                    heapq.heappush(edges, (cost2, to, to_next))

    logging.info(Fore.CYAN + f"Total cost of MST: {total_cost}" + Style.RESET_ALL)
    logging.info(Fore.GREEN + "MST: " + str(mst) + Style.RESET_ALL)
    return mst, total_cost

def visualize_graph(graph):
    """
    Visualize the given graph using igraph.
    """
    # Create a list of edges from the graph
    edges = [(from_node - 1, to_node - 1) for from_node, connections in graph.items() for to_node in connections]

    # Create an instance of Graph
    g = Graph(edges=edges, directed=False)

    # Define the path to save the image
    image_path = os.path.join(script_dir, "igraph", "graph-prims.png")

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    # Now you can visualize the graph by saving it to a file
    plot(g, target=image_path, bbox=(300, 300), margin=20)
    logging.info(f"Graph image saved to {image_path}")
    
def visualize_graph_3d(graph):
    """
    Visualizes a graph in 3D using the NetworkX and Matplotlib libraries.

    Parameters:
    graph (dict): A dictionary representing the graph. The dictionary keys are the graph nodes.
                  The values are dictionaries representing the connected nodes and their costs.

    The function creates a NetworkX graph from the input graph, generates a 3D spring layout, and creates a 3D plot using Matplotlib.
    The graph nodes are represented as points in the 3D plot and the edges are represented as lines.

    The plot is displayed using Matplotlib's show() function.
    """
    # Create a new NetworkX graph
    G = nx.Graph()

    # Add edges to the NetworkX graph
    for from_node, connections in graph.items():
        for to_node in connections:
            G.add_edge(from_node, to_node)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Generate a 3D spring layout
    pos = nx.spring_layout(G, dim=3)

    # Extract the coordinates from the position
    x = [pos[k][0] for k in G.nodes]
    y = [pos[k][1] for k in G.nodes]
    z = [pos[k][2] for k in G.nodes]

    # Draw nodes
    ax.scatter(x, y, z)

    # Draw edges
    for edge in G.edges:
        x = [pos[edge[0]][0], pos[edge[1]][0]]
        y = [pos[edge[0]][1], pos[edge[1]][1]]
        z = [pos[edge[0]][2], pos[edge[1]][2]]
        ax.plot(x, y, z, color='black')

    # Show the plot
    plt.show()

    
def run():
    """
    Main function to run the program. It reads a graph from a file, finds its minimum spanning tree using Prim's algorithm,
    and prints the result.
    """
    try:
        logging.info(Fore.GREEN + "Starting the program." + Style.RESET_ALL)
        graph = read_graph_from_file('C:\\Users\\coder\\Dropbox\\PC\\Documents\\Coder Projects\\Git Hub\\stanford algorithm\\algorithms\\ProgrammingAssignment\\ProgrammingAssignment\\data\\edges-prims.txt')
        mst = prim(graph, 1)
        logging.info(f"MST: {mst}")
        print(mst)

        # Visualize the graph
        visualize_graph(graph)
        visualize_graph_3d(graph)

    except Exception as e:
        logging.exception(Fore.RED + "An error occurred during the execution." + Style.RESET_ALL)
        
if __name__ == "__main__":
    run()