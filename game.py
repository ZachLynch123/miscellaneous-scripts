# This exercise helps teach control flow
import random
play = True

while play == True:
    number = random.randint(1, 10)
    guess = int(input('please guess a number 1 through 10: '))
    if guess == number:
        play = False
        keep_playing = raw_input("You're right! Thanks for playing!\n Would you like to play again? (Y/N): ")
        if keep_playing in ['y','Y']:
            play = True
        elif keep_playing in ['n','N'] :
            play = False
        else:
            print('Please input either y or n.')

    else:
        print('please try again\n \n')