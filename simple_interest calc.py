  #Task; interest calculator

prin = float(input("enter the principal amount:"))
rate = float(input("enter the rate of interest:"))
time = float(input("enter the time period in years:"))
interest = (prin * rate * time) / 100
print("the interest is: ", interest)
print("the total amount is: ", prin + interest)
