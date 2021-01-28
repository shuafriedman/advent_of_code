#Read file, split by line breaks into lists
txt_file = r'C:\Users\sfrie\Documents\Python Scripts\AdventofCode\Day6.txt'

def data_6partA():
    with open(txt_file) as file:
        passengers = file.read()
        string_1 = passengers.split('\n\n')
        string_2 = [x.replace('\n', '') for x in string_1]
        string_3 = [x.split() for x in string_2]
        return string_3
 
def data_6partB():
    with open(txt_file) as file:
        passengers = file.read()
        string_1 = passengers.split('\n\n')
        groups = [x.split('\n') for x in string_1]
    return groups   
 
    
def part_a():
    total = 0
    for x in data_6partA():
        for y in x:
            total += len(set(y))
    return total
 
   
def part_b():
    import string
    #Read file, split by line breaks into lists        
    count = 0
    for group in data_6partB():
        if '' in group:
            group.remove('')
            #^^ gets rid of the last '' I found after the last line
        unique_answers = string.ascii_lowercase
        for answers in group:
            questions = set(answers)
            unique_answers = set(unique_answers) & questions
        count += len(unique_answers)
    return count

print(part_a())
print(part_b())      
 
###PART B ALTERNATE, without String.Ascii.
#This one sets the first element of the list, and compares other elements
#in the group to it.     
# =============================================================================
# count = 0
# for group in data_6partB():
#     if '' in group:    
#         group.remove('')
#     unique_answers = None
#     for answers in group:
#         good_set = set(answers)
#         if unique_answers == None:
#             unique_answers = good_set
#         else:
#             unique_answers = unique_answers & good_set
#     count += len(unique_answers)
# print(count)
# =============================================================================
