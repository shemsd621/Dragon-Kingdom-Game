import random
import time

print('****************************************')
print('***  Welcome to Dragon Kingdom Game! ***')
print('****************************************')

#introduction to the game
def display_intro():
    print('''\nYou are in the Kingdom of Dragons.
In front of you, you see two caves.
In one cave, the dragon is friendly and will share his treasure with you.
The other dragon is hungry and will eat you on sight.\n''')
print()

#user inputs option
def choose_cave():
    cave = '' # local variable with empty string
    while cave != '1' and cave != '2':
        cave=input('Which cave will you go into? (1 or 2) : ')
        
    return cave

#game process and result    
def check_cave(chosen_cave):
    print('\nYou approach the cave...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! ')
    print('He opens his jaws and...')
    time.sleep(2)   #delays for 2 seconds
    friendlyCave = random.randint(1,2)
    if chosen_cave==str(friendlyCave): 
        print('\nGives you his treasure!')
    else:
        print('\nGobbles you down!')

#main program
done=False
while not done:
    display_intro()
    cave_number=choose_cave()
    check_cave(cave_number)
    option=input('\nPlease enter q to quit or any other key to continue : ')
    if option=='q' or option=='Q':
        print("\nHOPE YOU ENJOYED THE DRAGON KINGDOM GAME!") #the end
        done=True
    else:
        print("Let's play again")





    

        

