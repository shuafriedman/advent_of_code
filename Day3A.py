trees = 0
position = 3
with open ('Day3.txt') as file:
    next(file)
    for line in file:
        if line[position] == '#':
            trees += 1
        print(line)
        print(position)
        print(line[position])
        position = (position + 3) % 31
print(trees)
            