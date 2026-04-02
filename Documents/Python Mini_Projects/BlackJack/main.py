import art
import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card


def compre(u_score,c_score):
    if u_score > 21:
        return "You lose.Computer has BlackJack"
    elif c_score>21:
        return "You win.You have blackjack"
    elif u_score==21 and c_score==21:
        return "Draw"
    elif u_score==0:
        return "You win"
    elif c_score==0:
        return "Computer Wins"
    elif u_score>c_score:
        return "You win"
    else:
        return "You lose"

def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)





def play_game():
    user_card = []
    computer_card = []
    u_score=-1
    c_score=-1
    is_game_over=False
    print(art.logo)

    for i in range(2):
        user_card.append([deal_cards()])
        computer_card.append([deal_cards()])

    while not is_game_over:

        total = calculate_score(user_card)
        computer_score =calculate_score(computer_card)
        print(f"your cards {user_card}, current score:{total}")
        print(f"Computer's first hand: {computer_card[0]}")
        if total==0 or computer_score==0 or total>21 :
            is_game_over=True
        else:
           choice= input("Type 'y' to get another card, type 'n' to pass: ")
           if choice== "y":
               user_card.append(deal_cards())
           else :
               is_game_over=True
    while computer_score==0 and computer_score<17:
        computer_card.append(deal_cards())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {total}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compre(total, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print("\n" * 20)
        play_game()
