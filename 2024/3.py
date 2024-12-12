with open('2024/3.txt', 'r') as f:
    f = f.readlines()

def maybe_in_mul(char, line_length):
    if char not in ['m', 'u', 'l', '(']:
        return False
    if char == 'm':
        # current_mul.append(char)
        return True
    elif char == 'u' and line_length == 1:
        # current_mul.append(char)
        return True
    elif char == 'l' and line_length == 2:
        # current_mul.append(char)
        return True
    elif char == '(' and line_length == 3:
        # current_mul.append(char)
        return True
    return False
def calculate_mul(mul):
    mul = ''.join(mul)
    x, y = map(int, mul.split(','))
    return x*y

def look_and_do_mul(
    mul_started, in_mul, count, current_mul, inside_mul
):
    length_of_current_mul = len(current_mul)
    if in_mul == True:
        if char == ')':
            mul = calculate_mul(inside_mul)
            count+=mul
            current_mul= []
            inside_mul = []
            in_mul = mul_started = False
        elif char.isdigit() or char == ',':
            inside_mul.append(char)
        else:
            current_mul= []
            inside_mul = []
            in_mul = mul_started = False
        
    elif mul_started:
        if in_mul == False:
            if char == '(' and length_of_current_mul == 3:
                in_mul = True
            elif mul_started == maybe_in_mul(char, length_of_current_mul):
                if mul_started == True:
                    current_mul.append(char)
            else:
                current_mul = []
                inside_mul = []
                in_mul = mul_started = False       

    if mul_started == False:
        mul_started = maybe_in_mul(char, length_of_current_mul)
        if mul_started == True:
            current_mul.append(char)
    
    return mul_started, in_mul, count, current_mul, inside_mul

def contains_do(line):
    line = ''.join(line)
    return True if line.__contains__('do()') else False
def contains_dont(line):
    line = ''.join(line)
    return False if line.__contains__('don\'t()') else True

mul_started = False
in_mul = False
count = 0
do = True
do_list = []
for line in f:
    current_mul = []
    inside_mul = []
    for char in line:
        do_list.append(char)
        if do:
            do = contains_dont(do_list)
            if do == False:
                do_list = []
            mul_started, in_mul, count, current_mul, inside_mul = look_and_do_mul(
                mul_started, in_mul, count, current_mul, inside_mul
            )

        elif not do:
            do = contains_do(do_list)
            if do ==True:
                do_list = []
                        
print(count)     
        
            
            