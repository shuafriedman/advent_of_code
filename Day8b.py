def data():
    data = open('Day8.txt', 'r').readlines()
    #print(data)
    data2 = [x.strip() for x in data]
    list_data_return = [x.split() for x in data2]
    return list_data_return


list_data = data()

def check(data_list): 
    global loop
    global accumulator
    global line_num
    instruction = data_list[line_num]
    #Instruction is the position, or line, in the data list; given by line_num
       
    cmnd = instruction[0]
    val = instruction[1]
    int_val = int(val.strip(list(val)[0]))  
    #this last strip was to remove the plus and minus
    
    if (line_num) in check_doubles_list:
        return "didnt work"
    else:
        check_doubles_list.append(line_num) 
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
                
        if len(list_data) <= line_num:
            print('you made it')
            print(cmnd, val, accumulator)
            return False
        return check(data_list)
    
        #When it recursses, it returns the function again with the new line_num.

for x in list_data:
    accumulator = 0
    line_num = 0
    check_doubles_list = [] 
    if 'jmp' in x:
        x[0] = 'nop'
        check(list_data)
        x[0] = 'jmp'
    elif 'nop' in x:
        x[0] = 'jmp'
        check(list_data)
        x[0] = 'nop'
    if check(list_data) == False:
        break
