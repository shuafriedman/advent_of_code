def file():
    with open(r'Day9.txt') as file:
        file = file.readlines()
        file = [int(x.strip('n')) for x in file]
        return file
#print(file())


lists = [35, 20, 15, 25, 47,40,62,55,65,95,102, 117, 150, 182, 127]
numbers = [1,2,3,4,5,6,7,8,9,10]

def check_numbers(num_range: 'int', data):
    #print(lists)
    while len(data) >= num_range:
            good_list = []
            boolean = False
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
            
def contiguous(bad_number: 'function', data):
    #print(data)
    
    for num in data:
        good_list = []
        total = num
        for x in data:
            if x !=num:
                total+= x
                good_list.append(x)
                #print('list:', good_list)
                #print(total)
                #print(bad_number)
                
                if total == bad_number:
                    good_list.append(num)
                    #print('bad_number:', bad_number, good_list)
                    return good_list
        data.pop(0)
                
parta = check_numbers(25, file())
#print(parta)
print(contiguous(parta, file()))