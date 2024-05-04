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

#Write your code below this line 👇

print("Welcome to the Rock, Paper, Scissors Game!")
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice==0:
    print(rock)
    computer_choice=random.randint(0,2)
    if computer_choice==0:
        print(rock)
        print("Play again")
    elif computer_choice==1:
        print(paper)
        print("You lose")
    elif computer_choice==2:
        print(scissors)
        print("You win")  
    else: print("Choice invalid")

if choice==1:
    print(paper)
    computer_choice=random.randint(0,2)
    if computer_choice==1:
        print(paper)
        print("Play again")
    elif computer_choice==2:
        print(scissors)
        print("You lose")
    elif computer_choice==0:
        print(rock)
        print("You win")  
    else: print("Choice invalid")

if choice==2:
    print(scissors)
    computer_choice=random.randint(0,2)
    if computer_choice==2:
        print(scissors)
        print("Play again")
    elif computer_choice==0:
        print(rock)
        print("You lose")
    elif computer_choice==1:
        print(paper)
        print("You win")  
    else: print("Choice invalid")
