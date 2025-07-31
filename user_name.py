#Task: user name builder from full name
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
user_name = f_name + l_name
print("Your username is: ", user_name.lower())
print("Your username is: ", user_name.upper())
user_name= '_'.join(user_name.split())
print("Your username is: ", user_name.split())

