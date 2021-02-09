import re
import pprint

###Make dictionary of the data
with open(r'Day7.txt') as file:
    list_ = file.readlines()
    list_ = [y.strip() for y in list_]
    new_line = [re.split(r"contain|\,", line) for line in list_]


diction = {}
for line in new_line:
    bag_key = line[0].strip()
    bag_key = bag_key[:-5]
    line =  [x.rsplit(' ', 1) for x in line]
    line = [x[:-1] for x in line]
    line = [y.strip(' ') for x in line for y in x]

    diction[bag_key] = line[1:]

###Dictionary now looks like: {'bright white': ['1 shiny gold'],
                             #'dark olive': ['3 faded blue', '4 dotted black'], etc.

pprint.pprint(diction) 
#Alphabetizes the dictionary


###PART A
### Searching throughout the Rules list to see how many bags can contain Shiny Gold.
    #1) Create a for loop to split the Rule, by its bags.
    #2) Split the bags into values and colors.
good_bags = []
#List to keep track of bags containing Shiny gold.
count = 0
def deep_search(search_bag, dictionary):
    
    global count
    global good_bags
    
    for bag, rules in dictionary.items():
        bag_colors = []
        
        for x in rules:
            val, rule = x.split(' ', 1)
            bag_colors.append(rule)
            ###Split the number from color, and append color to our Bag_rules list.
            ###This lets us check if Shiny Gold is in this rules current colors.
        if search_bag in bag_colors:
            #print('Found one, bag =', bag, ', searching for', search_bag, ', in', bag_rules, count)
            if bag not in good_bags:
                ###filters out "redundant bags, to avoid double counting.
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
                #When it gets to "No other", the end of the current loop, it goes back
                #to the next relevant level.
                
    return count

###Part B
### Creating a function that will count all bags in Shiny Gold by:
    #1) loop through each bag in the current rules list:
    #2) Recurse through each level of depth, multiplying the bottom most total of bags
        # by the amount of bags holding it.
    # AFter the recursive iteration, the function will return the total amount.
    

#import inspect
def total_bags(bag_search):
    rules_list = bag_search
    total = 1
    global num
    for x in rules_list:
        #print('level', len(inspect.stack(0)) - 31)
        ###checks recursion depth
       
        #print(x, sg, total)
        value, color= x.split(' ', 1)
        
        if color == 'other':
            return 1
        
        else:
            total+= int(value) * total_bags(diction[color]) 
            #Because I didn't return the function again, rather I called it again,
            #this allows for the tree traversal.
    return total     
 

print('Bags containing Shiny Gold:', deep_search('shiny gold', diction))      
print('Total bags in Shiny Gold:', total_bags(diction['shiny gold']) -1)
###I need to do "-1" here, as to not count the Shiny Gold bag, I believe.







