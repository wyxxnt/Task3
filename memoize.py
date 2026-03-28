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
                key]

        if max_size and len(cache) >= max_size:
            if policy == "lru":
                old = min(cache, key=lambda k: times[k])
            elif policy == "lfu":
                old = min(cache, key=lambda k: counts[k])
            else:
                old = list(cache.keys())[0]
            del cache[old]
            del times[old]
            del counts[old]

        result = func(*args)
        cache[key] = result
        times[key] = time.time()
        counts[key] = 1
        return result

    wrapper.cache = cache
    wrapper.clear = lambda: (cache.clear(), times.clear(), counts.clear())

    return wrapper