## Scenario

The task is to calculate the total number of comparisons needed to sort the 
input file using QuickSort with three different pivoting rules.

Comparisons are not counted individually; instead, when a recursive call is made on a subarray of length m, m - 1 is 
added to the total comparisons due to comparisons with the pivot element. The Partition subroutine must be implemented. 
For this assignment's first part, always use the first element of the array as the pivot element. 
The file contains integers from 1 to 10,000 in unsorted order. Each row corresponds to an entry in an input array. 