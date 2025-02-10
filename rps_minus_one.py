import random
"""
Name: Aiden P.
File: rps_minus_one.py
Description: Implements Rock Paper Scissors Minus One from Squid Game
"""

"""
Pseudo Code
- Have computer pick RPS twice randomly
- Set both player's score to 0
- Store values in comp_hand
- Ask Users for their hands
- Store values in player_hand
- Ask user which hand to keep
- Remove a variable
- Computer randomly chooses which hand to keep
- Evaluate who wins
- Update score
- Ask user if they want to play again
- If they quit, print scores and end game
- otherwise play again
"""

def comp_hand():
    hand1 = (random.randint(1,3))
    hand2 = (random.randint(1,3))
    if hand1 == 1:
        compint = "Rock"
    elif hand1 == 2:
        compint = "Paper"
    elif hand1 == 3:
        compint = "Scissors"
    if hand2 == 1:
        compint2 = "Rock"
    elif hand2 == 2:
        compint2 = "Paper"
    elif hand2 == 3:
        compint2 = "Scissors"
    return[compint,compint2]

def player_hand():
    handinput = input("What are you gonna throw first?: ")
    handinput2 = input("What are you gonna throw next?: ")

    return[handinput.capitalize(),handinput2.capitalize()]

def take_away(hand_input):
    remove = input("What hand would you like to take away?, Left or Right?: ")
    if remove.capitalize() == "Right":
        del(hand_input[1])
    elif remove.capitalize() == "Left":
        del(hand_input[0])
    return(hand_input)
def comp_away(comp_hand):
    compremove = (random.randint(1,2))
    if compremove == 1:
        del(comp_hand[1])
    elif compremove== 2:
        del(comp_hand[0])
    return(comp_hand)

def main():
    score = 0
    player_choices = player_hand()
    comp_choices = comp_hand()
    print(f"The computer chose :{comp_choices}")
    print(f"You chose {player_choices}")
    one_hand = take_away(player_choices)
    comp_new_hand = comp_away(comp_choices)
    print(f"Now the computer's hand is {comp_new_hand}")
    print(f"Now your hand is {one_hand}")
    
    if one_hand[0] == "Rock":
        if comp_new_hand[0] == "Rock":
            print("You tied!")
            score = score + 0
        elif comp_new_hand[0] == "Paper":
            print("You lost!")
            score = score - 1
        elif comp_new_hand[0] == "Scissors":
            print("You win!")
            score = score + 1
    elif one_hand[0] == "Paper":
        if comp_new_hand[0] == "Rock":
            print("You win!")
            score = score + 1
        elif comp_new_hand[0] == "Paper":
            print("You tied!")
            score = score + 0
        elif comp_new_hand[0] == "Scissors":
            print("You lost!")
            score = score - 1
    elif one_hand[0] == "Scissors":
        if comp_new_hand[0] == "Rock":
            print("You lost!")
            score = score - 1
        elif comp_new_hand[0] == "Paper":
            print("You win!")
            score = score + 1
        elif comp_new_hand[0] == "Scissors":
            print("You tied!")
            score = score + 0

        
    play_again = input("Play again?: ")
    if play_again.capitalize() == "Yes":
        return(main())
    elif play_again.capitalize() == "No":
        print(f"Good Game! \nYour score was {score}")
        exit()



        
main()









