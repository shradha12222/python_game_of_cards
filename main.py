import random
from idlelib.editor import darwin
from os import system
from art import logo

def deal_card():
    card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(card)
    return card
def calculate_score(card):
    if sum(card) == 21 and len(card) == 2:
        return 0

    if 11 in card and sum(card) > 21:
            card.remove(11)
            card.append(1)
    return sum(card)
def compare(user,computer):
    if user == computer:
        return "draw"
    elif computer ==0:
        return "loss oponent"
    elif user==0:
        return "win woth black jag"
    elif computer > 21:
        return "oponent win"
    elif user > 21:
        return "you lose"
    elif user < computer:
        return "you win"
    else:
        return "you lose"
def play_game():
    print(logo)
    user_card=[]
    computer_card=[]
    is_game_over=False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        computer=calculate_score(computer_card)
        user=calculate_score(user_card)
        print(f"user cards are  {user_card} and socure is {user}")
        print(f"computer cards are  {computer_card} and  socure is {computer}")
        if user == 0 or computer == 0 or user >21:
            is_game_over=True
        else:
            ask=input("yes if you want to continue and no for passing")
            if ask == "yes":
                user_card.append(deal_card())
            else:
                is_game_over=True
    while computer != 0 and computer < 17:
        computer_card.append(deal_card())
        computer=calculate_score(computer_card)
    print(f"computer's final card is {computer_card}and scoure is { computer}")
    print(f"user final card is {user_card}and scoure is {user}")
    print(compare(user,computer))
while input("Do you want to play game ? (yes/no)").lower() == "yes":
    system('cls')
    play_game()
