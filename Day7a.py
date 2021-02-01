import re
import pprint
count = 0


with open(r'C:\Users\sfrie\Python\AdventofCode\Day7.txt') as file:
    list_ = file.readlines()
    list_ = [y.strip() for y in list_]
    new_line = [re.split(r"contain|\,", line) for line in list_]
    



diction = {}

#Make dictionary
for line in new_line:
    bag_key = line[0].strip()
    bag_key = bag_key[:-5]
    line =  [x.rsplit(' ', 1) for x in line]
    line = [x[:-1] for x in line]
    line = [y.strip(' ') for x in line for y in x]
    
    diction[bag_key] = line[1:]


pprint.pprint(diction)
        
        #val, color = x.split(' ', 1)
        


def search_bag(current_bag):
    global count
    global bag
    global rules
    rules = diction[current_bag]
    for x in rules:
        val, color = x.split(' ',1)
        if color == "shiny gold":
            count +=1
            return 'none'
        elif color == 'other':
            return "none"
        else:
            current_bag = color
            return search_bag(current_bag)         
    
for bag, rules in diction.items():
    for x in rules:
        val, color = x.split(' ',1)
        if color == 'other':
            continue
        else:
            search_bag(color)
    
print(' total', count)

        
        