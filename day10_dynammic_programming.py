def data():   
    data = open('input10.txt').read().split()
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
    ones = 0
    threes = 0
    for num in range(len(data())-1):
        next_num = data()[num +1]
        num = data()[num]        
        difference = next_num - num
        if difference == 1:
            ones+= 1
        if difference == 3:
            threes += 1
        
    return ones*threes
print(parta())
    
def partb():
    paths = [1] + [0]* data()[-1] #-1 to get rid of the last '+3'
    for num in data():
        #To get the total number of paths, we add the sum of the total number of paths of the three nodes before the current node.
        #e.g.-- [1,2,3,4],  1 has one path (from 0). 2 has 1 path (from 1). 3 has two paths (1-2-3, 1-3). 4 has 4 paths
        # (1-2-3-4, 1-3-4, 1-2-4, 1-4). So the paths array looks like: [1, 1, 2, 4] (four is the sum of the previous three nodes.)
        paths[num] += paths[num -1]+ paths[num-2] + paths[num-3] 
    return paths[-1]

print(partb())