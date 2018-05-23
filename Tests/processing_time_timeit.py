import timeit

# For loop
print (timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

# List comprehension
print (timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))

# Map()
print (timeit.timeit('"-".join(map(str, range(100)))', number=10000))