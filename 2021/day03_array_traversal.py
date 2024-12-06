#Simple Part A
# trees = 0
# position = 3
# with open ('input_3.txt') as file:
#     next(file)
#     for line in file:
#         if line[position] == '#':
#             trees += 1
#         position = (position + 3) % 31

file = open('input3.txt').read()
file = file.split()
line = [list(line) for line in file]

def check(cur):
    if cur == '#':
       return True

def check_slope(down, right):
    count = 0
    x = down
    y = right
    while x < len(file):
        cur = line[x][y]
        if check(cur):
            count += 1
        x+=down
        if y + right >= len(line[0]):
            y = (y+right) % len(line[0])
        else:
            y+=right
    return count
#Part A
print(check_slope(1,3))

#Part B
print(check_slope(1,1) * check_slope(1, 3) * check_slope(1, 5) * check_slope(1,7) * check_slope(2, 1)  )  