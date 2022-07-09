from random import choice
activate = True
s = ["rock", "paper", "scissors"]
while activate:
    user_choice = s[int(input("Please select your handsigns 0.rock 1.paper 2.scissors\n"))]
    com_choice = choice(s)
    if user_choice == com_choice:
        print("draw\n")
    else:
        if user_choice == "rock":
            if com_choice == "paper":
                print("you lose\n")
            else:
                print("you won\n")
        elif user_choice == "paper":
            if com_choice == "scissors":
                print("you lose\n")
            else:
                print("you won\n")
        else:
            if com_choice == "rock":
                print("you lose\n")
            else:
                print("you won\n")
    conti = input("Do you wish to continued? yes/no")
    if conti == "no":
        activate = False
    