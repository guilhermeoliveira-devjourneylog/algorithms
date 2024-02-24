## Scenario

Job scheduling problem where each job is characterized by a weight and a length. 
The format includes the number of jobs followed by pairs of weight and length values for each job.

The objective is to implement a greedy algorithm that schedules jobs in descending order of the difference between weight and length. 
In cases where two jobs have the same difference, the one with the higher weight should be scheduled first.

This algorithm may not always yield the optimal solution. 
The task is to compute the sum of weighted completion times for the resulting schedule, where weighted completion time is defined as the sum of job weights multiplied by their completion times.

Other task requires implementing a greedy algorithm to schedule jobs optimally based on the ratio of weight to length. 
The algorithm prioritizes jobs in decreasing order of this ratio, with no specific rule for breaking ties. 
The goal is to calculate and report the sum of weighted completion times of the resulting schedule, which will be a positive integer.