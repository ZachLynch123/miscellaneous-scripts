import random

random_number = random.randint(1,20)

play_game = True

while play_game == True:
    print(random_number)
    guess = int(input('Welcome to the number testing game! Please enter your number: '))

    if guess == random_number:
        play_again = raw_input('Great you got it right! Play again?(Y/N): ')
        if play_again == 'y' or 'Y':
            play_game = True
        elif play_again == 'n' or 'N':
            play_game = False
            break

    if guess != random_number:
        guess =  int(input('Guess wrong. Please guess again: '))


