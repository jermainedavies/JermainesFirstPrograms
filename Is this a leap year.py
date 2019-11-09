year = input('which year do you want to check?')
year_num = int(year)

if year_num % 4 == 0:
    print("this is a leap year")
    
else:
    print("this is not a leap year")