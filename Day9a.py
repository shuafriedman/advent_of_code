def file():
    with open(r'Day9.txt') as file:
        file = file.readlines()
        file = [int(x.strip('n')) for x in file]
        return file
#print(file())


def check_numbers(num_range: 'int', data):
    #print(lists)
    while len(data) >= num_range:
            good_list = []
            test_list = data[:num_range]
            
            if len(data) >=num_range +1:
                
                test = data[num_range]
                #print('\ntest number:', test)
                #print('test list:', test_list)
                for num in test_list:
                    for x in test_list:
                        if num + x == test:
                            #print('good:', num, '+', x, '=', test)
                            good_list.append(test)
                if good_list == []:
                    return test
                            
              
            data.pop(0)
            
def contiguous(bad_number: 'var', data: 'function'):
    #print(data)
    index_counter = 0
    ### This "pops" this next "first" number of the list.
    ### When I used pop for this puzzle, the iteration index wouldn't reset, therefore it
        # wasn't starting at the beginning of the list like I would like it to. This was
        # a good substitue.
    for num in data:
        good_list = []
        #This will give me, at the end, the list of numbers being added.
        total = num
        index_counter +=1
        
        for x in data[index_counter:]:
            if x != num:
            #Making sure we don't recount the current iterative
                total+= x
                good_list.append(x)
                
                if total == bad_number:
                    good_list.append(num)
                    #print('bad_number:', bad_number, good_list)
                    return 'bad number: ' + str(total), 'sum = ' + str(min(good_list) + max(good_list))
                
parta = check_numbers(25, file())
#print(parta)
print(contiguous(parta, file()))