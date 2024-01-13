import os
import json

def read_file(file_name):
    """
    Reads a file containing numbers, one per line. Checks if the file exists and, if it does, 
    opens the file and reads each line, converting each line into an integer and adding it to a list. 
    If the file does not exist, it prints an error message and returns an empty list.
    
    Parameters:
    file_name (str): The name of the file to be read
    
    Returns:
    list: A list of integers contained in the file
    """
    if not os.path.isfile(file_name):
        print(f"file {file_name} does not exist.")
        return []
    with open(file_name, 'r') as file:
        return [int(line.strip()) for line in file]
    
def quicksort(arr, start, end, comparison_count, partition_func):
    """
    Implements the QuickSort sorting algorithm. The function is recursive and uses a partition function 
    to divide the list into two halves and then calls itself for each half.
    
    Parameters:
    arr (list): The list to be sorted
    start (int): The starting index of the list or sublist to be sorted
    end (int): The ending index of the list or sublist to be sorted
    comparison_count (int): Counter for the number of comparisons made
    partition_func (function): The partition function to be used
    
    Returns:
    int: The total number of comparisons made
    """
    if start < end:
        comparison_count += end - start - 1
        pivot_index = partition_func(arr, start, end)
        comparison_count = quicksort(arr, start, pivot_index, comparison_count, partition_func)
        comparison_count = quicksort(arr, pivot_index + 1, end, comparison_count, partition_func)
    return comparison_count

 
def partition(arr, start, end):
    """
    Partitions a portion of an array around a pivot, which is the first element of the portion. 
    Rearranges the elements so that all elements less than the pivot come before all elements greater than the pivot.
    
    Parameters:
    arr (list): The list to be partitioned
    start (int): The starting index of the portion to be partitioned
    end (int): The ending index of the portion to be partitioned
    
    Returns:
    int: The index of the pivot after partitioning
    """
    pivot_value = arr[start]
    i = start + 1
    for j in range(start + 1, end):
        if arr[j] < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    return i - 1

def partition_median(arr, start, end):
    """
    This function partitions a portion of an array around a pivot, which is the median of the first, middle, and last elements of the portion. 
    It rearranges the elements so that all elements less than the pivot come before all elements greater than the pivot.
    
    Parameters:
    arr (list): The list to be partitioned
    start (int): The starting index of the portion to be partitioned
    end (int): The ending index of the portion to be partitioned
    
    Returns:
    int: The index of the pivot after partitioning
    """
    mid = (start + end - 1) // 2
    pivot = sorted([(arr[start], start), (arr[mid], mid), (arr[end - 1], end - 1)])[1][1]
    arr[start], arr[pivot] = arr[pivot], arr[start]
    return partition(arr, start, end)

def partition_last(arr, start, end):
    """
    This function partitions a portion of an array around a pivot, which is the last element of the portion. 
    It rearranges the elements so that all elements less than the pivot come before all elements greater than the pivot.
    
    Parameters:
    arr (list): The list to be partitioned
    start (int): The starting index of the portion to be partitioned
    end (int): The ending index of the portion to be partitioned
    
    Returns:
    int: The index of the pivot after partitioning
    """
    arr[start], arr[end - 1] = arr[end - 1], arr[start]
    return partition(arr, start, end)

def insertion_sort(arr):
    """
    Sorts a list using the Insertion Sort algorithm. Iteratively consumes one input element at each repetition 
    and grows a sorted output list. At each iteration, it removes one element from the input data, 
    finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.
    
    Parameters:
    arr (list): The list to be sorted
    
    Returns:
    list: The sorted list
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quicksort_count(file_name, partition_func):
    """
    Reads an input file, sorts the numbers contained in it using the QuickSort algorithm, and returns the number of comparisons made.
    
    Parameters:
    file_name (str): The name of the file to be read and sorted
    partition_func (function): The partition function to be used in QuickSort
    
    Returns:
    int: The total number of comparisons made
    """
    comparison_count = 0
    arr = read_file(file_name)
    if arr:
        comparison_count = quicksort(arr, 0, len(arr), comparison_count, partition_func)
    return comparison_count

# Read the JSON file and extract the file_name
with open('parameters_values.json', 'r') as json_file:
    data = json.load(json_file)
    file_name = data['file_name']

# Using the first element as the pivot
if file_name is not None:
    comparisons = quicksort_count(file_name, partition)
    if comparisons is not None:
        print('Comparisons using the first element as the pivot', comparisons)
    
# Using the last element as the pivot
if file_name is not None:
    comparisons = quicksort_count(file_name, partition_last)
    if comparisons is not None:
        print('Comparisons using the last element as the pivot', comparisons)
    
# Using the median-of-three as the pivot
if file_name is not None:
    comparisons = quicksort_count(file_name, partition_median)
    if comparisons is not None:
        print('Comparisons using the median-of-three as the pivot', comparisons)
