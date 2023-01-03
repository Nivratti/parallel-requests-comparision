"""
Output:
lst_elapsed_times: [7.3044119580008555, 6.728941023000516, 7.275437194002734, 7.636319279998133, 7.308217080000759]
avg_elapsed_time: 7.2507

Conclusion: It outperformed httpx with multi processing by 3x
"""
import os
import time
import timeit
from timeit import default_timer as timer

import asyncio
import aiohttp
from aiohttp import ClientSession, ClientConnectorError

async def fetch_html(url: str, session: ClientSession, **kwargs) -> tuple:
    try:
        resp = await session.request(method="GET", url=url, **kwargs)
    except ClientConnectorError:
        return (url, 404)
    return (url, resp.status)

async def make_requests(urls: set, **kwargs) -> None:
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                fetch_html(url=url, session=session, **kwargs)
            )
        results = await asyncio.gather(*tasks)

    # for result in results:
    #     print(f'{result[1]} - {str(result[0])}')

def get_average(number_list):
    from statistics import mean
    avg = mean(number_list)
    avg = round(avg, 4)
    # print("The average is ", avg)
    return avg

def main():
    import pathlib
    import sys

    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    here = pathlib.Path(__file__).parent

    urls = []
    number = 1000
    for i in range(0, number):
        url = "https://httpbin.org/get"
        urls.append(url)

    # asyncio.run(make_requests(urls=urls))

    repeat = 5
    lst_elapsed_times = []
    for i in range(repeat):
        print(f"Repetition: {i}")
        start_time = timer()
        asyncio.run(make_requests(urls=urls))
        end_time = timer()
        elapsed_time = end_time - start_time
        lst_elapsed_times.append(elapsed_time)

    print(f"lst_elapsed_times: {lst_elapsed_times}") # Time in seconds, e.g. 5.38091952400282

    avg_elapsed_time = get_average(lst_elapsed_times)
    print(f"avg_elapsed_time: {avg_elapsed_time}")

if __name__ == "__main__":
    main()