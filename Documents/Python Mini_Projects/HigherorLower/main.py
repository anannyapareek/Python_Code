import art
import game_data
import random

def random_generate():
    return random.choice(game_data.data)

def format(account):
    account_name=account['name']
    account_description= account['description']
    account_country = account['country']
    return f"{account_name} ,a {account_description}, from {account_country}"

def compare(acc1,acc2):
    f1 =acc1['follower_count']
    f2 = acc2['follower_count']
    if f1>f2:
        return "a"
    else:
        return "b"

def function_main():
    print(art.logo)
    game_play='y'
    score=0

    while game_play=='y':
        a1=random_generate()
        print("Compare A: ", format(a1))
        print(art.vs)
        a2=random_generate()
        while a2==a1:
            a2=random_generate()
        print("Compare B: ", format(a2))
        opt=compare(a1,a2)
        user_input=input("Who has more followers? Type A or B ").lower()
        if user_input == opt:
            game_play='y'
            score+=1
        else:
            game_play='n'
            print("\n"*20)
            print(art.logo)
            print(f"Your final Score:{score} ")

function_main()