# Task: sum nymbers divisible  by 3

num = int(input('enter the range ending:'))
sum = 0
for i in range(1, num):
    if i % 3 == 0:
        sum += i
        
print('the total sum is:',sum)