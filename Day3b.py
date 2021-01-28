total= 0
def slope(right, down):
    position = 0
    trees = 0
    with open ('Day3.txt') as file:
        if down == 2:
            for line in file.readlines()[::2]:
                if line[position] == '#':
                   trees = trees + 1
                position = (position + right) % 31 
        else:
            next(file)
            for line in file:
                position = (position + right) % 31 
                if line[position] == '#':
                    trees += 1
                
                
    return trees  
     
total = slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2)
print(total)

