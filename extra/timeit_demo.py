import timeit
from dill.source import getsource
import array

def foo_array(n):
    import array
    return array.array("i", [0]*n)

def foo_list(n):
    return [0]*n

def bench(snippet, number=1_000_000, rep=5, setup=''):
    return timeit.repeat(
        snippet,
        number=number,
        repeat=rep,
        setup=setup
    )

def main():
    number = 100
    rep = 5

    results = {}
    snippets = {
        "foo_array": "foo_array(100_000)",
        "foo_list" : "foo_list(100_000)",
    }
    for name, snippet in snippets.items():
        setup = getsource(eval(name))
        results[name] = bench(snippet, number, rep, setup)
        rounded_time = round(min(results[name]), 4)
        print(f"Min time: {rounded_time} : {name}")

        # max_rounded_time = round(max(results[name]), 4)
        # print(f"Max time: {rounded_time} : {name}")

if __name__ == "__main__":
    main()