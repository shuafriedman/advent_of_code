#Part B
def check(min, max, letter, seq):
    count = 0
    
    min = seq[int(min) -1]
    max = seq[int(max) -1]
    if letter == min  and letter != max:
        return True
    if letter == max and letter != min:
        return True
#Part A
# def check(min, max, letter, seq):
#     count = 0
#     seq = [list(x) for x in seq]
#     for x in seq[0]:
#         if x == ''.join(letter):
#             count+=1
#     if count >= min and count <= max:
#         return True
#     else:
#         return False


file = open('input2.txt').read().split('\n')
file = [x.split() for x in file]
valid_count = 0

for line in file:
    num, letter, seq = line
    min, max = num.split('-')
    letter =  letter[0]
        
    valid = check(min,max, letter, seq )

    if valid:
        valid_count +=1


print(valid_count)     
