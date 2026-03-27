import time


def memoize(func, max_size=None, policy="lru", ttl=None):
    cache = {}
    times = {}
    counts = {}

    def wrapper(*args):
        key = args

        if key in cache:
            if ttl and time.time() - times[key] > ttl:
                del cache[key]
                del times[key]
                del counts[key]
            else:
                times[key] = time.time()
                counts[key] += 1
                return cache[key]