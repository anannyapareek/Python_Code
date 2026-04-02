import art
import random

def input_start():

    choice=input("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100. \nChoose a difficulty. Type 'easy' or 'hard':").lower()
    if choice == "hard":
        return 5
    elif choice == "easy":
        return 10
    else:
        input()

def generate_number():
    num=random.randint(1,100)
    return num

def check_number(a,b):
    if a>b:
        return "Too High"
    elif b>a:
         return "Too Low"
    else:
        return "1"

def run():
    print(art.logo)
    attempt=input_start()
    num=generate_number()
    while not attempt==0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        user_input=int(input("Make a Guess: "))
        temp=check_number(user_input,num)
        if temp == "1":
            print(f"You got it! The answer was {num}")
            attempt=0
        else:
            print(temp)
            if attempt==1:
                print("You have fun out of Guesses!!")
            attempt-=1

run()