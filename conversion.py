#Task:4 conversions

dec= int(input('enter 1 for hour conversion and 2 for minute conversion:'))
if dec == 1:
    hour= int(input('enter hour: '))
    conv = hour * 60
    print('the hour is converted to minute: ', conv)
    
elif dec == 2:
    min= int(input('enter minute: '))
    conv = min / 60
    print('the minute is converted to hour: ', conv)
