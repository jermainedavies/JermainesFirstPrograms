user_num = int(input("which number would you like to check?"))

def devisible_by_both():
    if user_num %3 == 0 and user_num %5 == 0:
        print("your number is divisible by both")
    else:
         print("your number is not divisible by both")