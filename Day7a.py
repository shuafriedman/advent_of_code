import re
import pprint
count = 0


with open(r'Day7.txt') as file:
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
    print("current root is " + current_bag)
    rules = diction[current_bag]
    print("It's children are " , rules)
    for x in rules:
        val, color = x.split(' ',1)
        if color == "shiny gold":
            count +=1
            return 'none'
        # elif color == 'other':
        #     current_bag = color
        else:
            for k in diction.keys():    
                if color in diction.keys():
                    next_item = diction[color]
                    if next_item[0] != 'no other':
                        current_bag = color
                        return search_bag(current_bag)
                    # else:
                    #     print(color, " contains no other bags")
number = 0
for bag in diction.keys():
    
        #val, color = x.split(' ',1)
        #if color == 'other':
        # continue
    search_bag(bag)
    number += 1

print(' total', count, number)


# 
#
#
#
#
