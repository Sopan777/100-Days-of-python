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

import random
print("Welcome to the game of Rock Paper and Sissors")
choice = int(input("What do you choose? Type *0* for Rock, *1* for Paper or *2* for Scissors "))
# Printing user choice -----------------------------------------------------------------
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

random_choice =  random.randint(0, 2)
# Printing computer choice -------------------------------------------------------------
if random_choice == 0:
    print(rock)
elif random_choice == 1:
    print(paper)
elif random_choice == 2:
    print(scissors)

# Evaluating the choices ---------------------------------------------------------------
if choice >= 3 or choice < 0:
    print("Invalid Input, You Lose!")
elif choice == 0 and random_choice == 2:                                          
    print("You Wins!")                                                              
elif random_choice == 0 and choice == 2:                                        
    print("You Lose!")                              
elif choice == 2 and random_choice == 1:
    print("You wins!")
elif random_choice == 2 and choice == 1:
    print("You Lose!")
elif choice == 1 and random_choice == 0:
    print("You wins!")
elif random_choice == 1 and choice == 0:
    print("You Lose!")
else:
    print("Draw!")
     

