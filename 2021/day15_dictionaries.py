#Code from Dylan Codes Youtube Channel
file =open('input15.txt').read()
file = file.split(',')
file = list(map(int, file))

def part_a(rounds, cur_index, file, keep_going):

    while keep_going:
        
        if cur_index == rounds- 1:
            keep_going = False
            return(file[cur_index])
             
        else:
            finish_check = False
            for check in range(len(file)-2, -1, -1):  #-2, to skip the first one.
                if file[cur_index] == file[check]: 
                                                    #need to find a way to get the index of check- as of now, it takes the first instance from the left. need first instance from right.
                    file.append(((cur_index)) - (check)) #add +1 to fix the positioning value in the math.
                    finish_check = True
                    break
            if finish_check == False:
                file.append(0)
            cur_index+=1
#[0,3,6]

#part b
def part_b(rounds):
    file =open('input15.txt').read()
    file = file.split(',')
    file = list(map(int, file))

    memory = {}
    #initiate the memory with the first three numbers
    for index in range(len(file)-1): #We don't want to check the last in the input, so that it will know that it will know it is not in memory.
        cur = file[index]
        memory[cur] = index

    for index in range(len(file)-1, rounds-1):
        #add to memory (key = cur number, value = index)
        cur = file[index]
        if cur not in memory:
            file.append(0)
            memory[cur] = index
        else:
            last = memory[cur]
            new_num = index - last
            file.append(new_num)
            memory[cur]= index
    return file[rounds-1]

cur_index = 1
keep_going = True 
print(part_a(2020, (len(file)-1), file, keep_going))

#Part B calls for 30000000 rounds. The part A can not accomplish this, because the iterations are too large. In part A,
#the way it is written, requires the program to search through the list of numbers on each iteration. However, the list of numbers
#grows to very large lengths, requiring a lot of computing.

#In part B, the code uses a dicitonary. By using the dictionary, we can keep track of the last index instance of each number,
# and we don't need to search through the whole appended file to find the most recent instance- we can call it from the dicitonary.

#Part B also solves part a, however I left up my original solution for part A for learning purposes.


print(part_b(30000000))
        #check if key's last instance is in memory (memory will only consist of last instance)

            #if not, append 0
            #if yes, calculate current index - memory index, and append to file.
            # make current index into the memory index
        


