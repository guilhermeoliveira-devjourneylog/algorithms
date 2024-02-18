## Scenario

The vertices are labeled as positive integers from 1 to 875714. Each row indicates an edge, 
the vertex label in the first column is the tail, and the vertex label in the second column is 
the head (remember that the graph is directed, and the edges are directed from the vertex in the 
first column to the vertex in the second column). So, for example, the 11th line looks like: "2 47646". 
This simply means that the vertex labeled as 2 has an outgoing edge to the vertex labeled as 47646.

Task is to compute the strongly connected components (SCCs) and execute this algorithm on the provided graph, 
producing the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoiding spaces).