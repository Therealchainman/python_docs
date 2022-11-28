"""
This is an example of how to import from memory.py to be able to use it for printing out memory information, 
adding it as a decorator to function that requires one argument input. And maybe at some print statements after the function
to observe the memory usage over each function call. 
"""
from random import *
from memory import *
import os
import psutil
@memory_profile
def create_and_sum_matrix(N):
    # Create
    matrix = [[random() for _ in range(N)] for _ in range(N)]
    # Sum
    total_by_line = [sum(l) for l in matrix]
    total = sum(total_by_line)*2
    # Return
    return matrix
def main():
    res = create_and_sum_matrix(10000)
    print(f'cur memory usage after {get_memory_MB()}')
    print(f'max memory usage after {peak_memory_MB()}')
    create_and_sum_matrix(10000)
    print(f'cur memory usage after {get_memory_MB()}')
    print(f'max memory usage after {peak_memory_MB()}')
    return res

if __name__ == '__main__':
    main()
    print(f'cur memory at end {get_memory_MB()}')
