
import timeit

with open('1.txt', 'r') as f:
    f = f.readlines()
def solve_puzzle():
    list_a = []
    list_b = []
    differences = 0
    for pair in f:
        a,b=pair.split()
        list_a.append(int(a))
        list_b.append(int(b))


    counts = {}
    for val in sorted(list_b):
        counts[str(val)] = counts.get(str(val), 0) + 1
    for a in sorted(list_a):
        b = counts.get(str(a), 0)
        differences+= abs(a * b)
    print(differences)
    
#timeit
print(timeit.timeit(solve_puzzle, number=1))