# Task: password strength clasifier

import re
password = str( input('Enter your password;'))
score = 0
neg = 0
if len(password)>=8 :
    score += 1
else: 
    neg += 1
    print('length shpould be more then or equal to 8 letters and symbols')
if  any(char.isupper() for char in password) :
    score += 1
else:
    neg += 1
    print('enter atleast 1 uppercase letter')
if any(char.islower() for char in password):
    score += 1
else:
    neg += 1
    print('password should contain at least 1 lowercase character')
if any(char.isdigit() for char in password):
    score += 1
else:
    neg += 1
    print('password should contain atleast 1 digit')

special_characters = ":;!@#$%^&*_-.,"
if any(char in special_characters for char in password):
    score += 1
else: 
    neg += 1
    print('1 special character must be used')   
if score ==5 and neg==0:
    print('strong password')
elif score < 5 and score>= 4 and neg ==1:
    print('normal password')
elif score<4 and neg >=2:
    print('weak password')    
     
    


