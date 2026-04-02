import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice=int(input("Let's Play Rock Paper Scissors! Choose 1 for rock\n Choose 2 for Paper \nChoose 3 for Scissors:"))
pick=["rock","paper","scissors"]
user=pick[choice-1]
if user=="rock":
    print(rock)
if user=="paper":
    print(paper)
if user=="scissors":
    print(scissors)

print("Computer Plays:")
comp=random.randint(1,3)
computer=pick[comp-1]
if computer=="rock":
    print(rock)
if computer=="paper":
    print(paper)
if computer=="scissors":
    print(scissors)

if choice==1 and comp==3 :
    print("You Wins")
elif choice==2 and comp==1:
    print("You Wins")
elif choice==3 and comp==2:
    print("You Wins")
elif choice==comp:
    print("Tie")
else:
    print("Computer Wins")