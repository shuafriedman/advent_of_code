import re
import pprint

with open(r'Day7.txt') as file:
    list_ = file.readlines()
    list_ = [y.strip() for y in list_]
    new_line = [re.split(r"contain|\,", line) for line in list_]

#Make dictionary
diction = {}
#Make dictionary
for line in new_line:
    bag_key = line[0].strip()
    bag_key = bag_key[:-5]
    line =  [x.rsplit(' ', 1) for x in line]
    line = [x[:-1] for x in line]
    line = [y.strip(' ') for x in line for y in x]

    diction[bag_key] = line[1:]

#Dictionary now looks like: {'bright white': ['1 shiny gold'],
                             #'dark olive': ['3 faded blue', '4 dotted black'], etc.

#Alphabetizes the dictionary
pprint.pprint(diction)

good_bags = []
#List to keep track of bags containing Shiny gold.
count = 0
def deep_search(search_bag, dictionary):
    
    global count
    global good_bags
    
    for bag, rules in dictionary.items():
        bag_rules = []
        
        for x in rules:
            val, rule = x.split(' ', 1)
            bag_rules.append(rule)
            #Split the number from color, and append color to our Bag_rules list.
        if search_bag in bag_rules:
            print('Found one, bag =', bag, ', searching for', search_bag, ', in', bag_rules, count)
            if bag not in good_bags:
                good_bags.append(bag)
                count +=1
                deep_search(bag, dictionary)
                #Recursion happens here.
                #By changing search bag function to the current 'good bag', 
                #we now search through the beginning of the dictinory again,
                #looking for the "good bag". Meaning, the function doesn't just
                #search for "shiny gold", it now knows which bags contain shiny gold,
                #and searches for those bags.
                #Once it searches for our new bag throughout the whole dictionary,
                #it goes bag to searching for shiny gold, from the beginning of the dictionary, and repeats.
                
    return count


print('Bags containing Shiny Gold:', deep_search('shiny gold', diction))
