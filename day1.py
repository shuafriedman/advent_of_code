file = open("input1.txt").read().split()
file

#Part B
def multiply():
    for x in range(len(file)-1):
        cur = int(file[x])
        second = int(file[x+1])
        for y in range(len(file)-1):
            second = int(file[y])
            for z in range(len(file)-1):
                if x != y and y!= z:
                    third = int(file[z])
                    if cur + second + third == 2020:
                        result = cur*second*third

                        return(result)
print(multiply())              
