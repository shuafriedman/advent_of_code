def xmas_next_letter(current_letter):
    word = ['X', 'M','A','S']
    i = word.index(current_letter)
    return word[i+1]
            
    
def check_next_pos_and_direction(
    doc,dir,pos, cur_letter,
    amount_of_cols, amount_of_lines
):
    total = 0
    next_letter_in_xmas = xmas_next_letter(cur_letter)
    next_position = doc[pos[0]][pos[1]]
    if next_position == None:
        return total
    if next_position == 'S' and next_letter_in_xmas == 'S':
        return total + 1
    if next_position != next_letter_in_xmas:
        return total
    else:
        next_positions = check_adjacent_for_next_letter(tuple(pos), amount_of_cols, amount_of_lines)
        if next_positions.get(dir):
            total+= check_next_pos_and_direction(
                doc,dir,next_positions[dir],next_letter_in_xmas, amount_of_cols, amount_of_lines
            )
        return total
            
def check_adjacent_for_next_letter(
    cur_pos:tuple, amount_of_cols, amount_of_lines
    ):
    found = {}
    #up
    found["up"] = (cur_pos[0] - 1, cur_pos[1]) if cur_pos[0] !=0 else None
    #down
    found["down"] = (cur_pos[0]+1, cur_pos[1]) if cur_pos[0] != amount_of_cols-1 else None
    #right
    found["right"] = (cur_pos[0], cur_pos[1]+1) if cur_pos[1] != amount_of_lines-1 else None
    #left
    found["left"] = (cur_pos[0], cur_pos[1]-1) if cur_pos[1] != 0 else None
    #up_left
    if found["up"] is not None and found["left"] is not None:
        found["up_left"] = (found["up"][0], found["left"][1])
    else:
        found["up_left"] = None
    
    # up_right
    if found["up"] is not None and found["right"] is not None:
        found["up_right"] = (found["up"][0], found["right"][1])
    else:
        found["up_right"] = None
    
    # down_left
    if found["down"] is not None and found["left"] is not None:
        found["down_left"] = (found["down"][0], found["left"][1])
    else:
        found["down_left"] = None
    
    # down_right
    if found["down"] is not None and found["right"] is not None:
        found["down_right"] = (found["down"][0], found["right"][1])
    else:
        found["down_right"] = None
    return {key: val for key,val in found.items() if val}



with open("2024/4.txt", 'r') as f:
    doc = f.readlines()
doc = [f.strip() for f in doc]
puzzle_a_count= 0
puzzle_b_count = 0
amount_of_lines = len(doc)
amount_of_cols = len(doc[0])
for i in range(amount_of_lines):
    for n in range(amount_of_cols):
        #puzzle A
        if doc[i][n] == 'X':
            next_positions  = check_adjacent_for_next_letter(
                (i,n),amount_of_lines, amount_of_cols
            )
            for dir, pos in next_positions.items():
                puzzle_a_count+= check_next_pos_and_direction(
                    doc, dir, pos, 'X', amount_of_cols, amount_of_lines
                )
        if doc[i][n] == 'A':
            positions = check_adjacent_for_next_letter(
                (i,n), amount_of_lines, amount_of_cols
            )
            cross_pos = ['up_right', 'up_left', 'down_right', 'down_left']
            if all(
                [positions.get(dir) for dir in cross_pos]
            ):
                if all(
                    [
                        (
                            (
                                doc[positions['up_right'][0]][positions['up_right'][1]] == 'S' and \
                                doc[positions['down_left'][0]][positions['down_left'][1]] == 'M'
                            )
                            or
                            (
                                doc[positions['up_right'][0]][positions['up_right'][1]] == 'M' and \
                                doc[positions['down_left'][0]][positions['down_left'][1]] == 'S'
                            )
                        ),
                        (
                            doc[positions['up_left'][0]][positions['up_left'][1]] == 'M' and \
                            doc[positions['down_right'][0]][positions['down_right'][1]] == 'S'
                        )
                        or
                        (
                            doc[positions['up_left'][0]][positions['up_left'][1]] == 'S' and \
                            doc[positions['down_right'][0]][positions['down_right'][1]] == 'M'
                        )
                    ]
                ):
                    puzzle_b_count+=1  
print(puzzle_a_count)
print(puzzle_b_count)

    