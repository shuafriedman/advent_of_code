def data():   
    with open(r'C:\Users\sfrie\Python\AdventofCode\Day10.txt') as file:
        x = file.readlines()
        data = [int(y.strip()) for y in x]
        data.append(0)
        data = sorted(data)
        return data

def parta():
    print(data())
    ones = 0
    threes =1
    index = 1
    for num in data():
        if index < len(data()):
            next_num = data()[index]
            print(num, next_num)
            
            difference = next_num - num
            if difference == 1:
                ones+= 1
            if difference == 3:
                threes += 1
            
            index+=1
    return ones, threes, ones*threes
print(parta())
    