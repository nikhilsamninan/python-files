from sys import getsizeof
h=(x**2 for x in range(100000))
k=[x**2 for x in range(100000)]
print("h",getsizeof(h))
print("k",getsizeof(k))
