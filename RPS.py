import os
import random
import re

os.system('cls' if os.name == 'nt' else 'clear')

while (1 < 2):
    print("\n")
    print('Rock, Paper, Scissors - Shoot!')
    user_choice = input('Choose your weapon: [R]ock, [P]aper or [S]cissors\n>>> ')
    if not re.match('[SsRrPp]', user_choice):
        print('Please, make your choise: \n [R]ock, [P]aper or [S]cissors')
        continue
    print('You choose: ' + user_choice)
    choices = ['R', "S", 'P']
    opponent_choice = random.choice(choices)
    print('I choose: ' + opponent_choice)
    if opponent_choice == str.upper(user_choice):
        print('Tie!')
    elif opponent_choice == 'R' and user_choice == 's'.upper()
        print('Rock beating scissors! I win!')
        continue
    elif opponent_choice == 'S' and user_choice == 'p'.upper():
        print('Scissors beats paper! I win!')
        continue
    elif opponent_choice == 'P' and user_choice == 'r'.upper():
        print('Paper is stronger than rock! I win!! ')
        continue
    else:
        print('You win, Master')
