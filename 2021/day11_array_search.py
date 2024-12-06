#Code is from Dylan Codes Youtube channel.
file =  open('input11.txt')
olddata = file.readlines()
#sparse the data to make a border of '.'s around it, to easier validate the check.
top_bottom_border = ('.'*(len(olddata[0])-1))
olddata.append(top_bottom_border)
olddata.insert(0, top_bottom_border)
olddata = [list(line.strip()) for line in olddata]

data = []
for line in olddata:
    line.append('.')
    line.insert(0, '.')
    data.append(line)

#function to retrieve for each node, the count of adjacent '#'s.
def get_adjacent_count(cr, cc):
    count = 0
    #left
    if data[cr][cc-1] == '#': count+=1
    #right
    if data[cr][cc+1] == '#':count+=1
    #up
    if data[cr-1][cc] == '#':count+=1
    #up-right
    if data[cr-1][cc+1] == '#':count+=1
    #up-left
    if data[cr-1][cc-1] == '#':count+=1
    #down
    if data[cr+1][cc] == '#':count+=1
    #down-right
    if data[cr+1][cc+1] == '#':count+=1
    #down-left
    if data[cr+1][cc-1] == '#':count+=1              
    return count

#for each node, check the required rules of how many afjacent '#'s are required. Change the node in the new chart accordingly.
def apply_rules():
    new_chart = []
    #append a border row to the top.
    new_chart.append(list('.'*(len(data[0]))))
    for cr in range(1, len(data)-1):
        new_row = []
        #append a border '.' to the beginning of each row.
        new_row.append('.')
        for cc in range(1, len(data[cr])-1):
            seat = data[cr][cc]
            count = get_adjacent_count(cr, cc)
            
            if seat == 'L' and count == 0:
                new_row.append('#')
            elif seat == '#' and count  >= 4:
                new_row.append('L')
            else:
                new_row.append(seat)
        #append border '.' to the end of the row.
        new_row.append('.')
        new_chart.append(new_row)
    #append border row to the end of the chart.
    new_chart.append(list('.'*(len(data[0]))))
    
    #We need to change the data chart variable. Tried carrying over the new_chart variable, but required a global variable
    # to carry to the next function.
    for i in range(len(data)-1):
        data[i] = new_chart[i]
    
#Check if the new_chart (under the variable data, which we overwrited), is the same as the previous chart (data, which has not 
# yet been overwrited until after we run "apply_rules")        
def verify_double_array():
    previous = data.copy()
    apply_rules()
    while data != previous:
        previous = data.copy()
        apply_rules()

    return get_final_count()

def get_final_count():
    count = 0
    for cr in range(len(data)):
        for cc in range(len(data[cr])):
            if data[cr][cc] == '#':
                count +=1
    return count

print(verify_double_array())