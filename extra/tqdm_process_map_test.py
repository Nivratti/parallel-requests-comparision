import os
import time
import timeit
from timeit import default_timer as timer

from tqdm.auto import tqdm
from tqdm.contrib.concurrent import process_map, thread_map  # requires tqdm>=4.42.0
from functools import partial

def demo_func(num):
    time.sleep(3)
    return 1

def test_process_map(number=100, cpu_workers_cnt=4):
    worker = demo_func  # function to map
    kwargs = {}
    jobs = range(0, number)

    results = process_map(
        partial(worker, **kwargs), 
        jobs, 
        max_workers=cpu_workers_cnt
    )

def main():
    start_time = timer()
    test_process_map(number=1000, cpu_workers_cnt=128)
    end_time = timer()
    elapsed_time = end_time - start_time
    print(f"elapsed_time: {elapsed_time}") # Time in seconds, e.g. 5.38091952400282

if __name__ == "__main__":
    main()