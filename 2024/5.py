

with open('2024/5.txt', 'r') as f:
    rules, updates  = f.read().split("\n\n")
rule_dict = {}
for rule in rules.split('\n'):
    prior, post = rule.split('|')
    rule_dict[prior] = rule_dict.get(prior, [])
    rule_dict[prior].append(post)
updates = [update.split(',') for update in updates.split('\n')]
count = 0
invalid_corrected_count = 0
for update in updates:
    valid = True
    fixed_update = update.copy()
    for i in range(len(update)):
        rules = rule_dict.get(update[i])
        if valid == True:
            if rules:
                for rule in rules:
                    if rule in update[:i]:
                        valid = False
                        break 
                         
    if valid == True:
        count+= int(update[len(update) // 2]) 
    else:
        i=0
        while i < len(fixed_update):
            rules = rule_dict.get(fixed_update[i])
            if not rules:
                i+=1
            else:
                index = i
                updated = False
                for rule in rules:
                    while index>=0 and rule in fixed_update[:index]:
                        updated = True
                        fixed_value = fixed_update[index]
                        fixed_update[index] = fixed_update[index-1]
                        fixed_update[index-1] = fixed_value 
                        index -=1
                if updated:
                    i = index
                else:
                    i+=1
        num = int(fixed_update[len(fixed_update) // 2])
        invalid_corrected_count+=num
           
print(count)
print(invalid_corrected_count)

# for invalid in invalid_updates:
#     for i in range(len(invalid)):
#         rules = rule_dict.get(invalid[i])
#         if rules:
#             for rule in rules:
#                 if rule in update[:i]:
#                     fixed_update[i-1] = rule
#                     fixed_update[i] = update[i-1]
#                     num = int(fixed_update[len(fixed_update) //2])
#                     invalid_corrected_count+=num