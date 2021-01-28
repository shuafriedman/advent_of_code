mylist=[]
total_passwords= 0

## 1) Iterate through each line, seperating each element into one list.
with open("Day2.txt") as a_file:
  for line in a_file:
      #Not sure why, but the txt file adds a '\n' when added to python.
      #Need to use 'strip' to remove from each line.
      line = line.strip('\n')
## 2) Set each element of the line as a variable.
      range1, letter, password = line.split()
      letter = letter[0]
      min, max = range1.split('-')
          #Because the digits of the min and max change, we need to split out
          # the '-', to make the min and max into two different str.
      print (min, max, letter, password)
      
## 3) check how many times 'letter' is in password.
      amount= 0
      for x in password:
          if x == letter:
              amount = amount + 1
      print(amount)
## If function to check for the criteria given. Ranges is str, need int.             
      if amount >= int(min) and amount <= int(max):
          total_passwords = total_passwords + 1
          print(password)
print(total_passwords)

