#Task: grade calculator

obt_marks = int(input("Enter obtained marks: "))
tot_marks = int(input("Enter total marks: "))
# Calculating percentage
percent = (obt_marks / tot_marks) * 100
print('Your percentage is:',percent)
if percent >= 80:
    print("Your grade is: A+")
elif percent >= 70 and percent < 80:
    print("Your grade is: A")
elif percent >= 60 and percent < 70:
    print("Your grade is: B")
elif percent >= 50 and percent < 60:
    print("Your grade is: C")
elif percent >= 40 and percent < 50:
    print('Your grade is: D')
elif percent < 40 and percent >= 0:
    print("Your grade is: F")
