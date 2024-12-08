import timeit

row = list(range(10_000))  # A list with 10,000 elements
i = 5000

# Using list comprehension
def list_comp():
    [row[x] for x in range(len(row)) if x != i]

# Using slicing
def slicing():
    row[:i] + row[i + 1:]
    
print(timeit.timeit(list_comp, number=1))
print(timeit.timeit(slicing, number=1))
    