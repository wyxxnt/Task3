import time
from memoize import memoize


def add(a, b):
    return a + b


print("=== LRU ===")
m = memoize(add, max_size=3, policy="lru")
m(1, 2)
m(3, 4)
m(5, 6)
print(m.cache)
m(7, 8)
print(m.cache)

print("\n=== LFU ===")
m2 = memoize(add, max_size=3, policy="lfu")
m2(1, 2)
m2(1, 2)
m2(1, 2)
m2(3, 4)
m2(5, 6)
m2(7, 8)
print(m2.cache)

print("\n=== TTL ===")
m3 = memoize(add, ttl=1.0)
print(m3(10, 20))
print(m3(10, 20))
time.sleep(1.5)
print(m3(10, 20))

print("\n=== Clear ===")
m4 = memoize(add)
m4(1, 1)
m4(2, 2)
print(len(m4.cache))
m4.clear()
print(len(m4.cache))