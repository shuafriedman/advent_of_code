# %%
file = open('input6.txt').read().split('\n\n')
file = [x.split('\n') for x in file]

#Part A
# %%
def count_any():
    count = 0
    for group in file:
        unique = set()
        for passenger in group:
            for x in passenger:
                unique.add(x)

        count+= len(unique) 
    return count

def count_all():
    count = 0
    
    for group in file:
        all_list = []
        for passenger in group:
            unique = set()
            for x in passenger:
                unique.add(x)
            all_list.append(unique)
        intersect = set.intersection(*all_list)
        count+= len(intersect) 
    return count  


# %%
print('Part A, ', count_any())
print('Part B, ', count_all())  




