#strip lines to a list of strings, e.g. "acc +11"

data1 = open('Day8a.txt', 'r').readlines()
#print(data)
data = [x.strip() for x in data1]

#set variables. line_num will be the guide for which line it will jump to.
#check_list will contain every instruction it iterates over.
accumulator = 0
line_num = 0
check_doubles_list = []  


def check(data_list):
    
    global accumulator
    global line_num
    instruction = data_list[line_num]
    #Instruction is the position, or line, in the data list; given by line_num
       
    cmnd, val = instruction.split()
    print(cmnd, val)
    int_val = int(val.strip(list(val)[0]))  
    #this last strip was to remove the plus and minus
    
    if cmnd == 'nop':
        line_num +=1 
    if cmnd == 'acc':
        line_num +=1
        if '+' in val:
            accumulator += int_val
        if '-' in val:
            accumulator -= int_val
    if cmnd == 'jmp':
        if '+' in val:
            line_num = line_num + int_val
        if '-' in val:
            line_num = line_num - int_val
    
    if line_num > len(data):
        return accumulator, True
  
    
    return accumulator, False

            
        



