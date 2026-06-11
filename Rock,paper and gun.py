import random
while True:
    user_action=input("Enter a choice(rock,paper,sissors):")
    possible_actions=["rock","paper","sissors"]
    computer_action=random.choice(possible_actions)
    print(f"\nYou chose {user_action} ,computer chose {computer_action} .\n")
    if user_action == computer_action:
        print(f"both players selected{user_action}.It is a tie")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("rok smashes sissors! you win!")
        else:
            print("Paper covers rock you lose!")
    elif user_action=="paper":
        if computer_action=="rock":
            print("Paper covers rock you win !")
        else:
            print("Sissors cut papers you lose!")
    elif user_action=="sissors":
        if computer_action=="paper":
            print("sissors cut paper you win !")
        else:
            print("Rock smashes sissors you lose !")
    play_agian=input("play agian?(y/n):")
    if play_agian !="y":
        break
        
