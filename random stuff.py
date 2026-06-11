import random
playing=True
number=str(random.randint(0,9))
print("I will generate a number from 0 to 9, and you have to guss the number one digit at a time.")
print("you win when you guss the corrcet number")
while playing:
    guess=input("Give me your best guss! \n")
    if number==guess:
        print("YOU WIN!!!")
        print("the number was",guess)
    else:
        print("this isent right, try again.\n")


