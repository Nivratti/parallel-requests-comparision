"""
output:
lst_elapsed_times: [21.164009856998746, 20.691512638997665, 20.67186188300184, 21.12792774799891, 21.291930178002076]
avg_elapsed_time: 20.9894

Conclusion:
It's slower as compare to aiohttp
"""
import os
import time
import timeit
from timeit import default_timer as timer

from tqdm.auto import tqdm
from tqdm.contrib.concurrent import process_map, thread_map  # requires tqdm>=4.42.0
from functools import partial

import httpx ## pip install httpx


def make_request(index):
    r = httpx.get('https://httpbin.org/get', timeout=30)
    # if r.status_code == 200:
    #     print(f"{index} response json: {r.json()}")
    # else:
    #     print(f"r.status_code: {r.status_code}")
    #     pass
    return r

def test_process_map(number=100, cpu_workers_cnt=4):
    worker = make_request  # function to map
    kwargs = {}
    jobs = range(0, number)

    results = process_map(
        partial(worker, **kwargs), 
        jobs, 
        max_workers=cpu_workers_cnt
    )

def get_average(number_list):
    from statistics import mean
    avg = mean(number_list)
    avg = round(avg, 4)
    # print("The average is ", avg)
    return avg

def main():
    repeat = 5
    lst_elapsed_times = []
    for i in range(repeat):
        print(f"Repetition: {i}")
        start_time = timer()
        test_process_map(number=1000, cpu_workers_cnt=100)
        end_time = timer()
        elapsed_time = end_time - start_time
        lst_elapsed_times.append(elapsed_time)

    print(f"lst_elapsed_times: {lst_elapsed_times}") # Time in seconds, e.g. 5.38091952400282

    avg_elapsed_time = get_average(lst_elapsed_times)
    print(f"avg_elapsed_time: {avg_elapsed_time}")

if __name__ == "__main__":
    main()