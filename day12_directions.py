
# %%
file = open('input12.txt').read().split('\n')


east_count = 0
west_count = 0
north_count = 0
south_count = 0

directions = ['E', 'S', 'W', 'N']

for x in file:
    direct = directions[0]
    act = x[0]
    val = int(x[1:])
    if act == 'E':
        east_count += val
    elif act == 'W':
        west_count += val
    elif act == 'N':
         north_count += val 
    elif act == 'S':
        south_count += val
    elif act == 'F':
        if direct == 'E':
            east_count += val
        elif direct == 'W':
            west_count += val
        elif direct == 'N':
            north_count += val 
        elif direct == 'S':
            south_count += val


        #degree change
    elif act == 'R':
        if val == 90:
            new_direct = directions[1:]
            new_direct.extend(directions[:1])
            directions = new_direct 
        
        if val == 180:
            new_direct = directions[2:]
            new_direct.extend(directions[:2])
            directions = new_direct 

        if val == 270:
            new_direct = directions[3:]
            new_direct.extend(directions[:3])
            directions = new_direct

    elif act =='L':
        if val == 90:
            new_direct = directions[-1:]
            new_direct.extend(directions[:-1])
            directions = new_direct 
        
        if val == 180:
            new_direct = directions[-2:]
            new_direct.extend(directions[:-2])
            directions = new_direct 

        if val == 270:
            new_direct = directions[-3:]
            new_direct.extend(directions[:-3])
            directions = new_direct
print(abs(east_count- west_count) + abs(north_count - south_count))


# %%

