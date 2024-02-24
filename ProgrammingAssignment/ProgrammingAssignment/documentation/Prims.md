## Scenario

The problem involves implementing Prim's minimum spanning tree algorithm for an undirected graph with integer edge costs. 

The input file format consists of the number of nodes, the number of edges, and details of each edge including the nodes it connects and its cost. 

The task is to find the minimum spanning tree and report its overall cost, which may be negative. While a straightforward implementation with O(mn) time complexity is sufficient due to the small graph size, an optional challenge involves implementing a heap-based version for better efficiency. This can be achieved by maintaining relevant edges in a heap or storing unprocessed vertices in the heap. 
Both approaches require careful management of the heap and potentially mapping between vertices and their positions.


