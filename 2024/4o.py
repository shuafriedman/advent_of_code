directions = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1),
        (1,-1),
        (1,1),
        (-1,-1),
        (-1,1)
    ]

with open("2024/4.txt", 'r') as f:
    doc = f.readlines()
word = ['X', 'M', 'A','S']
doc = [x.strip() for x in doc]
count = 0
amount_of_lines = len(doc)
amount_of_cols = len(doc[0])
for l in range(amount_of_lines):
    for c in range(amount_of_cols):
        if doc[l][c] == word[0]:
            for dir_l, dir_c in directions:
                next_l, next_c = l, c
                xmas = True
                for i in range(len(word)):
                    if (
                        next_l < 0 or next_c <0 
                        or next_l>=amount_of_lines or next_c>= amount_of_cols 
                        or doc[next_l][next_c] != word[i]
                    ):
                        xmas = False
                        break
                    next_l+=dir_l
                    next_c+=dir_c
                if xmas == True:
                    count+=1
print(count)   
                    
                
                
                 