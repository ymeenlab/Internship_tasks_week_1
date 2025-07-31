#Task: multiplication table

num = int(input('enter a number to calculate its table:'))
length = int(input('enter the length of table:'))
for i in range(1, length):
   print(num, 'x', i, '=', num*i)