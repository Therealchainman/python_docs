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
    def memory(*args):
        print(func)
        print(f'cur memory usage before {get_memory_MB()}')
        print(f'max memory usage before {peak_memory_MB()}')
        return func(*args)
    return memory
