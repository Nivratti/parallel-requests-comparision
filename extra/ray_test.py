import os
import time
import timeit
from timeit import default_timer as timer
import ray

@ray.remote
def demo_func(num):
    time.sleep(3)
    return 1

def test_ray_remote(number=100, cpu_workers_cnt=4):
    lst = range(0, number)
    results = ray.get(
        [demo_func.remote(num) for num in lst],
    )
    # print("Result returned:", results)

def main():
    start_time = timer()
    test_ray_remote(number=10, cpu_workers_cnt=128)
    end_time = timer()
    elapsed_time = end_time - start_time
    print(f"elapsed_time: {elapsed_time}") # Time in seconds, e.g. 5.38091952400282

if __name__ == "__main__":
    main()