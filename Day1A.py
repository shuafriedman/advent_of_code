import pandas as pd
df = pd.read_excel(r'C:\Users\sfrie\Downloads\Book1.xlsx', sheet_name='Sheet1')
mylist= df['Numbers'].tolist()

for entry in mylist:
    for num2 in mylist:
        if entry + num2 == 2020:
            print(entry, num2)
            print(entry*num2)
            
    