import random
 
guess = (input("enter a number between 1 and 10"))

score = 0
 
rand = random.randint(1,10)

while True:
    if guessed_int == "b":
        break
        print("game over")
    if guess == rand:
        score +=10
        print("well done, your score is:", score)
        print("The random number was", rand
    elif guess != rand:
        print("Sorry, you didn't guess correctly. Try again!")
        print("The random number was", rand)