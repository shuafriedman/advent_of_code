def data():   
    data = open(r'Day10.txt').read().split()
    data = sorted(list(map(int, data)))
    return data
# =============================================================================
#     with open(r'Day10.txt') as file:
#         x = file.readlines()
#         data = [int(y.strip()) for y in x]
#         data.append(0)
#         data.append(max(data)+3)
#         data = sorted(data)
# =============================================================================
   

def parta():
    print(data())
    ones = 0
    threes = 0
    for num in range(len(data())-1):
        next_num = data()[num +1]
        num = data()[num]
        print(num, next_num)
        
        difference = next_num - num
        if difference == 1:
            ones+= 1
        if difference == 3:
            threes += 1
        
    return ones, threes, ones*threes
print(parta())
    
def partb():
# =============================================================================
#     paths = [1] + [0] * data()[-2]
#         #-2, to get rid of the first 0 and the last '+3'
#     
#     list = []
#     for x in range(1, max(data())-2):
#         list.append(x)
#     print(data())
#     print(list)
#     for index in range(1, max(data())-2):
#         for x in range(1,4):
#             if (index -x) in data():
#                 paths[index] += paths[index-x]
#     
#     print(paths)    
#     return paths[-1]
# 
# =============================================================================

    paths = [1] + [0]* data()[-1]
    for num in data():
        paths[num] += paths[num -1]+ paths[num-2] + paths[num-3]
        print(paths)
    return paths[-1]

print(partb())