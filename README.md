# Python Notes

### Python memory management with function scoping

scope defines the area of a program in which you can access that variable.

## Magic command in jupyter to save code in jupyter cell to a file

```py
%%file memory.py
from random import *
def create_and_sum_matrix(N):
    # Create
    matrix = [[random() for _ in range(N)] for _ in range(N)]
    # Sum
    total_by_line = [sum(l) for l in matrix]
    total = sum(total_by_line)
    # Delete
    del total_by_line
    del matrix
    # Return
    return total
```

## Memory profiling in python with print and psutil

```py
from random import *
import resource
import os
import psutil
process = psutil.Process(os.getpid())
def get_memory_MB():
    return process.memory_info().rss / 1e6
def peak_memory_MB():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3
def memory_profile(func):
    def memory(N):
        print(f'cur memory usage before {get_memory_MB()}')
        print(f'max memory usage before {peak_memory_MB()}')
        return func(N)
    return memory
@memory_profile
def create_and_sum_matrix(N):
    # Create
    matrix = [[random() for _ in range(N)] for _ in range(N)]
    # Sum
    total_by_line = [sum(l) for l in matrix]
    total = sum(total_by_line)
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
```

Converted it to a python decorator that can be imported from memory.py to be used with any function in python script. 

## range 

range is very useful, it can even be used in bisect functions.  The strength is that it can be reated in O(1) time compared to a python list because it is a range iterator.
But range allows O(1) access to elements in the range.