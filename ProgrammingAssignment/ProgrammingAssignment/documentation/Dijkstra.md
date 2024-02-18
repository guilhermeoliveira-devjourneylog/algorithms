## Scenario

The task is to implement Dijkstra's shortest-path algorithm on an undirected weighted graph with 200 vertices, 
using vertex 1 as the source. The graph is represented in an adjacency list format in a file. 
The goal is to compute the shortest-path distances between vertex 1 and every other vertex in the graph.

If there's no path between vertex v and vertex 1, the shortest-path distance between them is defined as 1000000. 
The shortest-path distances to specific vertices (7, 37, 59, 82, 99, 115, 133, 165, 188, and 197) need to be reported in a specific order, 
encoded as a comma-separated string of integers.

The implementation should provide the shortest-path distances for the specified vertices according to the given order.