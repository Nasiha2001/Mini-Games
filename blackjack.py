import art
import random

cards=['K','Q','J',10,9,8,7,6,5,4,3,2,'A']

def deal_cards():
    card_stack=[]
    for i in range(2):
        card_stack.append(random.choice(cards))
    return card_stack

def blackjack(card_stack):
    if 'A' in card_stack and 10 in card_stack:
        return True
    return False

def correction(card_correction,total):
    corrected_cards=[]
    for card in card_correction:
        if card in ['K', 'Q', 'J']:
            corrected_cards.append(10)
        elif card == 'A':
            if total > 21:
                corrected_cards.append(1)
            else: corrected_cards.append(11)
        else: corrected_cards.append(card)
    return corrected_cards

def calculate_score(card_stack,prev_score):
    card_stack=correction(card_stack,prev_score)
    score=sum(card_stack)
    return score

def check_for_win(your_score,computer_score):
    if your_score>21:
        print("More than 21.You lose :(")
    elif computer_score>21:
        print("Computer scored more than 21.You win!!")
    elif your_score>computer_score:
        print("You win!!")
    elif your_score==21:
        print("You win with perfect 21!!")
    elif your_score==computer_score:
        print("Draw")
    else:
        print("You lose :(")

game=True
while game:
    print(art.logo)
    your_cards=deal_cards()
    computer_cards=deal_cards()
    print(f"Your cards:{your_cards}")
    print(f"Computers first card:{computer_cards[0]}")
    if blackjack(your_cards):
        print("Blackjack!! You win")
        game=False
        continue
    if blackjack(computer_cards):
        print("Blackjack:( You lose")
        game=False
        continue
    you=0
    computer=0
    yes_or_no=input("Type 'y' to get another card, Type 'n' to pass:")
    computer = calculate_score(computer_cards,computer)
    you = calculate_score(your_cards,you)
    while yes_or_no=='y':
        your_cards.append(random.choice(cards))
        print(f"Your final hand:{your_cards}")
        you = calculate_score(your_cards,you)
        if you > 21:
            break
        yes_or_no = input("Type 'y' to get another card, Type 'n' to pass: ")
    if yes_or_no == 'n':
        print(f"your final hand:{your_cards}")
        you = calculate_score(your_cards,you)
        while computer<17:
            computer_cards.append(random.choice(cards))
            computer = calculate_score(computer_cards,computer)
        check_for_win(you,computer)
        break

    print(f"Your score: {you} Computer score: {computer}")
    again = input("press 'x' to end game or 'g' to replay")
    if again=='x':
        print("Thank You for playing!!")
        game=False
    elif again=='g':
        print("\n"*100)
        game=True

