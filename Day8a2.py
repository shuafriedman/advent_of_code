def data():
    data = open(r'C:\Users\sfrie\Python\AdventofCode\Day8a.txt').readlines()
    #print(data)
    data2 = [x.strip() for x in data]
    list_data_return = [x.split() for x in data2]
    return list_data_return
list_data = data()


#set variables. line_num will be the guide for which line it will jump to.
#check_list will contain every instruction it iterates over.
  
accumulator = 0
line_num = 0
check_doubles_list = []
#This is the issue. Won't reset after x in the loop at the bottom, because its
#a global variable. However, if I put it in the function, it resets after recursion.


def check(data_list):
    global accumulator
    global line_num
    instruction = data_list[line_num]
    loop = True
    #Instruction is the position, or line, in the data list; given by line_num
    
    while loop:
        cmnd = instruction[0]
        val = instruction[1]
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
        
        #this is the recursion. line_num is -1, because we want to check if the
        #line is in the doubles_list before we have skipped to the next instruction.
        if (line_num -1) in check_doubles_list:
            loop = False
            return "nope"

        else:
            check_doubles_list.append(line_num -1)
            return check(data_list)
    if len(data_list) <= line_num:
        return accumulator, "End of List"
            #When it recursses, it returns the function again with the new line_num.
for x in list_data:
    if 'jmp' in x:
        x[0] == 'nop'
        print(check(list_data))
        x[0] == 'jmp'
    elif 'nop' in x:
        x[0] = 'jmp'
        print(check(list_data))
        x[0] = 'nop'                     