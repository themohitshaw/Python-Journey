#Create a list that containg the table of 5

a = 5
table = []
for i in range(1,11):
    table.append(a*i)

print(table)


#This progarm in one line by list comprehension

table = [5*i for i in range (1,11)]
print(table)