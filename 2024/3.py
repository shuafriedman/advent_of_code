with open('2024/3.txt', 'r') as f:
    f = f.readlines()

def maybe_in_mul(char):
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
    
mul_started = False
in_mul = False
count = 0
for line in f:
    current_mul = []
    inside_mull = []
    for char in line:
        line_length = len(current_mul)
        
        if in_mul == True:
            if char == ')':
                mul = calculate_mul(inside_mull)
                count+=mul
                current_mul= []
                inside_mull = []
                in_mul = mul_started = False
            elif char.isdigit() or char == ',':
                inside_mull.append(char)
            else:
                current_mul= []
                inside_mull = []
                in_mul = mul_started = False
            
        elif mul_started:
            if in_mul == False:
                if char == '(' and len(current_mul) == 3:
                    in_mul = True
                elif mul_started == maybe_in_mul(char):
                    if mul_started == True:
                        current_mul.append(char)
                else:
                    current_mul = []
                    inside_mull = []
                    in_mul = mul_started = False       

        if mul_started == False:
            mul_started = maybe_in_mul(char)
            if mul_started == True:
                current_mul.append(char)
                
        
        # if in_mul == False:
        #     mul_started = maybe_in_mul(char)
        #     if mul_started:
        #         current_mul.append(char)
                
        # if mul_started and len(current_mul) == 4:
        #     in_mul = True
        #     mul_started = False
        # else:
        #     current_mul = inside_mull = []
        #     in_mul = mul_started = False 
            
        # if in_mul == True and char != ')':
        #     inside_mull.append(char)
        # elif in_mul == True and char == ')':
        #     mul = calculate_mul(inside_mull)
        #     count+=mul
            
        #     current_mul = inside_mull = []
        #     in_mul = mul_started = False         
           
print(count)     
        
            
            