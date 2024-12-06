with open('2024/2.txt', 'r') as f:
    f = f.readlines()

def check_adjacent(a, b):
    dif = abs(a-b)
    return True if dif <=3 and dif >=1 else False

def check_for_consistency(val, next_val, direction):
    if val < next_val:
        if direction == 'increase':
            return False
        return 'decrease'
    if val > next_val:
        if direction == 'decrease':
            return False
        return 'increase'
def check_row_for_rules(a):
    direction = None
    for i in range(len(a)-1):
        next_val = int(a[i+1])
        val = int(a[i])
        if not check_adjacent(val, next_val):
            return False
        direction = check_for_consistency(val, next_val, direction)
        if not direction:
            return False
    return True

#level 1
print(sum([check_row_for_rules(row.split()) for row in f]))

#level 2
count = 0
for row in f:
    row = row.split()
    valid = check_row_for_rules(row)
    if not valid:
        for i in range(len(row)):
            new_row = row.copy()
            #new_row.remove(row[i]) 
            new_row = [row[x] for x in range(len(row)) if x !=i]
            if check_row_for_rules(new_row):
                count+=1
                break
    else:
        count+=1
print(count)
                
        
         