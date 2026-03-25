import time
def wrapper(*args):
        key = args

        if key in cache:
            if ttl is not None:
                if time.time() - access_times[key] > ttl:
                    del cache[key]
                    del access_times[key]
                    del access_counts[key]
                    insert_order.remove(key)
                    else:
                times[key] = time.time()
                counts[key] += 1
                return cache[key]

        if max_size and len(cache) >= max_size:
            if policy == "lru":
