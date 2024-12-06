#1: Break up the file into three sections: Rules, Your Ticket, and nearby tickets.
input = open('input_16.txt').read().strip().split('\n\n')
rules, your_ticket, nearby_tickets = input
rules = rules.split('\n')
rules = [x.split(':') for x in rules]
rules_range = [x[1].strip().split(' ') for x in rules]
total_nums = set()
for x in rules_range:
    range1 = x[0].split('-')
    range2 = x[2].split('-')
    for num in range(int(range1[0]) , int(range1[1])+1):
        total_nums.add(num)
    for num in range(int(range2[0]), int(range2[1])+1):
        total_nums.add(int(num))

#2 breakup nearby ticekts, by line, and check each number in each ticket for any numbers not in the rules list.
nearby_tickets = nearby_tickets.split(':')
nearby_tickets = nearby_tickets[1].split('\n')
nearby_tickets.pop(0)

sum = 0
for line in nearby_tickets:
    line = line.split(',')
    for num in line:
        if int(num) not in total_nums:
            sum +=int(num)
print(sum)
        


