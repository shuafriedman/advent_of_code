import timeit
def look_ahead_on_same_line(doc, line_i, col_i):
    if doc[line_i][col_i + 1] == 'M' \
        and doc[line_i][col_i +2] == 'A' \
        and doc[line_i][col_i +3] == 'S': \
        return 1
    return 0
def look_back_on_same_line(doc, line_i, col_i):
    if doc[line_i][col_i -1] == 'M' \
        and doc[line_i][col_i -2] == 'A' \
        and doc[line_i][col_i -3] == 'S': \
        return 1 
    return 0
def look_up_on_all_lines(doc, line_i, col_i):
    if (doc[line_i-1][col_i] == 'M' and line_i > 0) \
        and (doc[line_i-2][col_i] == 'A' and line_i >1) \
        and doc[line_i-3][col_i] == 'S': \
        return 1 
    return 0
def look_down_on_all_lines(doc, line_i, col_i):
    if doc[line_i+1][col_i] == 'M' \
        and doc[line_i+2][col_i] == 'A' \
        and doc[line_i+3][col_i] == 'S': \
        return 1
    return 0
def look_up_right(doc, line_i, col_i):
    if doc[line_i+1][col_i+1] == 'M' \
        and doc[line_i+2][col_i+2] == 'A' \
        and doc[line_i+3][col_i+3] == 'S': \
        return 1
    return 0
def look_up_left(doc, line_i, col_i):
    if doc[line_i+1][col_i-1] == 'M' \
        and doc[line_i+2][col_i-2] == 'A' \
        and doc[line_i+3][col_i-3] == 'S': \
        return 1
    return 0
def look_down_left(doc, line_i, col_i):
    if doc[line_i-1][col_i-1] == 'M' \
        and doc[line_i-2][col_i-2] == 'A' \
        and doc[line_i-3][col_i-3] == 'S': \
        return 1
    return 0
def look_down_right(doc, line_i, col_i):
    if doc[line_i-1][col_i+1] == 'M' \
        and doc[line_i-2][col_i+2] == 'A' \
        and doc[line_i-3][col_i+3] == 'S': \
        return 1
    return 0
     
def main():
    with open("2024/4.txt", 'r') as f:
        orig_doc = f.readlines()
    orig_doc = [x.strip() for x in orig_doc]
    count = 0
    amount_of_lines = len(orig_doc)
    amount_of_cols = len(orig_doc[0])
    
    dots= ['.'] * amount_of_cols
    orig_doc.insert(0, dots)
    orig_doc.append(dots)
    doc = []
    for line in orig_doc:
        line = list(line)
        line.insert(0, '.')
        line.append('.')
        doc.append(line)
    for line_i in range(amount_of_lines+1): # [0,1,2,3,4,5,6,7,8,9]
        line = list(doc[line_i])
        for col_i in range(1, amount_of_cols+1): # [0,1,2,3,4,5,6,7,8,9]
            print(doc[line_i][col_i])
            if doc[line_i][col_i] == 'X':
                count+= look_ahead_on_same_line(doc, line_i, col_i)
                count+= look_back_on_same_line(doc, line_i, col_i) 
                count+= look_down_on_all_lines(doc, line_i, col_i)
                count+= look_up_on_all_lines(doc, line_i, col_i)
                count+= look_down_right(doc, line_i, col_i)
                count+= look_down_left(doc, line_i, col_i)
                count+= look_up_left(doc, line_i, col_i)
                count+= look_up_right(doc, line_i, col_i)
            else:
                pass
    print(count)
print(timeit.timeit(main, number=1))

    