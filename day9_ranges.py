file = open('input9.txt').read().split()
numbers = [int(x) for x in file]



def search(range_len, number):
    for start in range(range_len):
        start = numbers[start]
        for x in numbers[:range_len]:
            if x != start:
                if x + start == number:
                    return True 
def return_search(range_len):
    minmax = []
    for number in numbers[range_len:]:
        if search(range_len, number) == None:
            for x in numbers[:25]:
                #minmax.append(x)
                return number
        else:
            numbers.pop(0)
print(return_search(25))