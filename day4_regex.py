import collections
import re
valid = 0
#diction = {}
attrib_set = ['byr', 'iyr','hgt', 'ecl', 'pid', 'eyr', 'hcl']
attrib_cid = ['byr', 'iyr', 'cid','hgt', 'ecl', 'pid', 'eyr', 'hcl']
key_set = []

# =============================================================================
#     list_1 = file.read()
#     string_1 = list_1.split('\n\n')
#     #print(string_1)
#     string_2 = [x.replace('\n', ' ') for x in string_1]
#     #print(string_2)
#     string_3 = [x.split() for x in string_2]
# =============================================================================
data = open('input4.txt').read().split('\n\n')
data = [x.replace('\n', ' ').replace(' ', ', ').split(', ') for x in data]
for x in data:
    key_set=[]
    diction = {}
    for y in x:
        attribute, value = y.split(':')
        diction.setdefault(attribute)
        diction[attribute] = value
    for key in diction:
        key_set.append(key)

    if collections.Counter(attrib_set) == collections.Counter(key_set) or collections.Counter(attrib_cid) ==collections.Counter(key_set):
        valid += 1
        
print(valid)

#Partb
with open('input4.txt') as file:    
      
    list_1 = file.read()
    string_1 = list_1.split('\n\n')
    #print(string_1)
    string_2 = [x.replace('\n', ' ') for x in string_1]
    #print(string_2)
    string_3 = [x.split() for x in string_2]
    
    valid = 0
    for x in string_3:
        key_set=[]
        diction = {}
        for y in x:
            attribute, value = y.split(':')
            diction.setdefault(attribute)
            diction[attribute] = value
        for key in diction:
            key_set.append(key) 
            
        attrib_set = ['byr', 'iyr','hgt', 'ecl', 'pid', 'eyr', 'hcl']
        attrib_cid = ['byr', 'iyr', 'cid','hgt', 'ecl', 'pid', 'eyr', 'hcl']
        
        works = 'no'
        if collections.Counter(attrib_set) == collections.Counter(key_set) or collections.Counter(attrib_cid) ==collections.Counter(key_set):
            works ='yes'
            if not len(str(diction['byr'])) == 4  or not 1920 <= int(diction['byr']) <= 2003:
                works = 'no'
            if not len(str(diction['iyr'])) == 4  or not 2009 <= int(diction['iyr']) <= 2020:  
                works = 'no'
            if not len(str(diction['eyr'])) == 4  or not 2020 <= int(diction['eyr']) <= 2030:
                works = 'no'
            if not re.match('^\d*(cm|in)$', diction['hgt']):
                works ='no'
            if 'cm' in diction['hgt']:
                if not 150 <= int(diction['hgt'].replace('cm', '')) <= 193:
                    works = 'no' 
            if 'in' in diction['hgt']:
                if not 59 <= int(diction['hgt'].replace('in', '')) <= 76:
                    works = 'no'
            if not re.match("^^#[0-9a-f]{6}$", diction['hcl']):
                works = 'no'
            if not re.match('^(amb|blu|brn|gry|grn|hzl|oth)', diction['ecl']):
                works = 'no'
                
            if not re.match('^[0-9]{9}$', diction['pid']):
                works= 'no'
            
        else:
            works = 'no'
            
        if works == 'yes':
            valid += 1

print(valid)
  

