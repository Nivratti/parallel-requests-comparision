# import os
# import time

# from tqdm.auto import tqdm
# from tqdm.contrib.concurrent import process_map, thread_map  # requires tqdm>=4.42.0
# from functools import partial

# def demo_func():
#     time.sleep(4)
#     return 1

# def main():
#     worker = demo_func  # function to map
#     kwargs = {}
#     jobs = img_files  # file_rel_paths

#     results = process_map(
#         partial(worker, **kwargs), 
#         jobs, 
#         max_workers=cpu_workers, 
#         chunksize=1
#     )

# if __name__ == "__main__":
#     main()


import timeit

t1 = timeit.repeat("[_ for _ in range(10)]")
print(t1)