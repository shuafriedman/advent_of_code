#Create and read file
IDs= []
with open(r'C:\Users\sfrie\Documents\Python Scripts\AdventofCode\Day5.txt') as file:
    x = file.readlines()
    
# Loop through each line, removing '/n'        
    for string in x:
        string.strip('\n')
        
#Within the loop, set variables and create numbered list.
        column = []
        numbers = []
        for y in range(0, 128):
            numbers.append(y)
        for z in range(0,8):
            column.append(z)
        
        #Check each letter, dvide the list each time. Then, check last letters.  
        for letter in string:
           # print(letter)
            if letter == 'F':
                numbers = numbers[:int(len(numbers)/2)]
                #print(numbers)
            elif letter == 'B':
                numbers = numbers[-int(len(numbers)/2):]
                #print(numbers)
            elif letter == 'L':
                column = column[:int(len(column)/2)]
                #print(column)
            elif letter == 'R':
                column = column[-int(len(column)/2):]
                #print(column)
        
#Create Id number, add to list of IDs. Then, print the max.
        id = (numbers.pop()*8 + column.pop())
        IDs.append(id)
    print(IDs)
    print('Max ID = ', max(IDs))
       
### PART 2
IDs.sort()
for check in IDs[:]:
    if int(IDs[1]) - int(IDs[0]) == 2:
        print('Your missing ticket = ', IDs[1] - 1)
        break
    else:
        IDs.pop(0)

    
            
        