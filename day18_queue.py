#Part A from Dylan Codes Youtube Channel

with open('input18.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def eval(num1, num2, operator):
    if operator =='+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    
def simplify_parta(expr):
    while len(expr) > 1 :
        num1 = int(expr.pop())
        operator = expr.pop()
        num2 = int(expr.pop())
        result = eval(num1, num2, operator)
        expr.append(str(result))
    
    return expr[0] #return the simplified number

def simplify_partb(expr):
    while '+' in expr:
        num1 = int(expr.pop())
        operator = expr.pop()
        num2 = int(expr.pop())
        if operator == '+':
            result = num1 + num2
            expr.append(str(result))
        if operator == '*':
            expr.insert(0, operator)
            expr.insert(0, num1)
            expr.append(num2)
    result = simplify_parta(expr)        
    return expr[0]        


total = 0
for line in data:
    line = line.replace('(', '( ')
    line = line.replace(')', ' )')
    expr = line.split()
    #We will implement a LIFO structure (stack). The most recently added item to the stack will be the first item out of it, and vice versa.
    #sample stack: 3+2+1. once we hit a ')', we will pop from the stack to get the last in, until we hit the '(', and simplify that expression.
    stack = []

    # ['9', '*', '8', '+', '2', '+', '(', '4', '*', '(', '2', '*', '2', '+', '9', '*', '2', ')', '*', '9', '*', '3', '*', '8', ')', '+', '8', '*', '5']
    for char in expr:
        if char.isdigit() or char in ['*', '+', '(']:
            stack.append(char)
        elif char == ')':
            #the goal here with the following "ordered list" will be to add things into it until we find an open paranthesis. We will simplify each expression
            # within brackets, and append it to a new list. This list will be an expression, of all sums, without brackets, in the proper order of operations.
            ordered = []
            while stack[len(stack)-1] != '(':
                ordered.append(stack.pop()) 
            stack.pop() #this removes the open paranthesis
            #result = simplify_parta(ordered)
            result = simplify_partb(ordered)
            stack.append(result) #Now, stack consists of all numbers and operators before '(', and the simplified expression within the brackets.
    #Now that we have our unbracketed expression, we need to calculuate the total. The rules require us to go from left to right. Our current
    # simplify and eval functions calculate from right to left. Instea of making a new function to sum the total, we can reverse the order of the stack.
    
    # #partA
    # stack.reverse()
    # result = simplify_parta(stack)
    # total += int(result)
    
    #part B
    stack.reverse()
    result = simplify_partb(stack)
    total += int(result)
print(total)