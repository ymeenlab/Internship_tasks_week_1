#correctness of badly indented code 
""" num = int(input("Enter a number: "))
    if num % 2 == 0:
    print(f"{num} is an even number.") # Incorrect indentation here
    else:
     print(f"{num} is an odd number.") # Incorrect indentation here"""
     
     #corrected code
num = int(input("Enter a number: "))
if num % 2 == 0:
        print(f"{num} is an even number.")  #corrected indentation here by adding tab before print
else:
        print(f"{num} is an odd number.") # corrected indentation here by adding tab before print
        