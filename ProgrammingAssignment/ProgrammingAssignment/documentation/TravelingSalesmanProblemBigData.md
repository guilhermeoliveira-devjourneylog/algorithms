## Scenario

The assignment revisits the Traveling Salesman Problem (TSP), proposing the implementation of a heuristic instead of an exact algorithm to handle larger problem sizes. 
The task involves using a data file containing city coordinates to compute the TSP solution. 
The heuristic to be implemented is the nearest neighbor method, where the tour starts at the first city and repeatedly visits the closest unvisited city until all cities are visited once, then returns to the starting city to complete the tour. The distance between two cities is calculated using the Euclidean distance formula. The suggestion is to work with squared Euclidean distances for computational simplicity and then convert the tour length to standard Euclidean distance. 
The cost of the TSP tour computed by the nearest neighbor heuristic for the given instance should be entered, rounded down to the nearest integer.