import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS =3

    playagain = True
    while  playagain:


       

       playerchoice =input('\nenter... \n1 for Rock, \n 2 for Paper , or \n3 for scissors:\n\n')


       player = int(playerchoice)




        if player < 1 or player > 3:
            sys.exit('you must enter 1,2 or 3')


        compchoice = random.choice('123')
        computer = int(compchoice)

     
        print('\nyou chose' + ' '+  str(RPS(player)).replace('RPS.', '') + '.')
        print('python chose' +   ' '+ str(RPS(computer)).replace('RPS.', '') + '.\n')
       


        if player == 1 and computer == 3:
        print("🎉 you win")
        elif player == 2 and computer == 1:
        print('🎉you win!')
        elif player == 3 and computer == 2:
        print('💫you win ')
        elif player == computer:
        print('Tie game')
        else:
        print('🐍python wins!')    

       playagain = input('\nplay again? \nY for yes or \n Q to Quit\n\n')

       if playagain.lower() == 'y':
        continue
        else:
            print(🎉🎉🎉🎁)
            print('thank you  fro playing ! \n')
            playagain = False

 sys.exit('bye! 👋👋')           
