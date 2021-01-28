with open(r"C:\Users\sfrie\Documents\Python Scripts\AdventofCode\Day3.txt") as file:
    lines = [line.rstrip() for line in file]
    skip = []
    count = 2
    for l in lines:
      if count % 2 == 0:
        skip.append(l)
      count += 1
    print(len(skip))
    
    
total= 0
def slope(position, down):
    trees = 0
    with open ('Day3.txt') as file:
        if down == 2:
            for line in skip:
               if line[position] == '#':
                   trees = trees + 1
                   
                   position = (position + 3) % 31
        else:
            next(file)
            for line in file:
                if line[position] == '#':
                    trees = trees + 1
                
                position = (position + 3) % 31
                
    return trees  
     
total = slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2)
print(total)


