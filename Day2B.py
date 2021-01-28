mylist=[]
total_passwords= 0
password_list =[]

## 1) Iterate through each line, seperating each element into one list.
with open("Day2.txt") as a_file:
  for line in a_file:
      
      line = line.strip('\n')
      print(line)
## 2) Set each element of the line as a variable.
      range1, letter, password = line.split()
      letter = letter[0]
      min, max = range1.split('-')
      min = int(min)-1
      max = int(max)-1
          #Because the digits of the min and max change, we need to split out
          # the '-', to make the min and max into two different str.
      if password[(min)] == letter and password[(max)] !=letter:
         total_passwords = total_passwords + 1
         password_list.append(password)
         print (min, max, letter, password)
      if password[(max)] == letter and password[(min)] !=letter:
         total_passwords = total_passwords + 1
         password_list.append(password)
         print (min, max, letter, password)
         
print(total_passwords)
print(password_list)
print(len(password_list))

