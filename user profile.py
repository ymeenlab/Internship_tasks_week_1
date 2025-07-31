# Task: user profle summary 
name= input('enter your complete name:')
age= input('enter your age:')
study= input('enter your qualification:')
email= input('enter your email:')
Add1= input('enter your country:')
Add2= input('enter your city:')
Add3= input('enter your area:')
Add4= input('enter your home location:')
address= (f"{Add4} {Add3} {Add2} {Add1}")
print('your profile summary is:')
print('Name:',name)
print("age:",age)
print("qualification:",study)
print("Email:",email)
print("Address:",address)


# Task: swapping variable's value without using any third variable

num = 32
num2 = 60
num , num2 = num2 , num
print(num) 
print(num2)